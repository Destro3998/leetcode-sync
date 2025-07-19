"""
Given a string <code>s</code>, reverse only all the vowels in the string and return it.


The vowels are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>, and they can appear in both lower and upper cases, more than once.


 

<strong class="example">Example 1:</strong>


<div class="example-block">
<strong>Input:</strong> <span class="example-io">s = &quot;IceCreAm&quot;</span>


<strong>Output:</strong> <span class="example-io">&quot;AceCreIm&quot;</span>


<strong>Explanation:</strong>


The vowels in <code>s</code> are <code>[&#39;I&#39;, &#39;e&#39;, &#39;e&#39;, &#39;A&#39;]</code>. On reversing the vowels, s becomes <code>&quot;AceCreIm&quot;</code>.

</div>

<strong class="example">Example 2:</strong>


<div class="example-block">
<strong>Input:</strong> <span class="example-io">s = &quot;leetcode&quot;</span>


<strong>Output:</strong> <span class="example-io">&quot;leotcede&quot;</span>

</div>

 

<strong>Constraints:</strong>


<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consist of <strong>printable ASCII</strong> characters.</li>
</ul>

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        