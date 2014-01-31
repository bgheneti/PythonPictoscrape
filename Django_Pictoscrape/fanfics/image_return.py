import urllib2
import simplejson
import socket
import re, string


def queryFind(array):
	query=""
	for i in xrange(len(array)-1):
		query+=array[i]+"%20"

	query+=array[len(array)-1]
	return query

#adds keywords in Google URL encoding

def urlFind(keyword):
	keywords=keyword.split()
	print keywords
	if len(keywords)>1:
		keyword = keywords[0]
		for i in xrange(1,len(keywords)):
			print keywords[i]
			word=re.sub('[\W_]+', '', keywords[i])
			print "word:",word
			keyword+="%20"+word
	print keyword
	ip=socket.gethostbyname(socket.gethostname())
	queryURL='https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+keyword+'&userip='+ip
	return queryURL

#finding the url to search by query = key1 + %20 + key2 ... and image Number

def googlePrep(keyword):
	queryURL=urlFind(keyword)
	request = urllib2.Request(queryURL, None, {'Referer': 'http://www.google.com'})
	response = urllib2.urlopen(request)
	results = simplejson.load(response)
	for result in results['responseData']['results']:
		return result['unescapedUrl']

#takes array of keywords and imagerage, sends request and receives response, returns Image URL


print googlePrep("apple")