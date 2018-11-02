from bs4 import BeautifulSoup
import requests
from requests import get
import csv
from googlesearch import search
import lxml

def googletest():
    query = "transparency"
    url = "https://google.com/search?q=" + query
    raw = get(url).text
    soup = BeautifulSoup(raw, 'html.parser')

   # print(soup.prettify())

    for chunk in soup.find_all('div', class_='g'):
        try:
            print(chunk.h3.text)
            print()
        except:
            print("No text attribute")

    #for j in search(query, tld="com", num=10, stop=1, pause=2):
     #   print(j)

def scrapecorey():
    source = requests.get('http://cnn.com').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('cms_scrape.csv', 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'video_link'])

    for article in soup.find_all('article'):
        headline = article.h2.a.text
        print(headline)

        summary = article.find('div', class_='entry-content').p.text
        print(summary)

        try:
            vid_src = article.find('iframe', class_='youtube-player')['src']

            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]

            yt_link = f'https://youtube.com/watch?v={vid_id}'
        except Exception as e:
            yt_link = None

            print(yt_link)

            print()

            csv_writer.writerow([headline, summary, yt_link])

        csv_file.close()

def pullLinks(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    body = soup.find('body')
#    print(body)

    for link in body.find_all('a'):
        print(link.get('href'))

def hello():
    print("Working on it...")

if __name__ == '__main__':
    hello()
 #   scrapecorey()
    googletest()
    #pullLinks("http://cnn.com")