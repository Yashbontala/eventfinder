import requests
from bs4 import BeautifulSoup
import extruct
from w3lib.html import get_base_url
import csv

def get_metadata(url):
    """Fetch JSON-LD structured data."""
    reqs = requests.get(url)
    html = reqs.text
    metadata = extruct.extract(
        html,
        base_url=get_base_url(url),
        syntaxes=['json-ld'],
        uniform=True
    )['json-ld']
    if bool(metadata) and isinstance(metadata, list):
        metadata = metadata[0]

    return metadata
    


u="https://insider.in/online"
reqs = requests.get(u)
soup = BeautifulSoup(reqs.content, 'html.parser')
base_Url='https://insider.in'
atags=[item.find('a') for item in soup.find_all('div', class_="event-card")]
urls=[base_Url+item.get('href') for item in atags]
urls_final = list(dict.fromkeys(urls))
print("for insider.com")
print("JSON_ld data\n")
for i in range(0, 10):
    metadata=get_metadata(urls_final[i])
    title=metadata['name']
    description=metadata['description']
    start_time=metadata['startDate']
    end_time=metadata['endDate']
    url=urls_final[i]
    print(metadata)
    with open('data.csv', mode='a',newline='') as csv_file:
        data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data.writerow([title,description,start_time,end_time,url])
