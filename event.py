import requests
from bs4 import BeautifulSoup
import pprint
import csv


"""for eventbrite.com"""


def get_title(html):
    """Scrape page title."""
    title = None
    if html.find("meta", property="og:title"):
        title = html.find("meta", property="og:title").get('content')
    return title
def get_description(html):
    description = None
    if html.find("meta", property="og:description"):
        description = html.find("meta", property="og:description").get('content')
    return description

def get_start_time(html):
    start_time=None
    if html.find("meta",property="event:start_time"):
        start_time=html.find("meta",property="event:start_time").get('content')
    return start_time

def get_end_time(html):
    end_time=None
    if html.find("meta",property="event:end_time"):
        end_time=html.find("meta",property="event:end_time").get('content')
    return end_time



headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}
u= 'https://www.eventbrite.com/d/online/events/'
reqs=requests.get(u,headers=headers)
soup=BeautifulSoup(reqs.content, 'html.parser')
urls=[item.get('href') for item in soup.find_all('a' ,class_="eds-event-card-content__action-link")]
urls_final=list(dict.fromkeys(urls))
urls_final = list(filter(None, urls_final)) 
print("for eventbrite.com ")
print("data for meta data\n")
for i in range(0,10):
    pp = pprint.PrettyPrinter(indent=4)
    r = requests.get(urls_final[i], headers=headers)
    html = BeautifulSoup(r.content, 'html.parser')
    metadata = {
        'title': get_title(html),
        'description': get_description(html),
        'start_time': get_start_time(html),
        'end_time':get_end_time(html),
        'url': urls_final[i]
        }
    title=metadata['title']
    description=metadata['description']
    start_time=metadata['start_time']
    end_time=metadata['end_time']
    url=metadata['url']
    pp.pprint(metadata)
    with open('data.csv', mode='a',newline='') as csv_file:
        data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data.writerow([title,description,start_time,end_time,url])