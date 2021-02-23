<h2>1013. Partition Array Into Three Parts With Equal Sum</h2><h3>Easy</h3><hr><div data-read-aloud-multi-block="true"><p data-speechify-sentence="">Given an array of integers <code>arr</code>, return <code>true</code> if we can partition the array into three <strong>non-empty</strong> parts with equal sums.</p>

<p data-speechify-sentence="">Formally, we can partition the array if we can find indexes <code>i + 1 &lt; j</code> with <code>(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])</code></p>

<p>&nbsp;</p>
<p data-speechify-sentence=""><strong>Example 1:</strong></p>

<pre data-speechify-sentence=""><strong>Input:</strong> arr = [0,2,1,-6,6,-7,9,1,2,0,1]
<strong>Output:</strong> true
<strong>Explanation: </strong>0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
</pre>

<p data-speechify-sentence=""><strong>Example 2:</strong></p>

<pre data-speechify-sentence=""><strong>Input:</strong> arr = [0,2,1,-6,6,7,9,-1,2,0,1]
<strong>Output:</strong> false
</pre>

<p data-speechify-sentence=""><strong>Example 3:</strong></p>

<pre data-speechify-sentence=""><strong>Input:</strong> arr = [3,3,6,5,-2,2,5,1,-9,4]
<strong>Output:</strong> true
<strong>Explanation: </strong>3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
</pre>

<p>&nbsp;</p>
<p data-speechify-sentence=""><strong>Constraints:</strong></p>

<ul data-read-aloud-multi-block="true">
	<li data-speechify-sentence=""><code>3 &lt;= arr.length &lt;= 5 * 10<sup style="">4</sup></code></li>
	<li data-speechify-sentence=""><code>-10<sup style="">4</sup> &lt;= arr[i] &lt;= 10<sup style="">4</sup></code></li>
</ul>
</div>