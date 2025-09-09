// function display(result) {
//         console.log(result);
// }
// function add(num1, num2, mycallback) {
//         let sum = num1 + num2;
//         mycallback(sum)
// }
// add(40, 20, display)
// function greet(name, callback) {
//   console.log("Hello, " + name);
//   callback(); // calling the callback function
// }

// function sayGoodbye() {
//   console.log("Goodbye!");
// }


// greet("John", sayGoodbye);
function processUserInput(callback) {
  let name = "Alice";
  callback(name);
}

processUserInput(function(name) {
  console.log("Welcome, " + name);
});

