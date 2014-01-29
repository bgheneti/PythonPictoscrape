from urllib import urlopen
from rfc3987 import parse
from lxml import etree
from xml.etree.ElementTree import ElementTree



def userInput():

	website=raw_input("website?")

	try:
		print parse(website, rule='IRI')
		return website
	
	except:
		return False


def urlRead(website):
	websiteRead=urlopen(website).read()
	print websiteRead


	XHTML_NAMESPACE = website
	XHTML = "{%s}" % XHTML_NAMESPACE
	NSMAP = {None : XHTML_NAMESPACE} # the default namespace (no prefix)

	xhtml = etree.Element(XHTML + "html", nsmap=NSMAP) # lxml only!

	body.text = "Hello World"


	tree=etree.HTML(websiteRead)

	topic = tree.xpath( "//dd[@class='fandom tags']")

	wow.=etree



	print topic

def scrape():
	website=userInput()
	if website==False:
		print "website does not exist"
		scrape()
		return True
	urlRead(website)


urlRead("http://archiveofourown.org/works/1158492")