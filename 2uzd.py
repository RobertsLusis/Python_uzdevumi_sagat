"""
Iegūt ziņas, izmantojot rss no google.lv.

"""

import feedparser
#jānorāda RSS plūsmas URL
rss_url="https://news.google.com/rss?hl=en-LV&gl=LV&ceid=LV:lv'"

#lejupielādēt un izanalizēt RSS plūsmu
feed=feedparser.parse(rss_url)

#parādīt ziņu virsrakstus un saites
for entry in feed.entries:
    print("Virsraksts", entry.title)
    print("Saite", entry.link)
    print("\n")