## 递归

程序调用自身的编程技巧称为递归（ recursion）。递归做为一种[算法](https://baike.baidu.com/item/算法)在[程序设计语言](https://baike.baidu.com/item/程序设计语言)中广泛应用。 一个过程或[函数](https://baike.baidu.com/item/函数)在其定义或说明中有直接或间接调用自身的一种方法，它通常把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解，递归策略只需少量的程序就可描述出解题过程所需要的多次重复计算，大大地减少了程序的代码量。递归的能力在于用有限的[语句](https://baike.baidu.com/item/语句)来定义对象的[无限集合](https://baike.baidu.com/item/无限集合)。一般来说，递归需要有边界条件、递归前进段和递归返回段。当边界条件不满足时，递归前进；当边界条件满足时，递归返回。

递归，就是在运行的过程中调用自己。

构成递归需具备的条件：

[![函数嵌套调用过程示例](https://bkimg.cdn.bcebos.com/pic/7e3e6709c93d70cf13780beefbdcd100bba12b56?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1)](https://baike.baidu.com/pic/递归/1740695/0/7e3e6709c93d70cf13780beefbdcd100bba12b56?fr=lemma&ct=single)函数嵌套调用过程示例

\1. 子问题须与原始问题为同样的事，且更为简单；

\2. 不能无限制地调用本身，须有个出口，化简为非递归状况处理。

在[数学](https://baike.baidu.com/item/数学)和[计算机科学](https://baike.baidu.com/item/计算机科学)中，递归指由一种（或多种）简单的基本情况定义的一类对象或方法，并规定其他所有情况都能被还原为其基本情况。

递归实现注意点，**终止条件**

### 递归实现

#### Python

```python
def recursion(level,param1,param2...):
  # recursion terminator
  if level > MaxLevel:
    process_result
  
  # process logic in current level
  process(level, data)
  
  # dill down
  self.recursion(level + 1,param1,param2...)
  
  # reverse the current level status if needed
```

#### Java

```java
public void recur(int level, int param) { 
  // terminator 
  if (level > MAX_LEVEL) { 
    // process result 
    return; 
  }
  // process current logic 
  process(level, param); 
  // drill down 
  recur( level: level + 1, newParam); 
  // restore current status 
 
}
```

### 注意点

- 不要人肉递归
- 找到最近最简方法，将其拆解成可重复解决的``子问题``
- 数学归纳法思维

## 分治

在求解一个输入规模为n，而n的取值又很大的问题时，直接求解往往非常困难。这时，可以先分析问题本身所具有的某些特性，然后从这些特性出发，选择某些适当的[设计策略](https://baike.baidu.com/item/设计策略/11061445)来求解。这种方法，就是所谓的[分治法](https://baike.baidu.com/item/分治法/2407337)。(分而治之，后 meager)

采用[分治法](https://baike.baidu.com/item/分治法)解决的问题一般具有的特征如下：

1.  问题的规模缩小到一定的规模就可以较容易地解决。
2.  问题可以分解为若干个规模较小的模式相同的子问题，即该问题具有最优子结构性质。
3.  合并问题分解出的子问题的解可以得到问题的解。
4.  问题所分解出的各个子问题之间是独立的，即子问题之间不存在公共的子问题

### 代码实现

#### Python

```python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], param1, param2, ...) 
  subresult2 = self.divide_conquer(subproblems[1], param1, param2, ...) 
  subresult3 = self.divide_conquer(subproblems[2], param1, param2, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

#### Java

```java
private static int divide_conquer(Problem problem, ) {
  
  if (problem == NULL) {
    int res = process_last_result();
    return res;     
  }
  subProblems = split_problem(problem)
  
  res0 = divide_conquer(subProblems[0])
  res1 = divide_conquer(subProblems[1])
  
  result = process_result(res0, res1);
  
  return result;
}
```

## 回溯

回溯采用试错的思想，它尝试分步去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分布答案不能得到有效的正确答案。它将取消上一步或上几步的计算。再通过其他可能的分步解再次尝试寻找问题的答案

回溯法通常使用简单的递归来实现，在反复上述的步骤后可能出现两种情况：

- 找到一个可能存在的正确答案
- 尝试了所有分步方法后，宣告没有正确答案

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算





最优子结构：动态规划(DP)

相同子问题更具情况：分支或回溯等