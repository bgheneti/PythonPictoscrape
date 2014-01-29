from lxml import html
import requests
from rfc3987 import parse


def webCheck(website):

        try:
                print parse(website, rule='IRI')
                return True        
        except:
                return False
#checks if website URL exists

def urlRead(website):
        page = requests.get(website)
        tree=html.fromstring(page.text)
        print tree
        subject = tree.xpath('//dd[@class="fandom tags"]/ul/*[1]/a[@class="tag"]/text()')
        if subject==[]:
        	page=requests.get(website+"?view_adult=true")
        	tree=html.fromstring(page.text)
        	subject = tree.xpath('//dd[@class="fandom tags"]/ul/*[1]/a[@class="tag"]/text()')

        print subject
        summaryOrig = tree.xpath('//blockquote[@class="userstuff"]/p/text()')
        storyOrig = tree.xpath('//div[@role="article"]/p/text()')
        story=[]
        summary=[]
        for i in xrange(len(storyOrig)):
                part=storyOrig[i].strip().encode('ascii', 'ignore')
                if part!='' and part!='-':
                        story.append(part)
        for i in xrange(len(summaryOrig)):
                part=summaryOrig[i].strip().encode('ascii', 'ignore')
                if part!='' and part!='-':
                        summary.append(part)
        subject = subject[0]
        story = " ".join(story)
        summary = " ".join(summary)
        return [subject,summary,story]

#takes website URL and scrapes fandom subject, summary and story from html to ascii
def scrape(website):

        if webCheck(website)==False:
                print "website does not exist"
                return False
        return urlRead(website)

#takes website URL and returns text array of keywork, summary and story

print scrape('http://archiveofourown.org/works/1113812')