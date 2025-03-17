let level = "A1"
let currentWord = {
    "word": "Nahrungsmittelunversträglichkeit",
    "article": "die"
}

function setLevel(newLevel) {
    level = newLevel;
    console.log(level);
    newWord(level);
}

// new word after button press
function newWord(level) {
    // read words from words.json
    fetch('words.json')
        .then(response => response.json())
        .then(data => {
            // get a word from the specified level
            let words = data[level];
            let firstLetters = Object.keys(words)
            // get a random first letter of the word (which is a list)
            let firstLetter = firstLetters[Math.floor(Math.random() * firstLetters.length)];
            // get a random word from the list
            let word = words[firstLetter][Math.floor(Math.random() * words[firstLetter].length)];
            currentWord = word;
            // display the word
            document.getElementById("word").innerHTML = word["word"];
        });
}

function checkAnswer(article) {
    if (currentWord["article"] == article) {
        console.log("Correct!")
    } else {
        console.log("Incorrect!")
    }
    newWord(level)
}