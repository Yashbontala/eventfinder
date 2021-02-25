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

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}
u='https://www.naadyogacouncil.com/en/events/'
reqs=requests.get(u,headers=headers)
soup=BeautifulSoup(reqs.content, 'html.parser')
urls=[item.get('href') for item in soup.find_all('a' ,class_="url")]
urls_final=list(dict.fromkeys(urls))
print("for naadyogacouncil.com")
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
