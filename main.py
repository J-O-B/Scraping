import requests
from bs4 import BeautifulSoup
import urllib
import os

base_url = "https://www.latestpilotjobs.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def extract(page):
    url = f"https://www.latestpilotjobs.com/jobs/category/id/pilot_jobs/Jobs_page/{page}.html"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup):
    divs = soup.find_all('div', class_='aviation-jobs-content-first')
    for item in divs:
        try:
            title_contain = item.find('div', class_='row job-title-style')
            title_text = title_contain.find('a').text.strip()
            url = base_url + title_contain.find('a')['href']
            summary = item.find('div', class_='row job-description').text.strip()
            info = item.find('div', class_="col-lg-13")
            company = info.find('span').text.strip()
            location = info.find('span').next_sibling.next_sibling.text
            location = location[1:-1]
            date = item.find('div', class_="job-renew-date-size").text
            image = base_url + item.find('img', class_="company-logo-style")['src']
            urllib.request.urlretrieve(image, f"{image}")
            print(image)
        except:
            pass
    return

c = extract(1)

transform(c)