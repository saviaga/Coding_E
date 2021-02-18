<h2>944. Delete Columns to Make Sorted</h2><h3>Easy</h3><hr><div data-read-aloud-multi-block="true"><p data-speechify-sentence="">You are given an array of <code>n</code> strings <code>strs</code>, all of the same length.</p>

<p data-speechify-sentence="">The strings can be arranged such that there is one on each line, making a grid. For example, <code>strs = ["abc", "bce", "cae"]</code> can be arranged as:</p>

<pre data-speechify-sentence="">abc
bce
cae
</pre>

<p data-speechify-sentence="">You want to <strong>delete</strong> the columns that are <strong>not sorted lexicographically</strong>. In the above example (0-indexed), columns 0 (<code>'a'</code>, <code>'b'</code>, <code>'c'</code>) and 2 (<code>'c'</code>, <code>'e'</code>, <code>'e'</code>) are sorted while column 1 (<code>'b'</code>, <code>'c'</code>, <code>'a'</code>) is not, so you would delete column 1.</p>

<p data-speechify-sentence="">Return <em>the number of columns that you will delete</em>.</p>

<p>&nbsp;</p>
<p data-speechify-sentence=""><strong>Example 1:</strong></p>

<pre data-speechify-sentence=""><strong>Input:</strong> strs = ["cba","daf","ghi"]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
</pre>

<p data-speechify-sentence=""><strong>Example 2:</strong></p>

<pre data-speechify-sentence=""><strong>Input:</strong> strs = ["a","b"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.
</pre>

<p data-speechify-sentence=""><strong>Example 3:</strong></p>

<pre data-speechify-sentence=""><strong>Input:</strong> strs = ["zyx","wvu","tsr"]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.
</pre>

<p>&nbsp;</p>
<p data-speechify-sentence=""><strong>Constraints:</strong></p>

<ul data-read-aloud-multi-block="true">
	<li data-speechify-sentence=""><code>n == strs.length</code></li>
	<li data-speechify-sentence=""><code>1 &lt;= n &lt;= 100</code></li>
	<li data-speechify-sentence=""><code>1 &lt;= strs[i].length &lt;= 1000</code></li>
	<li data-speechify-sentence=""><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>
</div>