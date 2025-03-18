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
        showNotification("Richtig!")
    } else {
        showNotification("Falsch!")
    }
    newWord(level)
}

function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    if (message == "Richtig!") {
        notification.classList.add('correct');
    } else {
        notification.classList.add('incorrect');
    }
    notification.innerText = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.classList.add('fade-out');
        notification.addEventListener('transitionend', () => {
            notification.remove();
        });
    }, 1000); // Display for 1 second before fading out
}