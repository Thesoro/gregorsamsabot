# -*- coding: utf-8 -*-
pos = 'Noun'

text = """
==English==
{{wikipedia}}

===Etymology===
From {{etyl|grc|en}} {{term|κακός||bad, wretched|lang=grc}} + {{term|ἔχω|ἔχειν|to have|lang=grc}}.

===Noun===
{{en-noun|~}}

# {{context|medicine|pathology|lang=en}} A systemic [[wasting]] of muscle [[tissue]], with or without loss of fat mass, that accompanies a [[chronic]] [[disease]].
#* '''2007''', Lawrence E. Harrison, ''84: Nutritional Support for the Cancer Patient'', Alfred E. Chang, Patricia A. Ganz, Daniel F. Hayes, Timothy Kinsella, Harvey I. Pass, Joan H. Schiller, Richard M. Stone, Victor Strecher (editors), ''Oncology: An Evidence-Based Approach'', [http://books.google.com.au/books?id=vxh6u1-ETk0C&amp;pg=PA1488&amp;dq=%22cachexia%22%7C%22cachexias%22&amp;hl=en&amp;sa=X&amp;ei=3WFFU4asMMzQkQX8-4DIBQ&amp;redir_esc=y#v=onepage&amp;q=%22cachexia%22%7C%22cachexias%22&amp;f=false page 1488],
#*: Cancer '''cachexia''' is a complex syndrome clinically manifest by progressive involuntary weight loss and diminished food intake and characterized by a variety of biochemical alterations.
#* '''2007''', Toby C. Campbell, Jamie H. Von Roenn, ''Chapter 11: Anorexia/Weight Loss'', Ann M. Berger, John L. Shuster, Jamie H. Von Roenn (editors), ''Principles and Practice of Palliative Care and Supportive Oncology'', [http://books.google.com.au/books?id=LngD6RFXY_AC&amp;pg=PA125&amp;dq=%22cachexia%22%7C%22cachexias%22&amp;hl=en&amp;sa=X&amp;ei=3WFFU4asMMzQkQX8-4DIBQ&amp;redir_esc=y#v=onepage&amp;q=%22cachexia%22%7C%22cachexias%22&amp;f=false page 125],
#*: Cancer '''cachexia''' is a complex metabolic process, due to both host and tumor factors, which results in excess catabolism as well as aberrant fat and carbohydrate metabolism.
#* '''2008''', Mary Marian, Scott A. Shikora, Mary Russell, ''Clinical Nutrition for Surgical Patients'', [http://books.google.com.au/books?id=eFSzlYm0Fx8C&amp;pg=PA84&amp;dq=%22cachexia%22%7C%22cachexias%22&amp;hl=en&amp;sa=X&amp;ei=3WFFU4asMMzQkQX8-4DIBQ&amp;redir_esc=y#v=onepage&amp;q=%22cachexia%22%7C%22cachexias%22&amp;f=false page 84],
#*: Preoperative nutritional therapy in CHF&lt;sup&gt;[Cardiac Heart Failure]&lt;/sup&gt; patients with '''cachexia''' is associated with improved postoperative survival rates (56).
#* '''2009''', Connie W. Bales, Christine S. Ritchie, ''Handbook of Clinical Nutrition and Aging'', [http://books.google.com.au/books?id=jtsBbP2087wC&amp;pg=PA158&amp;dq=%22cachexia%22%7C%22cachexias%22&amp;hl=en&amp;sa=X&amp;ei=3WFFU4asMMzQkQX8-4DIBQ&amp;redir_esc=y#v=onepage&amp;q=%22cachexia%22%7C%22cachexias%22&amp;f=false page 158],
#*: While sarcopenia occurs very commonly with aging, '''cachexia''' occurs mainly in association with acute or chronic disease.

====Translations====
{{trans-top|systemic wasting of muscle tissue that accompanies a chronic disease}}
* Czech: {{t|cs|cachexie|f}}
{{trans-mid}}
* Tagalog: {{t|tl|pamamayat}}
{{trans-bottom}}

===External links===
* {{R:OneLook}}

[[ca:cachexia]]
[[et:cachexia]]
[[io:cachexia]]
[[my:cachexia]]
[[pl:cachexia]]
[[ta:cachexia]]
[[zh:cachexia]]
"""

title = ""

notourpos = ['Verb', 'Adjective', 'Noun', 'Proper Noun', 'Abbreviation']
notourpos.remove(pos)

# for letterone in 'abcdefghijklmnopqr':
#   for lettertwo in 'abcdefghijklmnopqrstuvwxyz':
#     try:
#       x = open('wiktdict.xml.'+letterone+lettertwo)
#     except:
#       pass
#     data = x.read()
#     start = data.find('<page>')
#     end = data.rfind('</page>')
#     print letterone+lettertwo
#     data = data[start:(end+7)]
#     data = "<root>" + data + "</root>"
#     d = xmltodict.parse(data)
#     x.close()

    # for item in d['root']['page']:
    #   try:
    #     title = item['title'].encode('utf8', 'replace')
    #   except AttributeError:
    #     pass
    #   if '#text' in item['revision']['text'].keys():
    #     text = item['revision']['text']['#text'].split("=Translations=")[0]
    #   else:
    #     text = ''
    #   if ':' in title or '==English==' not in text or '=='+pos+'==' not in text:
    #     pass
    #   if len(title) not in range(3,16):
    #     pass
    #   if title[0:4].lower() == "the ":
    #     pass

#we only want words that are first listed as the part of speech we want
for p in notourpos:
  npos = '=='+p
  if npos in text and text.find(npos) < text.find('=='+pos):
    pass
#a line of dashes indicates a section change, so if the noun form is in a different
#  language this will hopefully catch it
if text.find('----') != -1 and text.find('----') < text.find('==Adjective'):
  pass

#we crawl the text to isolate the first definition
defs = ''
multidef = False
defs = text[text.find('=='+pos+'=='):]
defs = defs[defs.find('#')+1:]
end = len(defs)-1
for item in ['--','==','[[','</']:
  i = defs.find(item)
  if i < end and i != -1:
    end = i

defs = defs[:end+1].encode('utf8', 'replace')
print defs
defs = defs.split('# ')

  #there's a lot of obscure and scientific words in the source. we try to remove them here.
badstrings = ['alternate spelling','|rare',
              '{{alternate form', '|obsolete', 'archaic','|anatomy',
              'initialism',"{obsolete",'{{plural', 'archaic',
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
for d in defs:
  if any(xz in d for xz in badstrings):
    defs.remove(d)
    print d
if len(defs) == 0:
  print title
  pass
#any word whose only definition is mostly the word itself is probably some scientific obscurity
if len(title) > 11 and not multidef:
  cont = False
  for num in range(len(title)-9):
    if title[num:(9+num)].lower() in defs[0].lower():
      cont = True
  if cont:
    pass

altext = text.replace('==='+pos+'===','')
if '===' not in altext:
  print title
  pass

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


