import xmltodict
import wiktword

p = wiktword.Word('', '')
poslist = p.poslist
filelist = {}
for p in poslist:
    filelist[p] = open('output/'+p+'.txt', 'w')


for letterone in 'abcdefghijklmnopqr':
    for lettertwo in 'abcdefghijklmnopqrstuvwxyz':
      try:
        x = open('dictionary/wiktdict.xml.'+letterone+lettertwo)
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
          text = item['revision']['text']['#text'].split("=Translations=")[0].split('----')[0]
        else:
          continue

        w = wiktword.Word(title, text)
        if not w.checkPartOfSpeech():
          continue
        w.parseDefsAndInfo()
        if not w.filterDefs():
          continue
        if not w.filterInfo():
          continue
        w.getMetaInfo()

        if len(w.text) < 140:
          # print w.title
          continue

        # print w.textline
        filelist[w.pos].write(w.title)
        filelist[w.pos].write(w.textline)






for p in poslist:
    filelist[p].close()

