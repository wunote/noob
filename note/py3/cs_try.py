from urllib.request import urlopen
from urllib import error

try:
    html = urlopen('http://jandan.net/ooxx')
except error.HTTPError as err:
    print("Exception", err)

try:
    print (1/0)
except ZeroDivisionError as err:
    print ('Exception: ', err)
