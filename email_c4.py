# import urllib3
# import sqlite3

# http = urllib3.PoolManager()
# r = http.request('GET',
#                  'https://www.py4e.com/code3/mbox.txt')


# with sqlite3.connect('testdb.sqlite') as db:
#     cur = db.cursor()
#     cur.executescript('''
#     DROP TABLE IF EXISTS Counts;
#     CREATE TABLE Counts(
#         org TEXT,
#         count INTEGER
#     )
#     ''')

#     for line in r.data.decode().split('\n'):
#         if not line.startswith('From '):
#             continue
#         pieces = line.split()
#         org = pieces[1].split('@')[1]
#         cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
#         curcount = cur.fetchone()
#         if curcount is None:
#             cur.execute('''INSERT INTO Counts (org, count)
#             VALUES (?, 1)''', (org,))
#         else:
#             cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#                         (org,))
# db.commit()
