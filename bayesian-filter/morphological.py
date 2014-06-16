# -*- coding: utf-8 -*-
import urllib
import urllib3
from BeautifulSoup import BeautifulSoup

appid = "dj0zaiZpPVluZUthQzFlVFpXTiZzPWNvbnN1bWVyc2VjcmV0Jng9NWQ-"
pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse"

def split(sentence, appid=appid, result="ma", filter="1|2|3|4|5|9|10"):
    sentence = sentence.encode("utf-8")
    params = urllib.urlencode({'appid':appid, 'results':results, 'filter':filter,'sentence':sentence})
    results = urllib2.urlopen(pageurl, params)
    soup = BeautifulSoup(results.read())
    
    return [w.surface.string for w in soup.ma_result.word_list]
