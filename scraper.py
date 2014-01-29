from lxml import html
import requests
from rfc3987 import parse


def webCheck(website):

	try:
		print parse(website, rule='IRI')
		return True	
	except:
		return False


def urlRead(website):
	page = requests.get(website)
	tree=html.fromstring(page.text)
	subject = tree.xpath('//dd[@class="fandom tags"]/ul/*[1]/a[@class="tag"]/text()')
	summary = tree.xpath('//blockquote[@class="userstuff"]/p/text()')
	storyOrig = tree.xpath('//div[@class="userstuff"]/p/text()')
	story=[]
	for i in xrange(len(storyOrig)):
		part=storyOrig[i].strip().encode('ascii', 'ignore')
		if part!='' and part!='-':
			story.append(part)
	story = " ".join(story);
	return [subject,summary,story]

def scrape(website):

	if webCheck(website)==False:
		print "website does not exist"
		return False
	return urlRead(website)


print scrape('http://archiveofourown.org/works/1158492')
