const prompt = require("prompt-sync")();
let number = number(prompt("enter a number:")
if(number =! number);
console.log("not a valid number");
else
{
console.log("enter a valid number")
for (let count = 1; count <= 12; count++){
console.log(number + "X" + count + " = " + (number * count));
}
}
