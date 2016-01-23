import oauth2
import authsec

def oauth_req(url, key, secret, http_method="POST", post_body='status: "SMARF"', http_headers=None):
    consumer = oauth2.Consumer(key=authsec.con_key, secret=authsec.con_secret)
    token = oauth2.Token(key=authsec.tok_key, secret=authsec.tok_secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

