from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
a = soup.find_all(name="a", class_="storylink")
upvotes = [int(i.getText().split()[0]) for i in soup.find_all(name="span", class_="score")]
article_text = []
article_link = []

for a_tag in a:
    article_text.append(a_tag.getText())
    article_link.append(a_tag.get("href"))

max_upvotes = max(upvotes)
index = upvotes.index(max_upvotes)

print(upvotes)
print(article_text[index], article_link[index], upvotes[index], f"Index: {index}")