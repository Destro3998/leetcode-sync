"""
Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an <span data-keyword="anagram">anagram</span> of <code>s</code>, and <code>false</code> otherwise.


 

<strong class="example">Example 1:</strong>


<div class="example-block">
<strong>Input:</strong> <span class="example-io">s = &quot;anagram&quot;, t = &quot;nagaram&quot;</span>


<strong>Output:</strong> <span class="example-io">true</span>

</div>

<strong class="example">Example 2:</strong>


<div class="example-block">
<strong>Input:</strong> <span class="example-io">s = &quot;rat&quot;, t = &quot;car&quot;</span>


<strong>Output:</strong> <span class="example-io">false</span>

</div>

 

<strong>Constraints:</strong>


<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

 

<strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        