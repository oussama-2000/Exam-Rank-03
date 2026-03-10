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