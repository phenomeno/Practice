## Check if the Internet is up and keep a log of when it goes down
## Written by Stewart Park
## Annotations by Grace Lee


## open python in any environment  (linux, mac, etc)
## universal coding

#!/usr/bin/env python
#-*- coding: utf-8 -*-



## use urllib2 to check if internet is on
## use datetime to incl. date in log. we import to avoid having to reference the lib
## and use only the module name datetime (namespace- ex) datetime.datetime.now())
## (scope - what functions/modules are available at this level)
## import time to use the sleep function


import urllib2
from datetime import datetime
import time


## while True- keep these running throughout, nothing to shut these off
## variable h will open the website
## variable f will open a log file in append mode
## ./ implies that it will kept in the current folder
## we set Flag to True to signify that the internet is working

while True:
    h = urllib2.urlopen('http://google.com')
    f = open('./internet-connection.log', 'a')
    flag = True
    
    
## 'with' means you dont have to close f later on 
## variable data will scan through the url
## we search for a term that will only be in the source code if the internet is up
## note the 'not in' syntax
## 'if flag' means if flag is true
## we write in the log with the two conditions- if the term is not in source code
## AND the internet flag is on or working
## we do this to circumvent the situation where internet is not working and term
## is not present (will give more than one log per down event)
## note 'f.write' and the string formatting (%s)
## set the flag to False to note that it is down
## else: if the term is in the source code
## use 'time.sleep(30)' to check every 30 secs
## keep the flag as True- internet still works
## close the url for h since h is not in the 'with' part

    with f:
        data = h.read()
        if 'google_favicon' not in data:
            if flag:
                f.write("[%s] Internet connection is down\n" % str(datetime.now()))
                flag = False
        else:
            time.sleep(30)
            flag = True
        h.close()