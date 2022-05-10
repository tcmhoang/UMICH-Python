# Notes
* Integer division return float in python3 not in python2
* `quit()`
* is operator type + value
* `[]` called sub
* Slicing can reference beyond the string (to the end of it)
* `in` operator like contains or `find`
* `dir` show methods in instance
* `lr_strip` trim
* Dictionary also called Associative Array
* For in dictionary  == dictionary.keys()
* ord
* import from or dot notation
* `pass` did not blow up in except clause 

## re lib

* search -> bool
* findAll
    * match can used grouping to extract 

## Port
* 21 -> FTP
* 22 SSH
* 23 Telnet
* 25 SMTP
* 53 DNS
* 143/220/993 IMAP
* 109/110 POP

## socket lib
* create `.socket(AF,SOCKIND)`
* open `.connect(ADDR, PORT)`
* convert str to UTF-8 .decode and .encode
* .send .recv

## urllib
* request.urlopen(url,ctx)
* ctx ssl use ssl lib (HTTPS site)
    * create_default_cntext
    * check_hostname = 
    * verify_mode =
* url.parse.urlencode
* getheaders()

## beautiful soup 
* .soup(tag)
* constructor(string,parser)

## xml.etree,ElementTree lib
* fromstring
* .text
* .get()
* .find(tag)
* findAll(xquery)

## json lib
* loads
* dumps

## oauth
* OAuthConsumer
* OAuthToken
    * OAuthRequest.from_consumer_and_token / .sign_request / .to_url

## String
* python3 unicode -> str
* python2 bstr == unicode 

## OOP
* __init__
* __del__
* inherit using params in class keyword

## sqlite3 lib

* sqlite3.connect -> make connection -> create if not extisted
* cur = instance.cursor()
* cur.execute -> tuple
* cur.fetchone
* conn.commit 
* cur.close


## SQLite
* Insert or Ignore / Replace

## SYS lib
* time.stop

## codecs lib
* codecs.open(FILE,MODE,CHAR COD)
* write
