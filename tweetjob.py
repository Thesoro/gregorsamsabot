import webapp2
import logging
import urllib
import tweetposter
import authsec

class samsatweet(webapp2.RequestHandler):
  def get(self):
    self.response.write('')
    f = tweetposter.construct_tweet("Metamorphosis")
    url = 'https://api.twitter.com/1.1/statuses/update.json?status='+urllib.quote_plus(f)
    k = authsec.sam
    c = k['con']
    t = k['token']
    home_timeline = tweetposter.oauth_req( url, c['key'], c['secret'], t['key'], t['secret'] )
    logging.info(home_timeline)
    logging.info('tweep!')
    logging.info(f)

class generaltweet(webapp2.RequestHandler):
  def get(self):
    self.response.write('')
    f = tweetposter.construct_tweet()
    url = 'https://api.twitter.com/1.1/statuses/update.json?status='+urllib.quote_plus(f)
    k = authsec.ope
    c = k['con']
    t = k['token']
    home_timeline = tweetposter.oauth_req( url, c['key'], c['secret'], t['key'], t['secret'])
    logging.info(home_timeline)
    logging.info('tweep!')
    logging.info(f)

class badplur(webapp2.RequestHandler):
  def get(self):
    self.response.write('')
    f = tweetposter.wrong_pluralization()
    url = 'https://api.twitter.com/1.1/statuses/update.json?status='+urllib.quote_plus(f)
    k = authsec.plu
    c = k['con']
    t = k['token']
    home_timeline = tweetposter.oauth_req( url, c['key'], c['secret'], t['key'], t['secret'])
    logging.info(home_timeline)
    logging.info('tweep!')
    logging.info(f)

class blants(webapp2.RequestHandler):
  def get(self):
    f = tweetposter.blants_tweet()
    self.response.write(f)

    url = 'https://api.twitter.com/1.1/statuses/update.json?status='+urllib.quote_plus(f)
    k = authsec.bla
    c = k['con']
    t = k['token']
    home_timeline = tweetposter.oauth_req( url, c['key'], c['secret'], t['key'], t['secret'])
    logging.info(home_timeline)
    logging.info('tweep!')
    logging.info(f)

app = webapp2.WSGIApplication( [
  # make a dang tweet
  ("/maketweet/samsa/$", samsatweet),
  ("/maketweet/general/$", generaltweet),
  ("/maketweet/badplur/$", badplur),
  ("/maketweet/blants/$", blants),

], debug=True)

