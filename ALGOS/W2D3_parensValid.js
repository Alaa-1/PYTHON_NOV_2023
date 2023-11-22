/* 
Parens Valid

Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValidCount(str) {
	var countParenth = 0;
	for (var char of str) {
		if (char === "(") {
			countParenth++;
		} else if (char === ")") {
			if (countParenth === 0) {
				return false;
			} else countParenth--;
		}
	}
	return countParenth === 0;
}
/*****************************************************************************/
function parensValid(str) {
	var parensStack = [];

	for (char of str) {
		if (char === "(") {
			parensStack.push(char);
		} else if (char === ")") {
			if (parensStack.length === 0) {
				return false;
			} else {
				parensStack.pop();
			}
		}
	}
	return parensStack.length === 0;
}

console.log(parensValidCount(str1));
console.log(parensValidCount(str2));
console.log(parensValidCount(str3));
console.log(parensValidCount(str4));

