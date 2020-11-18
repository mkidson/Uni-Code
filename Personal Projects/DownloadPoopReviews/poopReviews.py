from bs4 import BeautifulSoup as soup
import json

f=open(r'Personal Projects\DownloadPoopReviews\poopreviews.HTML', 'r')
pageHTML=f.read()
pageSoup=soup(pageHTML,'html.parser')

tags=pageSoup.findAll(href='/hashtag/milespoopreviews?src=hashtag_click')

for tag in tags:
    print(tag)
    print(pageSoup.fetchNextSiblings(tag))

print()