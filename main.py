import requests, re
from bs4 import BeautifulSoup 
from googlesearch import search

# TODO Test on Separate System


def find(question):
    # going through the hits and appending them to list
    for hit in search(question, num=10, stop=1, pause=2):
        urls.append(hit)

    # going through the urls
    for i in urls:
        # test to see if the url is valid exits on a failure
        try:
            r = requests.get(i)
        except:
            continue

        soup = BeautifulSoup(r.content, 'html5lib')

        terms = soup.findAll('div', attrs={'class': '"TermText"'})
        answers = soup.findAll('a', attrs={'class': '"SetPageTerm-definitionText"'})

        for i in range(len(terms)):
            if terms[i] == question:
                return answers[i]

            if terms[i].replace("_", "").replace(" ", "").replace("?", "") == \
                    question.replace("_", "").replace(" ", "").replace("?", ""):
                return answers[i]

            if answers[i].replace("_", "").replace(" ", "").replace("?", "") == \
                    question.replace("_", "").replace(" ", "").replace("?", ""):
                return answers[i]
            
            if answers[i] == question:
                return terms[i]



if __name__ == "__main__":
    while True:
        # list of possible Urls
        urls = []

        # the question for the google search
        query = input("Enter your question")

        if query.lower() != "n":
            find(query)
        else:
            break
