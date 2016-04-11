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

#an attempt to get the server to wake up so ope will actually tweet every three hours
class wakeup(webapp2.RequestHandler):
  def get(self):
    self.response.write('')
    logging.info('wake up!')

app = webapp2.WSGIApplication( [
  # make a dang tweet
  ("/maketweet/samsa/$", samsatweet),
  ("/maketweet/general/$", generaltweet),
  ("/maketweet/badplur/$", badplur),
  ("/maketweet/wakeup/$", wakeup)

], debug=True)

