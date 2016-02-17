x = open('index.adj')
x = x.readlines()

outlist = []
for line in x:
  word = line.split(' ')[0]
  if not word:
    pass
  elif word and word[0].lower() not in 'abcdefghijklmnopqrstuvwxyz':
    pass
  elif len(word) < 3:
    pass
  #get those roman numerals out of here
  elif "cx" in word or "lx" in word or "lv" in word or "xc" in word or "xi" in word or "xx" in word:
    pass
  else:
    outlist.append(word)

o = open('out.txt','w')

o.write('[')
for thing in outlist:
  thing = thing.replace('_',' ')
  thing =  '"' + thing + '"'+","
  o.write(thing)
o.write(']')
o.close()
