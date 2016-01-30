import oauth2

def oauth_req(url, key, secret, tokenkey, tokensecret, http_method="POST", post_body='status: "SMARF"', http_headers=None):
    consumer = oauth2.Consumer(key=key, secret=secret)
    token = oauth2.Token(key=tokenkey, secret=tokensecret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

