import xmltodict

o = open('out3.txt','w')

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
      if ':' in title or '==English==' not in text or '==Noun==' not in text:
        continue
      if len(title) not in range(3,16):
        continue
      if title[0:4].lower() == "the ":
        continue
        #there's a lot of obscure and scientific words in the source. we try to remove them here.
      badstrings = ['alternate spelling','|rare',
                    '{{alternate form', '|obsolete', 'archaic','|anatomy',
                    'initialism',"{obsolete","==Proper noun==",'{{plural', 'archaic',
                    'alternative form','alternative spelling', '|historic',
                    '|zoology','|entomology','|inorganic chem', '|organic chem',
                    '|biochemistry','|dated','genus', '{prefix','{suffix','|prefix','|suffix',
                    '|botany', '|geology', '|chemistry', 'A particular', 'subdivision of currency',
                    '|acronym', '|organic compound', '=Abbreviation=', '|abbreviation', 'Abbreviation of', '[drug]',
                    '{abbreviation', '|biology', 'irregular plural', 'plural form',
                    '|protein','|medicine', 'misspelling', 'mispelling', 'polymer', '[molecular formula]',
                    '|mineral','{{synonym of', '|mineralogy','|histology', 'antibiotic', '|surgery',
                    '|pathology','|mycology','{{Webster 1913}}']
      if any(x in text for x in badstrings):
        continue
      #anything that's a verb first isn't what we're looking for.
      #usually this is present participles (e.g. 'a shellacking')
      if '==Verb' in text and text.find('==Verb') < text.find('==Noun'):
        continue
      if '==Adjective' in text and text.find('==Adjective') < text.find('==Noun'):
        continue
      #a line of dashes indicates a section change, so if the noun form is in a different
      #  language this will hopefully catch it
      if text.find('----') != -1 and text.find('----') < text.find('==Noun'):
        continue

      o.write(title)

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
      o.write(is_countable)

      o.write('\n')


o.close()


