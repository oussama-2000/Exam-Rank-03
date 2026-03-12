<h1>is Anagram</h1>
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
<br>
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
<br>
<code>
Example 1:
<br>
Input: 
s = "racecar", t = "carrace"
<br>
Output: 
true
<br>
Example 2:
<br>
Input: 
s = "jar", t = "jam"
<br>
Output: 
false
<br>
</code>
Constraints:
<br>
<ul><li>s and t consist of lowercase English letters.</li></ul>

<br><br>

<h1>Two Sum</h1>
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
<br>
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
<br>
Return the answer with the smaller index first.
<br>
<code>
Example 1:
<br>
Input: 
nums = [3,4,5,6], target = 7
<br>
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
<br>
Example 2:
<br>
Input: nums = [4,5,6], target = 10
<br>
Output: [0,2]
<br>
Example 3:
<br>
Input: nums = [5,5], target = 10
<br>
Output: [0,1]
</code>
<br>
Constraints:
<br>
<ul>
<li>2 <= nums.length <= 1000</li>
<li>-10,000,000 <= nums[i] <= 10,000,000</li>
<li>-10,000,000 <= target <= 10,000,000</li>
<li>Only one valid answer exists.</li>
</ul>

<br><br>
<h1>Group Anagrams</h1>
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
<br>
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
<br>

<code>
Example 1:
<br>
Input: strs = ["act","pots","tops","cat","stop","hat"]
<br>
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
<br>
Example 2:
<br>
Input: strs = ["x"]
<br>
Output: [["x"]]
<br>
Example 3:
<br>
Input: strs = [""]
<br>
Output: [[""]]
</code>
<br>
Constraints:
<ul>
<li>1 <= strs.length <= 1000.</li>
<li>0 <= strs[i].length <= 100</li>
<li>strs[i] is made up of lowercase English letters.</li>
</ul>

<br><br>
<h1>Top K Frequent Elements</h1>
Given an integer array nums and an integer k, return the k most frequent elements within the array.
<br>
The test cases are generated such that the answer is always unique.
<br>
You may return the output in any order.

<code>
Example 1:
<br>
Input: nums = [1,2,2,3,3,3], k = 2
<br>
Output: [2,3]
<br>
Example 2:
<br>
Input: nums = [7,7], k = 1
<br>
Output: [7]
</code>

Constraints:
<ul>
<li>1 <= nums.length <= 10^4.</li>
<li>-1000 <= nums[i] <= 1000</li>
<li>1 <= k <= number of distinct elements in nums</li>
</ul>


<br><br>
<h1>Valid Palindrome</h1>
Given a string s, return true if it is a palindrome, otherwise return false.
<br>
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
<br>
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
<br>
<code>
Example 1:
<br>
Input: s = "Was it a car or a cat I saw?"
<br>
Output: true
<br>
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
<br>
Example 2:
<br>
Input: s = "tab a cat"
<br>
Output: false
<br>
Explanation: "tabacat" is not a palindrome.
<br>
</code>
<br>
Constraints:
<ul>
<li>1 <= s.length <= 1000</li>
<li>s is made up of only printable ASCII characters.</li>
</ul>

<br><br>
<h1>Custom Sorting</h1>
sort a list of strings primarily by their length, then by alphabetical order, then by number of vowels

