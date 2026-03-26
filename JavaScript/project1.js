const prompt = require("prompt-sync")()

let name = prompt("What is your name ?  ")

console.log("Hello", name, "Welcome to our game!");

const shouldWePlay = prompt('Do you want to play ? ')

// if(shouldWePlay == 'Y' || shouldWePlay == 'y')
//     console.log("Lets start then");
/* --------- OR --------- */ 
//  const condition = shouldWePlay == 'Y' || shouldWePlay == 'y'
//     console.log(condition);
    

const condition = shouldWePlay.toLowerCase() === "yes"
console.log(condition);

