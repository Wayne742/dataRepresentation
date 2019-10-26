# Wayne Reilly 26/10/2019.
# Exercise 3.2 from Lab 03.
# Test that I can read a file using carviewer.html. 
 
import requests
from bs4 import BeautifulSoup

with open("../carviewer.html") as fp:
	soup = BeautifulSoup(fp, 'html.parser')
print(soup.prettify())
