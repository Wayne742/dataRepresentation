# Wayne Reilly 26/10/2019.
# Exercise 3.1 from Lab 03.
# Test that I can retrieve a web page.
 
import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print("--------------------")
print(page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
print("--------------------")
print(soup1.prettify())
