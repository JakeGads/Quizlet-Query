import requests, re
from bs4 import BeautifulSoup 
from googlesearch import search

# TODO Test on Separate System


def find(question):
    # going through the urls
    for url in search(question, num=10, stop=1, pause=2):
        # A test to see if it is a quizlet link
        if "quizlet" not in url:
            print("This link is not a quizlet link")
            continue

        # test the link to see if its valid
        try:
            r = requests.get(url)
        except:
            continue

        # running soup saves the html locally for analysis
        soup = BeautifulSoup(r.content, 'html5lib')

        # getting my list of terms and my list of answers
        all_terms = soup.findAll('div', attrs={'class': '"TermText"'})
        split_term = []
        for i in range(0, len(all_terms), 2):
            try:
                temp = all_terms[i], all_terms[i+1]
                split_term.append(temp)
            except:
                break

        for combination in split_term:
            if question == combination[0]:
                return combination[1]
            if question == combination[1]:
                return combination[0]

            if question.replace(" ", "").replace("_", "").replace("?", "") == \
                    combination[0].replace(" ", "").replace("_", "").replace("?", ""):
                return combination[1]
            if question.replace(" ", "").replace("_", "").replace("?", "") == \
                    combination[1].replace(" ", "").replace("_", "").replace("?", ""):
                return combination[0]


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
