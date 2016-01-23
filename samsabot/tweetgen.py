import random
import sources
orig = "As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into a gigantic insect."
firstadj = random.choice(sources.adjlist)
secondadj = random.choice(sources.adjlist)
noun = random.choice(sources.nounlist)

while " " in noun:
  noun = random.choice(sources.nounlist)

article = "a"
if secondadj[0] in 'aeiou':
  article = "an"

temp = "As Gregor Samsa awoke one morning from %s dreams he found himself transformed in his bed into %s %s %s." % (firstadj,article,secondadj,noun)
print temp


