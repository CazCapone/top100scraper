import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")

titles = soup.find_all(name="h3", class_="title")
movie_list = [title.getText() for title in titles[::-1]]

print(movie_list)
with open("top_100_movie_list.txt", "w", encoding="utf8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
