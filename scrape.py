import urllib2
import simplejson
import socket



# def imageReturn(array):



# 	url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
#        'v=1.0&q=barack%20obama&userip=INSERT-USER-IP')

# 	request = urllib2.Request(url, None, {'Referer': /* Enter the URL of your site here */})
# 	response = urllib2.urlopen(request)


def query(array):
	query=""
	for i in xrange(len(array)-1):
		query+=array[i]+"%20"

	query+=array[len(array)-1]
	return query


print query(["a","b","c","d"])


def googlePrep(array):
	
	query=query(array)
	ip=socket.gethostbyname(socket.gethostname())

