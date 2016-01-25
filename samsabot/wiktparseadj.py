import xmltodict

o = open('out4.txt','w')

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
      if ':' in title or '==English==' not in text or '==Adjective==' not in text:
        continue
      if len(title) not in range(3,16):
        continue
      if title[0:4].lower() == "the ":
        continue

      #we crawl the text to isolate the first definition
      defs = ''
      multidef = False
      defs = text[text.find('==Adjective=='):]
      defs = defs[defs.find('#')+1:]
      end = len(defs)-1
      for item in ['--','==','[[','</']:
        i = defs.find(item)
        if i < end and i != -1:
          end = i

      defs = defs[:end+1].encode('utf8', 'replace')
      defs = defs.split('# ')

        #there's a lot of obscure and scientific words in the source. we try to remove them here.
      badstrings = ['alternate spelling','|rare',
                    '{{alternate form', '|obsolete', 'archaic','|anatomy',
                    'initialism',"{obsolete","==Proper noun==",'{{plural', 'archaic',
                    'alternative form','alternative spelling', '|historic',
                    '|zoology','|entomology','|inorganic chem', '|organic chem',
                    '|biochemistry','|dated','genus', '{prefix','{suffix','|prefix','|suffix',
                    '|botany', '|geology', '|chemistry', 'A particular', 'subdivision of currency',
                    '|acronym', '|organic compound', '=Abbreviation=', '|abbreviation',
                    'Abbreviation of', '[drug]','{alt form',
                    '{abbreviation', '|biology', 'irregular plural', 'plural form',
                    '|protein','|medicine', 'misspelling', 'mispelling', 'polymer', '[molecular formula]',
                    '|mineral','{{synonym of', '|mineralogy','|histology', 'antibiotic', '|surgery',
                    '|pathology','|mycology','{{Webster 1913}}','|ornithology', 'fungi of the family',
                    '|pharmacology','|ichthyology','{alternative', 'alternative case']
      if any(x in text for x in badstrings):
        continue
      #any word whose only definition is mostly the word itself is probably some scientific obscurity
      if len(title) > 11 and not multidef:
        if title[:10].lower() in fd.lower():
          continue
      #anything that's a verb first isn't what we're looking for.
      #usually this is present participles (e.g. 'a shellacking')
      if '==Verb' in text and text.find('==Verb') < text.find('==Adjective'):
        continue

      #a line of dashes indicates a section change, so if the noun form is in a different
      #  language this will hopefully catch it
      if text.find('----') != -1 and text.find('----') < text.find('==Adjective'):
        continue


      o.write(title)
      o.write('|||')

      if title[-3:] == "est" and title[-6:] not in ['modest','honest']:
        o.write('super')
      else:
        o.write('not')

      o.write('|||')

      usea = True
      if title[0].lower() in 'aeiou':
        usea = False
      exceptionlist = ['usu', 'use', 'honor', 'honest', 'one-', 'one ']
      for item in exceptionlist:
        if title[:(len(item))].lower() == item:
          usea = not usea

      if usea:
        o.write('a')
      else:
        o.write('an')

      o.write('\n')


o.close()
