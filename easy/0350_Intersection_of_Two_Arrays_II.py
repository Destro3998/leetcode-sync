"""
Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their intersection</em>. Each element in the result must appear as many times as it shows in both arrays and you may return the result in <strong>any order</strong>.


 

<strong class="example">Example 1:</strong>


<pre>
<strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2,2]
</pre>

<strong class="example">Example 2:</strong>


<pre>
<strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [4,9]
<strong>Explanation:</strong> [9,4] is also accepted.
</pre>

 

<strong>Constraints:</strong>


<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>

 

<strong>Follow up:</strong>


<ul>
	<li>What if the given array is already sorted? How would you optimize your algorithm?</li>
	<li>What if <code>nums1</code>&#39;s size is small compared to <code>nums2</code>&#39;s size? Which algorithm is better?</li>
	<li>What if elements of <code>nums2</code> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?</li>
</ul>

"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        