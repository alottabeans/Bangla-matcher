from lxml import etree, html
import requests
import json

class Scrape:  
  def __init__(self, URL):
    self.URL = URL
    self.URL = input('Enter URL: ')

    r = requests.get(URL)

    self.tree = html.fromstring(r.text)
    self.tree = etree.ElementTree(self.tree)

  def dump_words(self): 
    #translated words
    tw = self.tree.xpath('//div[@class="entry-content"]//td[3]//text()')

    #foreign words
    fw = self.tree.xpath('//div[@class="entry-content"]//td[2]//text()')

    #pack words into dict
    dictionary = dict(zip(tw, fw))

    #store words into a json 
    with open('scraped_words/wordz.json', 'w') as f:
      data = json.dump(dictionary, f)
