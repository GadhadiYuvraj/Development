const prompt = require("prompt-sync")();

let name = prompt("What is your name ?  ");

console.log("Hello", name, "Welcome to our game!");

const shouldWePlay = prompt("Do you want to play ? ");

if (shouldWePlay.toLowerCase() === "yes") {
  console.log("Okay then Let's Play! 😁");

  // Game Logic
  console.log("Now You Have Entered in a Maze,");
  console.log("Where Do you want to go ?");
  const leftOrRight = prompt(" Left ⬅️or Right➡️ ?");
  if (leftOrRight.toLowerCase() === "left") {
    console.log("Nice choice buddy");
    console.log("There are 2 doors in front of you  🚪🚪");
    const direction = prompt("Select any one Door-1 OR Door 2?:  ");
    if (direction == "1") {
      console.log(
        "you found out that is a fire 🔥 in this room and you saw another door (the only left which can be open ) so you just go out from there and game ends...",
      );
    } else if (direction == "2") {
      console.log(
        "You just dont want to continue this game so you left again ",
      );
    } else {
      console.log("invalid input. Get lost");
    }
  } else if (leftOrRight.toLowerCase() === "right") {
    console.log("Congratulations you have found the way out");
  }
} else if (shouldWePlay.toLowerCase() === "no") {
  console.log("okay no problem.. 🥲");
} else {
  console.log("Invalid input... 🤨\nTry again...😑 ");
}

/*Improved code by chatGPT */
// const prompt = require("prompt-sync")();

// let name = prompt("What is your name? ");
// console.log(`Hello ${name}, Welcome to the Maze Game! 🧩`);

// let health = 3;

// const shouldWePlay = prompt("Do you want to play? (yes/no): ").toLowerCase();

// if (shouldWePlay === "yes") {
//   console.log("\nYou entered a dark maze... 🌑");

//   while (health > 0) {
//     console.log(`\n❤️ Health: ${health}`);
//     const direction = prompt("Go Left ⬅️ or Right ➡️ ? ").toLowerCase();

//     if (direction === "left") {
//       console.log("\nYou see 2 doors 🚪🚪");
//       const door = prompt("Choose door 1 or 2: ");

//       if (door === "1") {
//         console.log("💥 Trap! You lost 1 health.");
//         health--;
//       } else if (door === "2") {
//         console.log("🎉 Safe path! You move forward.");

//         const chest = prompt(
//           "You found a chest! Open it? (yes/no): ",
//         ).toLowerCase();

//         if (chest === "yes") {
//           const outcome = Math.random();

//           if (outcome < 0.5) {
//             console.log("💎 You found treasure! You WIN!");
//             break;
//           } else {
//             console.log("☠️ Poison trap! You lose 2 health.");
//             health -= 2;
//           }
//         }
//       } else {
//         console.log("Invalid door. You hesitate and lose 1 health.");
//         health--;
//       }
//     } else if (direction === "right") {
//       console.log("\nA monster appears! 👹");
//       const action = prompt("Fight ⚔️ or Run 🏃 ? ").toLowerCase();

//       if (action === "fight") {
//         const fight = Math.random();

//         if (fight > 0.5) {
//           console.log("🔥 You defeated the monster!");
//         } else {
//           console.log("💀 You got hit! Lose 1 health.");
//           health--;
//         }
//       } else if (action === "run") {
//         console.log("😨 You escaped safely.");
//       } else {
//         console.log("Frozen in fear. You lose 1 health.");
//         health--;
//       }
//     } else {
//       console.log("You hit a wall 🤦‍♂️ Lose 1 health.");
//       health--;
//     }

//     if (health <= 0) {
//       console.log("\n💀 Game Over! You died in the maze.");
//     }
//   }
// } else if (shouldWePlay === "no") {
//   console.log("Okay... maybe next time 😅");
// } else {
//   console.log("Invalid input.");
// }
