'''
In this assignment I'm serching for the name of all two stars books
'''
import requests
import bs4
#requesting pages
res = []
for i in range(1,51):
    res.append(requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html'))
#converting pages to soups  
soup = []
for i in range(50):
    soup.append(bs4.BeautifulSoup(res[i].text,'lxml'))
#extracting relevant class - for each product(book)
product = []
for i in range(50):
    product.append(soup[i].select(".product_pod"))
#creating a books list - not necessary but more convenient
books = []
for i in range(50):
    for j in range(20):
        books.append(product[i][j])
#creating a list of two stars books
two_star_books = []
for i in range(1000):
    if books[i].select('.star-rating.Two') != []:
        two_star_books.append(books[i])
#creating a list of two stars books name
name_of_books = [] 
for i in range(len(two_star_books)):
    name_of_books.append(two_star_books[i].select('a')[1]['title'])
#printing the books name
for i in name_of_books:
	print('***'+i+'***')