'''
In this assignment I'm serching for all the authors in all the pages 
Without knowing how much pages there are
'''
import bs4
import requests
#counter
page = 1
#a set for unique authors
authors = set()
#break condition - temp == []
while True :
    #requesting pages   
    res = requests.get(f'http://quotes.toscrape.com/page/{page}/')
    #converting pages to soups
    soup = bs4.BeautifulSoup(res.text,'lxml')
    #extracting relevant class
    temp = soup.select('.author')
    #adding the authors to the set
    if temp != []:
        for author in temp:
            authors.add(author.text)
    else:
        break
        
    page += 1
        
print(authors)