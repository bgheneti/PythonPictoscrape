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
        authority=parse(website, rule='IRI')['authority']
        #print tree

        if authority=='www.fanfiction.net':
                subject = tree.xpath('//span[@class="lc-left"]/*[3]/text()')
                storyOrig = tree.xpath('//div[@class="storytext xcontrast_txt nocopy"]/p/text()')
                author = tree.xpath('//div[@id="profile_top"]/*[5]/text()')
                #print author
                title = tree.xpath('//div[@id="profile_top"]/b/text()')
                story=[]
                summary=None

                for i in xrange(len(storyOrig)):
                        part=storyOrig[i].strip().encode('ascii', 'ignore')
                        if part!='' and part!='-':
                                story.append(part)

                if subject==[]:
                        return False
                subject = subject[0].strip().encode('ascii', 'ignore')
                author = author[0].strip().encode('ascii', 'ignore')
                title = title[0].strip().encode('ascii', 'ignore')

                story = " ".join(story)

                dictionary = {'fandom':subject,'title':title,'author':author,'summary':summary,'text':story}

                return dictionary

        if authority=='archiveofourown.org':
                subject = tree.xpath('//dd[@class="fandom tags"]/ul/*[1]/a[@class="tag"]/text()')
                if subject==[]:
                        page=requests.get(website+"?view_adult=true")
                        tree=html.fromstring(page.text)
                        subject = tree.xpath('//dd[@class="fandom tags"]/ul/*[1]/a[@class="tag"]/text()')
                #print subject
                summaryOrig = tree.xpath('//blockquote[@class="userstuff"]/p/text()')
                storyOrig = tree.xpath('//div[@role="article"]/p/text()')
                author = tree.xpath('//a[@class="login author"]/text()')
                title = tree.xpath('//h2[@class="title heading"]/text()')


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
                if subject==[]:
                        return False
                subject = subject[0].strip().encode('ascii', 'ignore')
                author = author[0].strip().encode('ascii', 'ignore')
                title = title[0].strip().encode('ascii', 'ignore')

                story = " ".join(story)
                summary = " ".join(summary)

                dictionary = {'fandom':subject,'title':title,'author':author,'summary':summary,'text':story}

                return dictionary

        else:
                return False


#takes website URL and scrapes fandom subject, summary and story from html to ascii
def scrape(website):

        # if webCheck(website)==False:
        #         print "website does not exist"
        #         return False
        try:
                return urlRead(website)
        except:
                return False

#takes website URL and returns text array of keywork, summary and story

# print scrape('http://archiveofourown.org/works/1145750/chapters/2320181')