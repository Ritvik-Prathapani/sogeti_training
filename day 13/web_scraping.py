import requests
from bs4 import BeautifulSoup as bs
Headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
url = "https://www.cdn.geeksforgeeks.org/data-structures/"
responce = requests.get(url,headers=Headers)
soup = bs(responce.content,'html.parser')
print(soup.prettify())