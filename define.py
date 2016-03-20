import requests
from bs4 import BeautifulSoup

wordFile = open('words.txt', 'r') 
name = raw_input('Enter name of text file: ')+'.txt'
output = open(name,'a')


for word in wordFile:	#Iterate over each word
	word = word.strip()

	r = requests.get("http://mnemonicdictionary.com/word/" + str(word))
	data = r.text
	soup = BeautifulSoup(data, "lxml")
	mnem = str(soup.find_all("div", class_="span9")[0].text)
	mnem = mnem.strip()
	output.write(word + ": " + str(mnem) +"\n\n")



 