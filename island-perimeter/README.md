<h2>463. Island Perimeter</h2><h3>Easy</h3><hr><div data-read-aloud-multi-block="true"><p data-speechify-sentence="">You are given <code>row x col</code> <code>grid</code> representing a map where <code>grid[i][j] = 1</code> represents&nbsp;land and <code>grid[i][j] = 0</code> represents water.</p>

<p data-speechify-sentence="">Grid cells are connected <strong>horizontally/vertically</strong> (not diagonally). The <code>grid</code> is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).</p>

<p data-speechify-sentence="">The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.</p>

<p>&nbsp;</p>
<p data-speechify-sentence=""><strong>Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/island.png" style="width: 221px; height: 213px;">
<pre data-speechify-sentence=""><strong>Input:</strong> grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
<strong>Output:</strong> 16
<strong>Explanation:</strong> The perimeter is the 16 yellow stripes in the image above.
</pre>

<p data-speechify-sentence=""><strong>Example 2:</strong></p>

<pre data-speechify-sentence=""><strong>Input:</strong> grid = [[1]]
<strong>Output:</strong> 4
</pre>

<p data-speechify-sentence=""><strong>Example 3:</strong></p>

<pre data-speechify-sentence=""><strong>Input:</strong> grid = [[1,0]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p data-speechify-sentence=""><strong>Constraints:</strong></p>

<ul data-read-aloud-multi-block="true">
	<li data-speechify-sentence=""><code>row == grid.length</code></li>
	<li data-speechify-sentence=""><code>col == grid[i].length</code></li>
	<li data-speechify-sentence=""><code>1 &lt;= row, col &lt;= 100</code></li>
	<li data-speechify-sentence=""><code>grid[i][j]</code> is <code>0</code> or <code>1</code>.</li>
</ul>
</div>