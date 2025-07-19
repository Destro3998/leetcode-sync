"""
Given an input string <code>s</code>, reverse the order of the <strong>words</strong>.


A <strong>word</strong> is defined as a sequence of non-space characters. The <strong>words</strong> in <code>s</code> will be separated by at least one space.


Return <em>a string of the words in reverse order concatenated by a single space.</em>


<b>Note</b> that <code>s</code> may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


 

<strong class="example">Example 1:</strong>


<pre>
<strong>Input:</strong> s = &quot;the sky is blue&quot;
<strong>Output:</strong> &quot;blue is sky the&quot;
</pre>

<strong class="example">Example 2:</strong>


<pre>
<strong>Input:</strong> s = &quot;  hello world  &quot;
<strong>Output:</strong> &quot;world hello&quot;
<strong>Explanation:</strong> Your reversed string should not contain leading or trailing spaces.
</pre>

<strong class="example">Example 3:</strong>


<pre>
<strong>Input:</strong> s = &quot;a good   example&quot;
<strong>Output:</strong> &quot;example good a&quot;
<strong>Explanation:</strong> You need to reduce multiple spaces between two words to a single space in the reversed string.
</pre>

 

<strong>Constraints:</strong>


<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> contains English letters (upper-case and lower-case), digits, and spaces <code>&#39; &#39;</code>.</li>
	<li>There is <strong>at least one</strong> word in <code>s</code>.</li>
</ul>

 

<b data-stringify-type="bold">Follow-up: </b>If the string data type is mutable in your language, can you solve it <b data-stringify-type="bold">in-place</b> with <code data-stringify-type="code">O(1)</code> extra space?


"""

class Solution:
    def reverseWords(self, s: str) -> str:
        