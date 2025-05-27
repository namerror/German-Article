# some extra processing or testing of the word list.
# WARNING: make sure to read the code before running as it might make unintended changes to the json file!
# ONLY run make_changes() to make certain changes to the dictionary!!!
import json
from typing import Callable

def count_words(obj: dict): 
    wc = 0
    for key in obj:
        for letter in obj[key]:
            wc+=len(obj[key][letter])
            print("Now counting:" + key + " - " + letter + " - " + str(wc))

    print("Total word count: " + str(wc))

def replace_special_char(obj):
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
    count = 0
    for level in obj.values():
        for letter in level.values():
            for word in letter:
                for key, value in replacements.items():
                    word["word"] = word["word"].replace(key, value)
                print(word)
                count += 1

    print(count)

def make_changes(file, func: Callable[[dict], None]):
    # load data
    with open(file, "r") as f:
        obj = json.load(f)

    # function: changes to be made
    func(obj)

    # save data to file
    with open(file, "w") as f:
        f.write(json.dumps(obj, indent=4))

def read_only(file, func: Callable[[dict], None]):
    with open(file, "r") as f:
        obj = json.load(f)

    func(obj)

# delete empty lists from the dictionary
def delete_empty_lists(obj):
    for level in obj.values():
        for letter,l in level.copy().items():
            # if the list is empty, delete it
            if not l:
                del level[letter]

# ONLY RUN WHEN NECESSARY
make_changes("words.json", delete_empty_lists)