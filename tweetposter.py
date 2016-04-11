import oauth2
import quotesources
import quotereqs
import random
import logging


def oauth_req(url, key, secret, tokenkey, tokensecret, http_method="POST", post_body='status: "SMARF"', http_headers=None):
  consumer = oauth2.Consumer(key=key, secret=secret)
  token = oauth2.Token(key=tokenkey, secret=tokensecret)
  client = oauth2.Client(consumer, token)
  resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
  return content

def construct_tweet(title=False):
  if not title:
    r = random.randint(0,len(quotesources.l.keys())) - 1
    title = quotesources.l.keys()[r]
  m = quotesources.l[title]
  logging.info(title)
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
        if pos == "Noun":
          l[1] = l[1].split('`')[0]
        l = "|||".join(l)

        for f in a.valuesearchers:
          if f and not f in l:
            valuechecks = False
          if (f == "yes" or f == "no") and "both" in l:
            valuechecks = True
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

  return f

def wrong_pluralization():
  word = ""
  z = open('dictionary/Noun.txt')
  x = z.readlines()
  while " " not in word:
    num = random.randint(0,len(x)) - 1
    l = x[num][:-1].split('|||')
    word = l.pop(0)
  word = word.split(' ')
  if word[0][-1] in ['s', 'h', 'x', 'z']:
    pl = 'es'
  elif word[0][-1] in ['y'] and word[0][-2] not in ['a','e','i','o','u']:
    word[0] = word[0][0:-1]
    pl = 'ies'
  else:
    pl = 's'
  if "'" in word[0]:
    word[0] = word[0].replace("'", "")
    word[0] = word[0] + "'"
    pl = ''
  word[0] = word[0]+pl
  word = ' '.join(word)
  return "Actually, the correct pluralization is "+word+"."
