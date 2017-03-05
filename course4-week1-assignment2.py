import sqlite3
import re

conn = sqlite3.connect('course4-week1-assignment2.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    # Extract organization from any line that has the following structure From: user@orgaization.sample
    org = re.findall('^From: \S+@(\S+)+?',line)

    # Skip if no matching From line could be found
    if len(org) == 0: continue

    print org[0]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org[0], ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', ( org[0], ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
            (org[0], ))

# Commit changes to disk after all From lines have been processed
conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
