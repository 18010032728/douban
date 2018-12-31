import requests
from bs4 import BeautifulSoup

def parseMovieUrl(url,offset=0):
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
    mUrl=url.format(offset)
    print(mUrl)
    response=requests.get(mUrl,headers=headers)
    response.encoding="utf-8"
    #print(response.text)
    json=response.json()
    for items in json['subjects']:
         movie_title=items['title']
         movie_url=items['url']
         #print(movie_title+"\t"+movie_url)
         parseMovie(movie_title,movie_url)
    offset+=20
    parseMovieUrl(url,offset)
def parseMovie(title,url):
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'lxml')
    types=soup.find_all('span',property="v:genre")
    typelist=[]
    for type in types:
        typelist.append(type.get_text())
    type=','.join(typelist)    
    with open('douban_movie.csv',"a")as file:
        file.write(title+","+type+","+url+"\n")
        file.close()

if __name__=="__main__":
    url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}"
    parseMovieUrl(url)
    #url="https://movie.douban.com/subject/27019570/"
    #title="test"
    #parseMovie(title,url)