"""
The string <code>&quot;PAYPALISHIRING&quot;</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)


<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

And then read line by line: <code>&quot;PAHNAPLSIIGYIR&quot;</code>


Write the code that will take a string and make this conversion given a number of rows:


<pre>
string convert(string s, int numRows);
</pre>

 

<strong class="example">Example 1:</strong>


<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 3
<strong>Output:</strong> &quot;PAHNAPLSIIGYIR&quot;
</pre>

<strong class="example">Example 2:</strong>


<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 4
<strong>Output:</strong> &quot;PINALSIGYAHRPI&quot;
<strong>Explanation:</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

<strong class="example">Example 3:</strong>


<pre>
<strong>Input:</strong> s = &quot;A&quot;, numRows = 1
<strong>Output:</strong> &quot;A&quot;
</pre>

 

<strong>Constraints:</strong>


<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), <code>&#39;,&#39;</code> and <code>&#39;.&#39;</code>.</li>
	<li><code>1 &lt;= numRows &lt;= 1000</code></li>
</ul>

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        