const prompt = require("prompt-sync")();

let name = prompt("What is your name ?  ");

console.log("Hello", name, "Welcome to our game!");

const shouldWePlay = prompt("Do you want to play ? ");

if (shouldWePlay.toLowerCase() == "yes") {
  console.log("Okay then Let's Play! 😁");

  // Game Logic
  console.log("Now You Have Entered in a Maze,");
  console.log("Where Do you want to go ?");
  const leftOrRight = prompt(" Left ⬅️or Right➡️ ?");
  // Left turn
  if (leftOrRight.toLowerCase() == "left") {
    console.log("You go let and see a bridge...");
    const cross = prompt("Do you want to cross a bridge?").toLowerCase();
    if (cross == "yes" || cross == "y") {
      console.log(
        "You cross but the bridge was weak and broke and you fell. you lost.",
      );
    } else if (cross.toLowerCase() == "no") {
      console.log(
        "you see another Road near the bridge and you pass from there",
      );
      console.log("and Some how you find a way out (A Hiddien Gate to wind)");
      console.log("Congratulationss");
    } else {
      console.log("Get Lost Your Out 😑");
    }
  } else if (leftOrRight.toLowerCase() == "right") {
    console.log("you chose to move right");
    console.log(
      "There are 2 doors now one will instantly make you winner and \nanother one will keep the game moving",
    );
    const choice = prompt("Door 1 or Door 2 : ");
    if (choice.toLowerCase() == "door 1" || choice.toLowerCase() == "1") {
      console.log("You found out there is a Demon in this room and you have 2");
      console.log(
        "again you have 2  options 1st Fight the Demon \n2nd You have to be his Slave for 2 years and still he might kill you.",
      );
      const demonRoom = prompt("Chose Fight or Slave : ");
      if (demonRoom.toLowerCase() == "fight") {
        console.log("You fought Bravely but died");
      } else if (demonRoom.toLowerCase() == "slave") {
        console.log(
          "You found out that Demon cannot go out from this room and once your Out He cannot ever catch you",
        );
        console.log("So you run away and Won the game");
        console.log("Congratulations 🎉🥳");
      } else {
        console.log("You have selected wrong input and your out of this Game");
      }
    } else if (
      choice.toLowerCase() == "door 2" ||
      choice.toLowerCase() == "2"
    ) {
      console.log("You leave this maze safely...");
      console.log("Congratulation!! 🥳🎉You won this game ");
    } else {
      console.log("Invalid input... Get Lost");
    }
  }
} else if (shouldWePlay.toLowerCase() == "no") {
  console.log("okay no problem.. 🥲");
} else {
  console.log("Invalid input... 🤨\nTry again...😑 ");
}

/*Improved code */
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
