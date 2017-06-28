from data_retrieve import *
from html_parser import *

dt = DataRetrieve()

hp = MyHTMLParser()
hp.feed(dt.html_string)

url = 'output/1.txt'

fp = open(url, 'w')
