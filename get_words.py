import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.verben.de/suche/substantive/"
levels = {
    11: "A1",
    12: "A2",
    21: "B1",
    22: "B2",
    31: "C1",
    32: "C2"
}

def get_words(url: str):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    words = soup.find_all("div", class_="bTrf rClear")
    return words

def get_word(word: BeautifulSoup) -> dict:
    try:
        base = word.find("div", class_="rAuf").div
        noun = base.find("u").string
        article = base.find("span", title=True).string
        word_data = {
            "word": noun,
            "article": article
        }
    except:
        word_data = None
    finally:
        return word_data

def scrape_and_save(url, keyword: str, level, word_dict: dict) -> dict:
    page_num = 1
    searching = True
    list_name = levels.get(level)
    word_dict.update({list_name:[]})

    while searching:
        current_page = url + "?w=" + keyword + "&l=" + level + "&p=" + page_num
        words = get_words(current_page)

        # iterate through the page
        for word in words:
            new_word = get_word(word)
            if new_word:
                if not str(new_word["word"]).startswith(keyword): # end of the list
                    searching = False
                    break
                # add word to the list
                word_dict[list_name].append(new_word)
        
        page_num+=1

# Main process

        

