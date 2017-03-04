import urllib
import json

# Load sample xml data
uh = urllib.urlopen('http://python-data.dr-chuck.net/comments_357862.json')
raw_data = uh.read()

# Loop through comments and sum the individual comment counts
print sum([ comment['count'] for comment in json.loads(raw_data)['comments']])
