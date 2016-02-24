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
    home_timeline = tweetposter.oauth_req( url, authsec.con_keysam, authsec.con_secretsam, authsec.tok_keysam, authsec.tok_secretsam )
    logging.info(home_timeline)
    logging.info('tweep!')
    logging.info(f)

class generaltweet(webapp2.RequestHandler):
  def get(self):
    self.response.write('')
    f = tweetposter.construct_tweet()
    url = 'https://api.twitter.com/1.1/statuses/update.json?status='+urllib.quote_plus(f)
    home_timeline = tweetposter.oauth_req( url, authsec.con_keyope, authsec.con_secretope, authsec.tok_keyope, authsec.tok_secretope)
    logging.info(home_timeline)
    logging.info('tweep!')
    logging.info(f)

app = webapp2.WSGIApplication( [
  # make a dang tweet
  ("/maketweet/samsa/$", samsatweet),
  ("/maketweet/general/$", generaltweet)

], debug=True)

