setTimeout(
        function () {
                console.log("hello, Michel");
        }, 8000);

setTimeout(function(){
        console.log("learning javascript");
}, 2000);
setTimeout(function () {
        console.log("ritajosephine");
}, 1000);

setTimeout(() => {
        console.log("arrow function")
}, 6000);
//output:
// ritajosephine
// sett.js:10
// learning javascript
// sett.js:7
// arrow function
// sett.js:14
// hello, Michel
setTimeout(() => {
        console.log("runnining fast")
}, 500);
