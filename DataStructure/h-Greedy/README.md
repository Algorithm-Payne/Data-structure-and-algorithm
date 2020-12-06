# 贪心算法

贪心算法（英语：greedy algorithm），又称贪婪算法，是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是最好或最优的算法。

比如在旅行推销员问题中，如果旅行员每次都选择最近的城市，那这就是一种贪心算法。

贪心算法在有最优子结构的问题中尤为有效。最优子结构的意思是局部最优解能决定全局最优解。简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。
**贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。**

**动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。**



贪心法可以解决一些最优化问题，如：求图中的最小生成树、求哈夫曼编码……对于其他问题，贪心法一般不能得到我们所要求的答案。一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。在不同情况，选择最优的解，可能会导致辛普森悖论（Simpson's Paradox），不一定出现最优的解。

贪心算法在数据科学领域被广泛应用，特别是金融工程。其中一个贪心算法例子就是Ensemble method。
> 细节
> 创建数学模型来描述问题。
> 把求解的问题分成若干个子问题。
> 对每一子问题求解，得到子问题的局部最优解。
> 把子问题的解局部最优解合成原来解问题的一个解。
> 实现该算法的过程：
> 从问题的某一初始解出发；while 能朝给定总目标前进一步 do，求出可行解的一个解元素；
> 最后，由所有解元素组合成问题的一个可行解。
