// https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

//                               V
const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

// pseudocode here

// create the function and decide what params it needs and what it will return
function oddOccurenyArray(arr) {
	var freqTable = {};
	for (var elem of arr) {
		if (!freqTable.hasOwnProperty(elem)) {
			freqTable[elem] = 1;
		} else {
			freqTable[elem] += 1;
		}
	}
	for (var key in freqTable) {
		if (freqTable[key] % 2 !== 0) {
			return parseInt(key);
		}
	}
}
