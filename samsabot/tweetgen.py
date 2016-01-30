import random
import quotesources
import quotereqs

title = "Moby Dick"
m = quotesources.l[title]
reqs = m['reqs']
orig = m['orig']
words = []
dupelist = []
for l in range(0,len(reqs)):
  a = reqs[l]

  if a.dupe:
    #[where to place, where to dupe]
    dupelist.append([l, a.dupe])
  else:
    pos = a.pos
    z = open(pos+'.txt')
    x = z.readlines()
    valuechecks = False
    while not valuechecks:
      valuechecks = True
      num = random.randint(0,len(x)) - 1
      l = x[num][:-1].split('|||')
      word = l.pop(0)
      for f in a.valuesearchers:
        if f and not f in l or (f == "yes" and "both" not in l and "yes" not in l):
          valuechecks = False
      if a.needsarticle:
        word = l[-1]+ ' ' + word
    words.append(word)

for item in dupelist:
  words.insert(item[0], words[item[1]])

f = orig % tuple(words)
#ishmael gets a little custom formatting because he's imperative
if title == "Moby Dick" and len(words[0].split(' ')) > 1:
  c = f.split(' ')
  print c
  if c[-3] in ['down', 'in', 'off', 'on', 'by', 'up', 'out']:
    c[-3], c[-2] = c[-2], c[-3]
    f = ' '.join(c)
print f[0].upper() + f[1:]
ppp = len(orig % tuple(words))
if ppp > 140:
  print ppp
