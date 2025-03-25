'''Stealing words to make my own dictionary, the data will be saved as a json file'''
import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.verben.de/suche/substantive/"
levels = {
    "A1": 11,
    "A2": 12,
    "B1": 21,
    "B2": 22,
    "C1": 31,
    "C2": 32
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def get_words(url: str):
    soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    words = soup.find_all("div", class_="bTrf rClear")
    return words

def get_word(word: BeautifulSoup) -> dict:
    replacements = {
        "a3": "ä",
        "A3": "Ä",
        "o3": "ö",
        "O3": "Ö",
        "u3": "ü",
        "U3": "Ü",
        "s5": "ß",
        "e1": "é"
    }
    try:
        base = word.find("div", class_="rAuf")
        noun = base["id"].split(":")[1]
        
        # change special characters
        for key, value in replacements.items():
            noun = noun.replace(key, value)
        
        article = base.div.find("span", title=True).string
        word_data = {
            "word": noun,
            "article": article
        }
    except:
        word_data = None
    finally:
        return word_data

def scrape_and_save(url: str, keyword: str, level: str, word_dict: dict):
    page_num = 1
    searching = True

    if not level in word_dict:
        word_dict.update({level:{}}) # make a new list
    if not keyword.capitalize() in word_dict[level]:
        word_dict[level].update({keyword.capitalize():[]})

    while searching:
        current_page = url + "?w=" + keyword + "&l=" + str(levels.get(level)) + "&p=" + str(page_num)
        words = get_words(current_page)
        # iterate through the page
        for word in words:
            new_word = get_word(word)
            print(new_word)
            if new_word:
                if not str(new_word["word"]).startswith(keyword): # end of the list
                    searching = False
                    break
                # add word to the list
                word_dict[level][keyword.capitalize()].append(new_word)
        
        page_num+=1

# Main process
dictionary = {}
with open("words.json", "r") as openfile:
    dictionary = json.load(openfile)
'''
Note: already scraped data include 
"A" for "A1" "A2" "B1" "B2" "C1"
"B" for "A1" "A2" "B1" "B2" "C1"
"C" for "A1" "A2" "B1" "B2" "C1"
"D" for "A1" "A2" "B1" "B2" "C1"
"E" for "A1" "A2" "B1" "B2" "C1"
"F" for "A1" "A2" "B1" "B2" "C1"
"G" for "A1" "A2" "B1" "B2" "C1"
"H" for "A1" "A2" "B1" "B2" "C1"
"I" for "A1" "A2" "B1" "B2" "C1"
"J" for "A1" "A2" "B1" "B2" "C1"
"K" for "A1" "A2" "B1" "B2" "C1"
"L" for "A1" "A2" "B1" "B2" "C1"
"M" for "A1" "A2" "B1" "B2" "C1"
"N" for "A1" "A2" "B1" "B2" "C1"
"O" for "A1" "A2" "B1" "B2" "C1"
[Do not scrape too often as the website might block this IP]
'''

scrape_and_save(URL, "O", "C1", dictionary)

data = json.dumps(dictionary, indent=4)

with open("words.json", "w") as outfile:
    outfile.write(data)

