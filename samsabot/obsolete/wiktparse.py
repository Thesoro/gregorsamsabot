import xmltodict

nounfile = open('out3.txt','w')
adjfile = open('out4.txt', 'w')
verbfile = open('out5.txt', 'w')
z = [[verbfile, 'Verb']]
# z = [[nounfile,'Noun'],[adjfile,'Adjective']]

for thing in z:
  pos = thing[1]
  f = thing[0]

  notourpos = ['Verb', 'Adjective', 'Noun', 'Proper Noun', 'Abbreviation']
  notourpos.remove(pos)

  for letterone in 'abcdefghijklmnopqr':
    for lettertwo in 'abcdefghijklmnopqrstuvwxyz':
      try:
        x = open('wiktdict.xml.'+letterone+lettertwo)
      except:
        continue
      data = x.read()
      start = data.find('<page>')
      end = data.rfind('</page>')
      print letterone+lettertwo
      data = data[start:(end+7)]
      data = "<root>" + data + "</root>"
      d = xmltodict.parse(data)
      x.close()

      for item in d['root']['page']:
        try:
          title = item['title'].encode('utf8', 'replace')
        except AttributeError:
          continue
        if '#text' in item['revision']['text'].keys():
          text = item['revision']['text']['#text'].split("=Translations=")[0]
        else:
          text = ''
        if ':' in title or '==English==' not in text or '=='+pos+'==' not in text:
          continue
        if len(title) not in range(3,16):
          continue
        if title[0:4].lower() == "the ":
          continue

        verbtype = False

        #we only want words that are first listed as the part of speech we want
        contcheck = False
        for p in notourpos:
          npos = '=='+p
          if npos in text and text.find(npos) < text.find('=='+pos):
            contcheck = True

        if contcheck:
          continue
        #a line of dashes indicates a section change, so if the noun form is in a different
        #  language this will hopefully catch it
        if text.find('----') != -1 and text.find('----') < text.find('=='+pos):
          continue

        #we crawl the text to isolate the first definition
        defs = ''
        pl = False
        defs = text[text.find('=='+pos+'=='):]
        info = defs[:defs.find('#')]
        defs = defs[defs.find('#')+1:]
        end = len(defs)-1
        for item in ['--','==','</']:
          i = defs.find(item)
          if i < end and i != -1:
            end = i
        defs = defs[:end+1].encode('utf8', 'replace')
        defs = defs.split('# ')

          #there's a lot of obscure and scientific words in the source. we try to remove them here.
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
                      '|steroid','[[BAN]]', 'fandom ', 'A medication', 'prodrug', ]
        filtereddefs = []
        for d in defs:
          if any(xz in d for xz in badstrings):
            pass
          else:
            filtereddefs.append(d)
        if len(filtereddefs) == 0:
          # print title
          continue
        #any word whose only definition is mostly the word itself is probably some scientific obscurity
        if len(title) > 11 and len(filtereddefs) == 1:
          cont = False
          for num in range(len(title)-9):
            if cont:
              break
            if title[num:(9+num)].lower() in filtereddefs[0].lower():
              cont = True
          if cont:
            continue

        #we only want things that are the part of speech we're looking for in the language were lookin for
        if all(k not in text for k in ['{{en-'+pos[0:3].lower(), 'en|'+pos[0:3].lower()]):
          if pos == "Noun" and 'plural' in info:
            pl = True
          # elif pos == "Verb" and any('participle' in t for t in filtereddefs):
          #   verbtype =
          elif pos == "Verb" and any('participle' in t for t in filtereddefs):
            for de in filtereddefs:
              if "participle" in de:
                verbtype = 'part'
                if 'present' in de:
                  verbtype = 'pres' + verbtype
                elif 'past' in de:
                  verbtype = 'past' + verbtype
                break
          else:
            # print title
            continue
        if pos == 'Verb' and not verbtype:

          infolist = info.split('verb')[1].split('|')
          if 'obsolete' in infolist[:3]:
            # print title
            continue

          if any('[' in item for item in infolist):
            print title
            continue
        altext = text.replace('==='+pos+'===','')
        if '===' not in altext:
          # print title
          continue
        f.write(title)

        if pos == "Noun":
          is_countable = '|||'
          if '{{en-noun' in text:
            sect = text[text.find('{{en-noun'):]
            nc = ['|-', '-}}']
            sectb = text[:text.find('}}')+2]
            if any(item in sectb for item in nc):
              is_countable += 'no'
            elif "{{en-noun|~" in text:
              is_countable += 'both'
            else:
              is_countable += "yes"
          else:
            is_countable += "yes"
          f.write(is_countable)

          f.write('|||'+str(pl))


        if pos == "Adjective":
          f.write('|||')
          if title[-3:] == "est" and title[-6:] not in ['modest','honest']:
            f.write('super')
          else:
            f.write('not')
          f.write('|||')
          usea = True
          if title[0].lower() in 'aeiou':
            usea = False
          exceptionlist = ['usu', 'use', 'honor', 'honest', 'one-', 'one ']
          for item in exceptionlist:
            if title[:(len(item))].lower() == item:
              usea = not usea

          if usea:
            f.write('a')
          else:
            f.write('an')

        if pos == "Verb":
          f.write('|||')
          if "en-past of" in title:
            f.write('past')
          elif len(infolist) == 1:
            f.write('std')
          elif len(infolist) == 2:
            f.write('rt:'+(infolist[1].replace('}','').replace('\n','')).encode('utf8', 'replace'))
          elif verbtype:
            f.write(verbtype)
          else:
            f.write('`'.join(infolist))
          f.write('|||')

        f.write('\n')


  f.close()




