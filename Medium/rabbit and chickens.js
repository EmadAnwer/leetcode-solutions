//

// function getRabbitsAndChickens(l, h) {
//   let rabbits = Math.floor(l / 4);

//   let chickens = (l - rabbits * 4) / 2;

//   return { rabbits, chickens };
// }

// function getChickensAndRabbits(l, h) {
//   let rabbits = 0;
//   let chickens = 0;
//   while (l > 0) {
//     if (l - 4 >= 0) {
//       rabbits++;
//       l -= 4;
//     } else {
//       if (l - 2 < 0) {
//         break;
//       }
//       chickens++;
//       l -= 2;
//     }
//     h--;
//   }

//   return { rabbits, chickens };
// }

function getChickensAndRabbits(heads, leags) {
  let rabbits = 0;
  let chickens = 0;
  while (heads > 0) {
    // get number of chickens
    if (leags % 4 === 0 && heads - leags / 4 === 0)
      return { rabbits: leags / 4, chickens };
    chickens++;
    leags -= 2;
    heads--;
  }

  return { rabbits, chickens };
}
console.log(getChickensAndRabbits(35, 94));
