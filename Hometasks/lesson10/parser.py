from bs4 import BeautifulSoup
import requests


url = "https://en.wikipedia.org/wiki/Bottom-up_parsing"
page = requests.get(url)
#print(page.status_code)
filtered_content=[]
content = []
soup = BeautifulSoup(page.text, 'html.parser')
soup_ol = soup.ol.extract()



titles = soup.findAll('h1')
for title in titles:
    print(title.text)

content = soup.findAll('div', class_='mw-body-content')
print(type(content))


for data in content:
        if data.find("div") is not None:
            filtered_content.append((data.text))

for data in filtered_content:
    print(data)