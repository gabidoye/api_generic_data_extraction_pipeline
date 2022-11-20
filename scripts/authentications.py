# Authentication in Requests with HTTPBasicAuth
import requests
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('user', 'pass')

print(requests.get('https://httpbin.org/basic-auth/user/pass', auth=auth))

# Returns: <Response [200]>


# Using an Authorization Token as Credentials
import requests

headers = {'Authorization': 'abcde12345'}
print(requests.get('https://httpbin.org/basic-auth/user/pass', headers=headers))

# Returns: <Response [200]>


# Authentication in Requests with HTTPDigestAuth
import requests
from requests.auth import HTTPDigestAuth
auth = HTTPDigestAuth('user', 'pass')

print(requests.get('https://httpbin.org/basic-auth/user/pass', auth=auth))

# Returns: <Response [200]>

# Authenticating Using the OAuth1 Authentication Method
import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

requests.get(url, auth=auth)
#<Response [200]>


# Authenticating with OAuth2 in Requests
from requests_oauthlib import OAuth2Session

# Inlcude your data
client_id = "include your client_id here"
client_secret = "include your client_secret here"
redirect_uri = "include your redirect URI here"

# Create a session object
oauth = OAuth2Session(client_id, redirect_uri = redirect_uri)

# Fetch a token
token = oauth.fetch_token("<url to fetch access token>", client_secret = client_secret)

# Get your authenticated response
resp = oauth.get("URL to the resource")