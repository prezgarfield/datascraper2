from bs4 import BeautifulSoup
import requests
from requests import get
import csv
import urllib
import urllib.parse
from urllib.request import urlopen
from googlesearch import search
import lxml


def requesttest(url):
    try:
        html = urlopen(url)
    except:
        print("URL not found")
    try:
        soup = BeautifulSoup(html.read(), 'lxml')
        page = soup
    except AttributeError as e:
        return None
    # return soup.prettify()
    nameList = soup.find_all("span", {"class":"green"})
    for name in nameList:
        print(name.get_text())

def googletest():
    query = "transparency"
    url = "https://google.com/search?q=" + query
    raw = get(url).text
    soup = BeautifulSoup(raw, 'html.parser')

   # print(soup.prettify())
    test = soup.find('div', class_='g')
    #newtest = BeautifulSoup(test.read(), 'html.parser')
    print(test)

    for chunk in soup.find_all('div', class_='g'):
        try:
            print(chunk.h3.text)
            soup.select_one("h3.r a".get('href'))
            print()
        except:
            print("No text attribute")

def makenodes(node, links, csvfile):

    return None

def makeedges(urls, csvfile):
    return None

def cleanURLs(urls):
    newlist = []

    for link in urls:
        newurl = link.split('/')
        newurl = ''.join(newurl[0] + "//" + newurl[2])
        newlist.append(newurl)
        # print(newurl)
    newlist = list(set(newlist))
    return newlist

def bruteforce(query):
    urls = []
    for j in search(query, tld="com", num=50, stop=1, pause=2):
       urls.append(j)

    print("list initial contents:")

    urls = list(set(urls))
    cleaned = cleanURLs(urls)

    csv_edges = open('edges.csv', 'a', newline='')
    csv_writer_edge = csv.writer(csv_edges)

    for i in cleaned:
        csv_writer_edge.writerow([query, i])

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
 #    googletest()
    #pullLinks("http://cnn.com")
    # print(requesttest("http://bit.ly/1Ge96Rw"))
    csv_nodes = open('nodes.csv', 'w', newline='')
    csv_writer_node = csv.writer(csv_nodes)
    csv_writer_node.writerow(['ID'])
    csv_nodes.close()
    csv_nodes = open('nodes.csv', 'a', newline='')
    csv_writer_node = csv.writer(csv_nodes)

    csv_edges = open('edges.csv', 'w', newline='')
    csv_writer_edge = csv.writer(csv_edges)
    csv_writer_edge.writerow(['Source', 'Target'])
    csv_edges.close()

    query = None
    while 1:
        query = input("enter a keyword to search")
        if query == 'q':
            break
        csv_writer_node.writerow([query])
        bruteforce(query)
