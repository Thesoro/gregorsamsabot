import webapp2
import random
import logging
import urllib
import tweetposter
import quotesources
import quotereqs
import authsec

class samsatweet(webapp2.RequestHandler):
  def get(self):

    title = "Metamorphosis"
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
        z = open('dictionary/'+pos+'.txt')
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

    f = f[0].upper() + f[1:]
    ppp = len(orig % tuple(words))
    if ppp > 140:
      logging.info(ppp)

    # url = 'https://api.twitter.com/1.1/statuses/update.json?status='+urllib.quote_plus(f)
    # home_timeline = tweetposter.oauth_req( url, authsec.con_keysam, authsec.con_secretsam, authsec.tok_keysam, authsec.tok_secretsam )
    # logging.info(home_timeline)
    self.response.write('')
    logging.info('tweep!')
    logging.info(f)

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
        z = open('dictionary/'+pos+'.txt')
        x = z.readlines()
        valuechecks = False
        while not valuechecks:
          valuechecks = True
          num = random.randint(0,len(x)) - 1
          l = x[num][:-1].split('|||')
          z = l.pop(1).split('`')
          l = l[:1] + z + l[1:]
          word = l.pop(0)
          for f in a.valuesearchers:
            if f and not f in l or (f == "yes" and "both" not in l and "yes" not in l):
              valuechecks = False
          if a.needsarticle:
            word = l[-1]+ ' ' + word
          if a.pluralform:
            if l[1] == "normal" or len(l[1]) < len(word):
              word += "s"
            else:
              word = l[1]
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

