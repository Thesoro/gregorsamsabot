import webapp2
import random
import sources
import logging
import urllib
import tweetposter
import quotesources
import quotereqs
import authsec

class samsatweet(webapp2.RequestHandler):
  def get(self):

    orig = "As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into a gigantic insect."
    adjs = []
    firstadj = 'A'
    secondadj = 'A'
    noun = 'A'
    article = 'an '
    superl = ''

    z = open('wikt.adjs', 'r')
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

    o = open('wikt.nouns','r')
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


    temp = "As Gregor Samsa awoke one morning from %s%s dreams he found himself transformed in his bed into %s%s %s." % (superl,firstadj,article,secondadj,noun)
    url = 'https://api.twitter.com/1.1/statuses/update.json?status='+urllib.quote_plus(temp)
    home_timeline = tweetposter.oauth_req( url, authsec.con_keysam, authsec.con_secretsam, authsec.tok_keysam, authsec.tok_secretsam )
    logging.info(home_timeline)
    self.response.write('')

class generaltweet(webapp2.RequestHandler):
  def get(self):

    title = random.choice(quotesources.l.keys())
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
      if c[-3] in ['down', 'in', 'off', 'on', 'by', 'up', 'out']:
        c[-3], c[-2] = c[-2], c[-3]
        f = ' '.join(c)
    f = f[0].upper() + f[1:]
    ppp = len(orig % tuple(words))
    if ppp > 140:
      logging.info(ppp)

    url = 'https://api.twitter.com/1.1/statuses/update.json?status='+urllib.quote_plus(f)
    home_timeline = tweetposter.oauth_req( url, authsec.con_keyope, authsec.con_secretope, authsec.tok_keyope, authsec.tok_secretope)
    logging.info(home_timeline)
    self.response.write('')
    logging.info('tweep!')
    logging.info(f)

app = webapp2.WSGIApplication( [
  # make a dang tweet
  ("/maketweet/samsa/$", samsatweet),
  ("/maketweet/general/$", generaltweet)

], debug=True)

