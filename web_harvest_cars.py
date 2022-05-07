from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def main():

    # open the url to obtain the html
    page = None
    url = "https://www.amazon.sg/gp/bestsellers?ref_=nav_cs_bestsellers"

    books_list = []    # list of books

    try:
        page = urlopen(url)
        #print("Page connected properly.")

        soup = BeautifulSoup(page, 'html.parser')
        #print(soup)
        for element in soup.find_all('div', {"class" : "p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-2"}):
            books_list.append(element.text)   # save the data to books_list

        books_list.sort()

        for index, book in enumerate(books_list):   # index, title
           print(f"{index + 1}) {book}")   # printing a list


    except Exception as ex:
        print(ex)


main()