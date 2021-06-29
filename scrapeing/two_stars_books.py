'''
In this assignment I'm serching for the name of all two stars books
'''
#option one - run time : 35.40986119999798
def func_one(): 
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

#option two - faster and more readable, run time :34.78170209999999
def func_two():
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
    #creating a list of relevant book 
    two_star_books = []
    for i in range(50):
        for j in range(20):
            if product[i][j].select('.star-rating.Two') != []:
                two_star_books.append(product[i][j])
    #creating a list of relebant books names
    name_of_books = [] 
    for i in range(len(two_star_books)):
        name_of_books.append(two_star_books[i].select('a')[1]['title'])
    #printing books names
    for i in name_of_books:
        print(f'***{i}***')