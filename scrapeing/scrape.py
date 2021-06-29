import requests
import bs4

res = []
for i in range(1,51):
    res.append(requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html'))

soup = []
for i in range(50):
    soup.append(bs4.BeautifulSoup(res[i].text,'lxml'))

product = []
for i in range(50):
    product.append(soup[i].select(".product_pod"))

books = []
for i in range(50):
    for j in range(20):
        books.append(product[i][j])

two_star_books = []
for i in range(1000):
    if books[i].select('.star-rating.Two') != []:
        two_star_books.append(books[i])

name_of_books = [] 
for i in range(len(two_star_books)):
    name_of_books.append(two_star_books[i].select('a')[1]['title'])

for i in name_of_books:
	print('***'+i+'***')