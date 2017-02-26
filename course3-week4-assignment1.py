import urllib
from BeautifulSoup import *

# Load page from server
html = urllib.urlopen('http://python-data.dr-chuck.net/comments_357861.html').read()

# Parse HTML
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')

# Sum comments and print the sum
print sum([ int(tag.contents[0]) for tag in tags ])
