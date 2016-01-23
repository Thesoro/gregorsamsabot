import webapp2
import random
import sources
import logging
import urllib
import oauth2 as oauth
import time
import tweetposter

class maketweet(webapp2.RequestHandler):
  def get(self):


    logging.info('meep')



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
    url = 'https://api.twitter.com/1.1/statuses/update.json?status='+urllib.quote_plus(temp)
    home_timeline = tweetposter.oauth_req( url, 'abcdefg', 'hijklmnop' )
    logging.info(home_timeline)
    self.response.write('')


app = webapp2.WSGIApplication( [
  # make a dang tweet
  ("/maketweet/hourly/$", maketweet)
], debug=True)

