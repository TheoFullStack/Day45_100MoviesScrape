import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# Connection to URL
response = requests.get(url=URL)
response.raise_for_status()

if response.status_code == 200:
    print("connection successful.")
else:
    print(f'connection error: {response.status_code}')

webpage = response.text

soup = BeautifulSoup(webpage,"html.parser")

titles = soup.find_all(name="h3",class_="title")

titles_text = []

for title in titles:
    text = title.getText()
    titles_text.append(text)


print(titles_text[::-1])

with open("movies.txt","w",encoding="utf-8") as file:
    for item in titles_text[::-1]:
        file.write(f'{item}\n')
file.close()


