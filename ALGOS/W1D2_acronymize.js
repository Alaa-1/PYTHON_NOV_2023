/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const strA = "object oriented programming";
const expectedA = "OOP";

// The 4 pillars of OOP
const strB = "abstraction polymorphism inheritance encapsulation";
const expectedB = "APIE";

const strC = "software development life cycle";
const expectedC = "SDLC";

// Bonus: ignore extra spaces
const strD = "  global   information tracker    ";
const expectedD = "GIT";

// take 5-8 mins to write the pseudocode here:

// create the function and decide what params it needs and what it will return

// using split()
function acronymize(str) {
	var acronym = "";
	var wordsArr = str.split(" ");
	// console.log(wordsArr);

	for (var word of wordsArr) {
		if (word) {
			acronym += word[0].toUpperCase();
		}
	}
	return acronym;
}

// console.log(acronymize(strD));
// console.log(acronymize(strB));
// console.log(acronymize(strC));

// without split()

function acronymize2(str) {
	var acro = "";

	for (var i = 0; i < str.length; i++) {
		// console.log(str[i]);
		// var currentChar = str[i];
		// var isCurrentCharSpace = currentChar === " ";
		// var isPreviousCharSpace = str[i - 1] === " ";
		var isFirstLetter =
			(i === 0 && str[0] !== " ") || (str[i - 1] === " " && str[i] !== " ");

		if (isFirstLetter === true) {
			acro += str[i].toUpperCase();
		}
	}
	return acro;
}

console.log(acronymize2(strD));
