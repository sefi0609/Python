'''
In this assignment I'm serching for the name of all two stars books
'''
import requests
import bs4
#empty list for the relevant books
two_star_books = []

for i in range(1,51):
    #requesting pages
    res = requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html')
    #converting pages to soups
    soup = bs4.BeautifulSoup(res.text,'lxml')
    #extracting relevant class - for each product(book)
    product = soup.select(".product_pod")
    #adding the relevant book names
    for j in range(20):
        #checking for two star books
        if product[j].select('.star-rating.Two') != []:
            #adding the relevan books name to the list
            two_star_books.append(product[j].select('a')[1]['title'])
#printing the books names
for i in two_star_books:
    print(f'***{i}***')