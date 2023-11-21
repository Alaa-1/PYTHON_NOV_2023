/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/
//            v
const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

// pseudocode here

// create the function and decide what params it needs and what it will return
// w/ freqTable
function stringDedupe(str) {
	var resultStr = "";
	var freqTable = {};

	// loop through the given array
	for (var i = 0; i <= str.length - 1; i++) {
		if (!freqTable[str[i]]) {
			resultStr += str[i];
			freqTable[str[i]] = true;
		}
	}
	return resultStr;
}

// without freq Table
function stringDedupe2(str) {
	var resultStr = "";
	for (var char of str) {
		if (resultStr.includes(char) === false) {
			resultStr += char;
		}
	}
	return resultStr;
}

// console.log(stringDedupe2(str2));

// BONUS

function stringDedupeBonus(str) {
	var freqTable = {};
	var resultStr = "";
	for (i = 0; i < str.length; i++) {
		if (freqTable.hasOwnProperty(str[i])) {
			delete freqTable[str[i]];
		}
		freqTable[str[i]] = i;
	}
	// console.log(freqTable);
	for (var key in freqTable) {
		resultStr += key;
	}
	return resultStr;
}

console.log(stringDedupeBonus("helolol"));

const stringDedupeWithSet = (str = "") => [...new Set(str)].join("");
