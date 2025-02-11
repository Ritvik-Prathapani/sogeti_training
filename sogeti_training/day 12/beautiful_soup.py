from bs4 import BeautifulSoup as bs
import requests
def imdb(url):
    Headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    response=requests.get(url,headers=Headers)
    print(response)
    soup = bs(response.content,'html.parser')
    movies=soup.find_all('h3')
    movies=movies[1:6]
    for movie in movies:
        print(movie.get_text())
    # for title in movies:
    #     print(title)
url="https://www.imdb.com/chart/top/"
imdb(url)