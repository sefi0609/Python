'''
In this script I'm sending myself the books list from http://books.toscrape.com/
You can change to whom you wanna send it to
'''

import smtplib
import bs4
import requests
import getpass
#function to get the books list
def func_two():

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
    #creating a string of all two star books    
    string =''
    for book in name_of_books:
        string += f'\n{book}'
    return string
        
books = func_two()
#creating STMP object to work with
obj = smtplib.SMTP('smtp.gmail.com',587)
#establishes the connection
obj.ehlo()
#initiate TLS encryption
obj.starttls()
#get the user email
email = getpass.getpass("Enter your email: ")
#get the user password - apps password not regular password for gmail
password = getpass.getpass("Enter your password: ")
#login to this gmail
obj.login(email,password)

from_address = email
to_address = email
subject = 'Scraping'
message = books
#the actual message
msg = "Subject: "+subject+'\n'+message
#sending the email
obj.sendmail(from_address,to_address,msg)
#closing connection
obj.quit()