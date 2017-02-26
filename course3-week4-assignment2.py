import urllib
from BeautifulSoup import *

# Load page from server
def loadURL(url, position, steps):
    print 'Retrieve ' + url + '...'
    html = urllib.urlopen(url).read()
    # Parse HTML
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags

    tags = soup('a')
    tag = tags[position]
    key, url = tag.attrs[0]

    steps = steps - 1
    if steps >= 0:
        loadURL(url, position, steps)

position = int(raw_input('Position:')) - 1
steps = int(raw_input('Steps:'))

loadURL('http://python-data.dr-chuck.net/known_by_Aymie.html', position, steps)
