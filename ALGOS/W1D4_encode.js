/* 
  Given in an alumni interview
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 

  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */
//                     i
// const str1 = "aaaabbcddd";
// const expected1 = "a4b2cd3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

// RIOT   Read Input Output Talk

// take 5-7 mins to write the pseudocode here:

// create the function and decide what params it needs and what it will return

// -------------------------------

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */

//* 1) declare & intialize varibales
// ? new_str = ""
// ? count = 1
//* 2) Loop through the string (start: i =0; stop: i < string length; Step: i ++)
//? On each iteration:
//?  IF the current char is equal to the next char
//!       increment the count

//?  ELSE
//? IF count equal to 1
//!   new_str += str[i]
//? ELSE
//! new_str += str[i] + count

// RESET th count to one
function encodeStr(str) {
	var new_str = "";
	var count = 1;

	for (var i = 0; i < str.length; i++) {
		if (str[i] === str[i + 1]) {
			count += 1;
		} else {
			if (count === 1) {
				new_str += str[i];
			} else {
				new_str += str[i] + count;
			}
			count = 1;
		}
	}
	if (new_str.length < str.length) {
		return new_str;
	} else {
		return str;
	}
}

const str1 = "aaaabbcddd";
const expected1 = "a4b2cd3";

// console.log(encodeStr(str1));
// console.log(encodeStr(str2));
// console.log(encodeStr(str3));
console.log(encodeStr("bc"));

// -----------------------------------------------------
// using frequency map
function strEncodeHashTable(str = "") {
	const charFreq = {};
	let encoded = "";

	for (const char of str) {
		if (charFreq[char]) {
			charFreq[char]++;
		} else {
			charFreq[char] = 1;
		}
	}

	// iterate back over str to get the proper order
	// order of keys on obj is not guaranteed to be in order
	for (const char of str) {
		if (charFreq[char] > 0) {
			encoded += char + charFreq[char];
			// Next time the same letter is looked up, it won't be added again.
			charFreq[char] = 0;
		}
	}
	return encoded.length < str.length ? encoded : str;
}
