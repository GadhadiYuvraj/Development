const prompt = require("prompt-sync")()

let name = prompt("What is your name ?  ")

console.log("Hello", name, "Welcome to our game!");

const shouldWePlay = prompt('Do you want to play ? ')

if(shouldWePlay == 'Y')
    console.log("Lets start then");
    


