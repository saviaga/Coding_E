<h2>674. Longest Continuous Increasing Subsequence</h2><h3>Easy</h3><hr><div data-read-aloud-multi-block="true"><p data-speechify-sentence="">Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest <strong>continuous increasing subsequence</strong> (i.e. subarray)</em>. The subsequence must be <strong>strictly</strong> increasing.</p>

<p data-speechify-sentence="">A <strong>continuous increasing subsequence</strong> is defined by two indices <code>l</code> and <code>r</code> (<code>l &lt; r</code>) such that it is <code>[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]</code> and for each <code>l &lt;= i &lt; r</code>, <code>nums[i] &lt; nums[i + 1]</code>.</p>

<p>&nbsp;</p>
<p data-speechify-sentence=""><strong>Example 1:</strong></p>

<pre data-speechify-sentence=""><strong>Input:</strong> nums = [1,3,5,4,7]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
</pre>

<p data-speechify-sentence=""><strong>Example 2:</strong></p>

<pre data-speechify-sentence=""><strong>Input:</strong> nums = [2,2,2,2,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
</pre>

<p>&nbsp;</p>
<p data-speechify-sentence=""><strong>Constraints:</strong></p>

<ul data-read-aloud-multi-block="true">
	<li data-speechify-sentence=""><code>0 &lt;= nums.length &lt;= 10<sup style="">4</sup></code></li>
	<li data-speechify-sentence=""><code>-10<sup style="">9</sup> &lt;= nums[i] &lt;= 10<sup style="">9</sup></code></li>
</ul>
</div>