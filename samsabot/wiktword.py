# -*- coding: utf-8 -*-

class Word:
  def __init__(self, title, text):
    self.title = title
    self.text = text
    self.info = ''
    self.pos = None
    self.poslist = ['Verb', 'Adjective', 'Noun', 'Proper noun', 'Abbreviation', 'Past Participle', 'Present Particple']


    self.defs = []
    self.filtereddefs = []
    self.plural = False
    self.infolist = []

    self.textline = ''


  def checkPartOfSpeech(self):
    if ':' in self.title or '==English==' not in self.text:
      return False
    if len(self.title) not in range(3,16):
      return False
    if self.title[0:4].lower() == "the ":
      return False
    pospositions = {}
    for p in self.poslist:
      pospositions[p] = self.text.find('=='+p+'==')

    for key in pospositions.keys():
      if pospositions[key] == -1:
        del pospositions[key]

    if pospositions:
      self.pos = min(pospositions, key=pospositions.get)


    return self.pos

  #turns the info into a string and the definitions into an array
  def parseDefsAndInfo(self):
    d = self.text[self.text.find('=='+self.pos+'=='):]
    self.info = d[:d.find('#')]
    d = d[d.find('#')+1:]
    end = len(d)-1
    for item in ['--','==','</']:
      i = d.find(item)
      if i < end and i != -1:
        end = i
    d = d[:end+1].encode('utf8', 'replace')
    self.defs = d.split('# ')

  #removes definitions based on a number of criteria. we aim to remove obscure, obsolete, and archaic words
  def filterDefs(self):
    badstrings = ['alternate spelling','|rare',
                  '{{alternate form', '|obsolete', 'archaic','|anatomy',
                  'initialism',"{obsolete",'{{plural',
                  'alternative form','alternative spelling', '|historic',
                  '|zoology','|entomology','|inorganic', '|organic',
                  '|biochemistry','|dated','genus', '{prefix','{suffix','|prefix','|suffix',
                  '|botany', '|geology', '|chemistry', 'A particular', 'subdivision of currency',
                  '|acronym', '|abbreviation',
                  'Abbreviation of', '[drug]','{alt form',
                  '{abbreviation', '|biology', 'irregular plural', 'plural form',
                  '|protein','|medicine', 'misspelling', 'mispelling', 'polymer', '[molecular formula]',
                  '|mineral','{{synonym of', '|mineralogy','|histology', 'antibiotic', '|surgery',
                  '|pathology','|mycology','{{Webster 1913}}','|ornithology', 'fungi of the family',
                  '|pharma','|ichthyology','{alternative', 'alternative case',
                  '|steroid','[[BAN]]', 'fandom ', 'A medication', 'prodrug', 'dated form of', '|dated', '{dated',
                  'antibody', 'steroid', '|cytology', '|law', '|historic']
    for d in self.defs:
      if any(xz in d for xz in badstrings):
        pass
      else:
        self.filtereddefs.append(d)
    if len(self.filtereddefs) == 0:
      # print title
      return False


    #any word whose only definition is mostly the word itself is probably some scientific obscurity
    if len(self.title) > 9 and len(self.filtereddefs) == 1:
      cont = False
      for num in range(len(self.title)-9):
        if cont:
          break
        if self.title[num:(9+num)].lower() in self.filtereddefs[0].lower():
          cont = True
      if cont:
        return False

    return True

  #filters out words based on if their metainfo is up to snuff.
  def filterInfo(self):
    #we only want things that are the part of speech we're looking for in the language were lookin for
    #this also picks up participles and plural metainfo

    if all(k not in self.info for k in ['{{en-'+self.pos[0:3].lower(), 'en|'+self.pos[0:3].lower()]):
      if self.pos == "Noun" and 'plural' in self.info:
        self.plural = True
      elif "past participle" in self.info:
        self.pos = "Past Participle"
      elif "present participle" in self.info:
        self.pos = "Present Participle"
      elif self.pos == "Verb" and any('participle' in t for t in self.filtereddefs):
        for de in self.filtereddefs:
          if "participle" in de:
            if 'past' in de:
              self.pos = "Past Participle"
            elif 'present' in de:
              self.pos = "Present Participle"
      else:
        return False

    if self.pos == 'Verb':
      # print self.info
      self.infolist = self.info.split('verb')[1].split('|')

      #sometimes the 'obsolete' marker is listed in info rather than the defs
      # if it's one of the first three forms, shut it all down
      if 'obsolete' in self.infolist[:3]:
        # print self.title
        return False

    # this bit catches words with only one section in them, on the principle
    # that they're usually not very well fleshed out and are often silly pharmaceutical brand names
    altext = self.text.replace('==='+self.pos+'===','')
    if '===' not in altext:
      # print self.title
      return False


    # #this part originally filtered out verbs that had links to other words in their info
    # #but this isn't necessary and filters out all sorts of reasonable
    # #compound verbs ('take part', 'abut on')

    # if any('[' in item for item in self.infolist):
    #   return False

    return True

  def getMetaInfo(self):

    if self.pos == "Noun":
      is_countable = '|||'
      if '{{en-noun' in self.text:
        sect = self.text[self.text.find('{{en-noun'):]
        nc = ['|-', '-}}']
        sectb = self.text[:self.text.find('}}')+2]
        if any(item in sectb for item in nc):
          is_countable += 'no'
        elif "{{en-noun|~" in self.text:
          is_countable += 'both'
        else:
          is_countable += "yes"
      else:
        is_countable += "yes"
      self.textline += (is_countable)

      self.textline += ('|||'+str(self.plural))


    if self.pos == "Adjective":
      self.textline += ('|||')
      if "superlative" in self.text:
        self.textline += ('super')
      else:
        self.textline += ('not')
      self.textline += ('|||')
      usea = True

    if self.pos == "Verb":
      self.textline += ('|||')
      if "en-past of" in self.info:
        self.textline += ('past')
      elif len(self.infolist) == 1:
        self.textline += ('std')
      elif len(self.infolist) == 2:
        self.textline += ('rt:'+(self.infolist[1].replace('}','').replace('\n','')))
      else:
        self.textline += ('`'.join(self.infolist).replace('\n','').replace('}',''))

    #everybody gets an article
    self.textline += ('|||')
    #first we look for an ipa pronunciation
    # pronun = self.text.split('ciation===')[-1]
    # print pronun
    # .split('IPA|/')
    # print pronun
    # if len(pronun) > 1:
    #   init = pronun[1].split('/')[0]
    #   init = init.replace('ˈ','')
    #   init = init[0]
    #   print init

    #   if init in'ʌɑ:æeɜ:ɪi:ɒɔ:ʊu:aɪaʊeɪoʊɔɪeəɪəʊə':
    #     print 'meep'
    #     self.textline += "an"
    #   else:
    #     print 'honk'
    #     self.textline += "a"
    #elif
    if self.title[0].lower() in 'aeiou':
      usea = False
      exceptionlist = ['usu', 'use', 'honor', 'honest', 'one-', 'one ']
      for item in exceptionlist:
        if self.title[:(len(item))].lower() == item:
          usea = not usea

      if usea:
        self.textline += ('a')
      else:
        self.textline += ('an')
    else:
      self.textline += ('a')

    self.textline += ('\n')
    self.textline = self.textline.encode('utf8', 'replace')


