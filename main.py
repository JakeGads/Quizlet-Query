import requests, re
from bs4 import BeautifulSoup
from googlesearch import search


# May error out on mac's

# https://repl.it/@DevinShende/Quizlet-Scraper

def find(question):
    # going through the urls
    for url in list(search(question, num=35, stop=1, pause=2)):
        # A test to see if it is a quizlet link
        if "quizlet" not in url:
            print("This link is not a quizlet link")
            continue
        else:
            print("Testing quizlet Link")

        # test the link to see if its valid
        try:
            r = requests.get(url)
        except:
            print("Request Failed")
            continue

        # https://quizlet.com/462418579/security6-7quizes-flash-cards/?x=1qqt
        # Aditya is attempting to classify information regarding a new project that his organization will undertake in
        # secret. Which characteristic is NOT normally used to make these type of classification decisions?

        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")

        data = []  # data will be a list containing many dicts with term and definition keys
        content = soup.select("div.SetPage-terms")[0]
        pairs = content.select("div.SetPageTerm-content")
        for pair in pairs:
            term = pair.select("span.TermText")[0].get_text()
            defn = pair.select("span.TermText")[1].get_text()
            data.append({
                "term": term,
                "definition": defn
            })

        for key, value in data:
            
        return data


if __name__ == "__main__":
    while True:
        # list of possible Urls
        urls = []

        # the question for the google search
        query = input("Enter your question\nn forces an exit\t")

        if query.lower() != "n":
            print(find(query))
        else:
            break
