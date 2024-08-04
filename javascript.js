
/* JavaScript:
forEach() with a callback: */

let arr = ["shower", "brush teeth", "mow lawn", "eat brains"];
arr.forEach((item, index) => console.log(`Index: ${index}, Item: ${item}`));

// Using Array.prototype.entries() 
for (const [index, item] of arr.entries()) {
    console.log(`Index: ${index}, Item: ${item}`);
}