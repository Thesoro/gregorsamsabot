import random
import sources

orig = "As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into a gigantic insect."
adjs = []
firstadj = 'A'
secondadj = 'A'
noun = 'A'
article = 'an '
superl = ''

z = open('out4.txt', 'r')
x = z.readlines()
while firstadj[0].isupper() or secondadj[0].isupper():
  num = random.randint(0,len(x)) - 1
  num2 = random.randint(0,len(x)) - 1
  for n in [num, num2]:
    s = x[n].split('|||')
    s[2] = s[2][:-1]
    adjs.append(s)

  firstadj = adjs[0][0]
  secondadj = adjs[1][0]

o = open('out3.txt','r')
l = o.readlines()

while noun[0].isupper():
  num = random.randint(0,len(l)) - 1

  f = l[num].split('|||')
  f[1] = f[1][:-1]

  countable = f[1]
  noun = f[0]

if countable == 'yes':
  article = 'a '
elif countable == 'no':
  article = ''
elif countable == 'both':
  coin = random.randint(0,1)
  if coin == 0:
    article = 'a '
  if coin == 1:
    article = ''
else:
  article = 'a '

if adjs[0][1] == "super":
  superl = "the "

if article and adjs[1][1] == "super":
  article = "the "
elif article and ('False' in f[2]):
  article = adjs[1][2] + ' '
elif article and ('True' in f[2]):
  article = ' '
else:
  article = ' '


temp = "As Gregor Samsa awoke one morning from %s%s dreams he found himself transformed in his bed into %s%s %s." % (superl,firstadj,article,secondadj,noun)
print temp
