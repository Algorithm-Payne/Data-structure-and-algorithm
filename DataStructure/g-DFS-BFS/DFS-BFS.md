## BFS or DFS



搜索：查找某容器中的成员，如果不存在，则会遍历一边。告知不存在

遍历：从开始到结尾

> 注意，此处的开始及结尾为相对概念。开始与结尾均可以由开发人员控制。例如从第二个到倒数第二个

### 搜索基本概念

- 无知（盲目）搜索：按照事先约定的某种次序，系统地在状态空间中搜索目标状态
- 有知(智能)搜索：如果对问题有所了解，能运用某些知识，克服无知搜索的盲目性，有效的指导搜索
- 盲目(暴力)搜索的两大代表：深度优先搜索和广度优先搜索

有且仅访问一次

### 遍历的基本概念

从开始到结尾，按照顺序依次迭代

### 无序

在线性结构下，搜索约等于遍历。也就说二者差别并不是那么大

在非线性结构下，由策略不同分为深度优先(DFS)与广度优先(BFS)

### 有序

搜索即搜索，遍历即遍历。

### DFS(深度优先搜索)

度优先搜索属于图算法的一种，是一个针对图和树的遍历算法，英文缩写为DFS即Depth First Search。深度优先搜索是图论中的经典算法，利用深度优先搜索算法可以产生目标图的相应拓扑排序表，利用拓扑排序表可以方便的解决很多相关的图论问题，如最大路径问题等等。一般用堆数据结构来辅助实现DFS算法。其过程简要来说是对每一个可能的分支路径深入到不能再深入为止，而且每个节点只能访问一次。

#### 代码实现

##### 递归写法


```python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

##### 非递归写法

```python
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
```



### BFS(广度优先搜索)

 广度优先搜索（也称宽度优先搜索，缩写BFS，以下采用广度来描述）是连通图的一种遍历算法这一算法也是很多重要的图的算法的原型。Dijkstra单源最短路径算法和Prim最小生成树算法都采用了和宽度优先搜索类似的思想。其别名又叫BFS，属于一种盲目搜寻法，目的是系统地展开并检查图中的所有节点，以找寻结果。换句话说，它并不考虑结果的可能位置，彻底地搜索整张图，直到找到结果为止。基本过程，BFS是从根节点开始，沿着树(图)的宽度遍历树(图)的节点。如果所有节点均被访问，则算法中止。一般用队列数据结构来辅助实现BFS算法。

```python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

