let level = "A1"
let currentWord = {
    "word": "Nahrungsmittelunversträglichkeit",
    "article": "die"
}
let score = 0;
let highestScore = localStorage.getItem("highestScore") || 0; // Retrieve highest score from localStorage

window.onload = function () {
    loadHighestScore();
    function loadHighestScore() {
        document.getElementById("highest-score").innerHTML = highestScore;
    }
}

function setLevel(newLevel) {
    level = newLevel;
    // console.log(level);
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
        score++;
        if (score > highestScore) {
            highestScore = score;
            document.getElementById("highest-score").innerHTML = highestScore;
            localStorage.setItem("highestScore", highestScore); // Save the new highest score to localStorage
        }
    } else {
        showNotification("Falsch!")
        score = 0;
    }
    document.getElementById("score").innerHTML = score;
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

document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.level-buttons button');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove the 'pressed' class from all buttons
            buttons.forEach(btn => btn.classList.remove('pressed'));
            // Add the 'pressed' class to the clicked button
            button.classList.add('pressed');
        });
    });
});