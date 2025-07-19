"""
Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.


An input string is valid if:


<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
	<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

 

<strong class="example">Example 1:</strong>


<div class="example-block">
<strong>Input:</strong> <span class="example-io">s = &quot;()&quot;</span>


<strong>Output:</strong> <span class="example-io">true</span>

</div>

<strong class="example">Example 2:</strong>


<div class="example-block">
<strong>Input:</strong> <span class="example-io">s = &quot;()[]{}&quot;</span>


<strong>Output:</strong> <span class="example-io">true</span>

</div>

<strong class="example">Example 3:</strong>


<div class="example-block">
<strong>Input:</strong> <span class="example-io">s = &quot;(]&quot;</span>


<strong>Output:</strong> <span class="example-io">false</span>

</div>

<strong class="example">Example 4:</strong>


<div class="example-block">
<strong>Input:</strong> <span class="example-io">s = &quot;([])&quot;</span>


<strong>Output:</strong> <span class="example-io">true</span>

</div>

<strong class="example">Example 5:</strong>


<div class="example-block">
<strong>Input:</strong> <span class="example-io">s = &quot;([)]&quot;</span>


<strong>Output:</strong> <span class="example-io">false</span>

</div>

 

<strong>Constraints:</strong>


<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>

"""

class Solution:
    def isValid(self, s: str) -> bool:
        