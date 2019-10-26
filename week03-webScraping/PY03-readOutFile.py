# Wayne Reilly 26/10/2019.
# Exercise 3.3 from Lab 03.
# Extract the first tr from the file carviewer.html. 
# Through out this file I have used the hash symbol to "comment out" some lines of the script.
 
import requests
from bs4 import BeautifulSoup

with open("../carviewer.html") as fp:
	soup = BeautifulSoup(fp, 'html.parser')

#print(soup.tr)

rows = soup.findAll("tr")
for row in rows:
	#print("----------")
	#print(row)
	
	dataList = []
	
	cols = row.findAll("td")
	for col in cols:
	#	print(col.text)
		dataList.append(col.text)
	print(dataList)