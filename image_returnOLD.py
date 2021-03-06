import urllib2
import simplejson
import socket




def queryFind(array):
	query=""
	for i in xrange(len(array)-1):
		query+=array[i]+"%20"

	query+=array[len(array)-1]
	return query

#adds keywords in Google URL encoding

def urlFind(array,imageRange):
	
	query=queryFind(array)
	ip=socket.gethostbyname(socket.gethostname())
	queryURLS=[]
	for x in xrange(imageRange[0],imageRange[1],imageRange[2]):
		imageNum=str(x)
		queryURLS.append(('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+query+'&userip='+ip+'&start='+imageNum))
	return queryURLS

#finding the url to search by query = key1 + %20 + key2 ... and image Number

def googlePrep(array,imageRange):
	
	queryURLS=urlFind(array,imageRange)
	imageURLS=[];
	for queryURL in queryURLS:
		request = urllib2.Request(queryURL, None, {'Referer': 'http://www.google.com'})
		response = urllib2.urlopen(request)
		results = simplejson.load(response)
		for result in results['responseData']['results']:
			    imageURLS.append(result['unescapedUrl']);
	return imageURLS
#takes array of keywords and imagerage, sends request and receives response, returns Image URL


print googlePrep(array,(1,3,1))