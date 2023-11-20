/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
*/
//                       v
const arr1 = ["a", "a", "a"];
const expected1 = {
	a: 3,
};

const arr2 = ["a", "b", "a", "c", "Bob", "c", "c", "d"];
const expected2 = {
	a: 2,
	b: 1,
	c: 3,
	Bob: 1,
	d: 1,
};

const arr3 = [];
const expected3 = {};

// pseudocode here
// *1) Create an empty object
//*2) Loop through the array
//? a) Check if the element at the specific index exists in the object
//! 		if doesn't exist -> Add it to the object as a key with value of 1
//*			if it exists -> increment the value
//* 3) Return the object
// create the function and decide what params it needs and what it will return
function makeFrequencyTable(arr) {
	var freqTable = {};
	for (var elem of arr) {
		if (!freqTable.hasOwnProperty(elem)) {
			freqTable[elem] = 1;
		} else {
			freqTable[elem] += 1;
		}
	}
	return freqTable;
}

// module.exports = makeFrequencyTable;
