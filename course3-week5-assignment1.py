import urllib
import xml.etree.ElementTree as ET

# Load sample xml data
uh = urllib.urlopen('http://python-data.dr-chuck.net/comments_357858.xml')
xml_data = uh.read()

# Loop through comments and sum the individual comment counts
print sum( [ int(comment.find('count').text) for comment in ET.fromstring(xml_data).findall('comments/comment')])
