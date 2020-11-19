# Tree

**树**是一种[数据结构](https://baike.baidu.com/item/数据结构/1450)，它是由*n(n>=1*)个有限结点组成一个具有层次关系的[集合](https://baike.baidu.com/item/集合)。把它叫做“树”是因为它看起来像一棵倒挂的树，也就是说它是根朝上，而叶朝下的。它具有以下的特点：

每个结点有零个或多个子结点；没有[父结点](https://baike.baidu.com/item/父结点/9796346)的结点称为根结点；每一个非根结点有且只有一个父结点；除了根结点外，每个子结点可以分为多个不相交的子树；

## 树的定义

树（*tree*）是包含n(n >= 1)个结点，n - 1条边的有穷集，其中：

（1）每个元素称为结点（*[node](https://baike.baidu.com/item/node/4689680)*）；

（2）有一个特定的结点被称为根结点或树根（*[root](https://baike.baidu.com/item/root/73226)*）。

（3）除根结点之外的其余数据元素被分为m(m >= 0)个互不相交的集合T1,T2,T3，其中每一个集合Ti(1 =< i =< m)本身也是一棵树，被称作原树的子树（*subtree*）。

树也可以这样定义：树是由根结点和若干颗子树构成的。树是由一个集合以及在该集合上定义的一种关系构成的。集合中的元素称为树的结点，所定义的关系称为父子关系。父子关系在树的结点之间建立了一个层次结构。在这种层次结构中有一个结点具有特殊的地位，这个结点称为该树的根结点，或称为树根。

单个结点是一棵树，树根就是该结点本身。设T1，T2，....Tk是树，它们的根结点分别为n1,n2,n3...nk。用一个新结点n作为n1,n2,n3...nk的父亲，则得到一棵新树，结点n就是新树的根。我们称n1,n2...nk为一组兄弟结点，它们都是结点n的子结点。我们还称T1,T2,T3为结点n的子树。

空集合也是树，称为[空树](https://baike.baidu.com/item/空树/20809571)。空树中没有结点。

孩子结点或[子结点](https://baike.baidu.com/item/子结点/9795653)：一个结点含有的子树的[根结点](https://baike.baidu.com/item/根结点/9795570)称为该结点的[子结点](https://baike.baidu.com/item/子结点/9795653)；

结点的度：一个结点含有的子结点的个数称为该结点的度；

[叶结点](https://baike.baidu.com/item/叶结点/9795627)或终端结点：[度](https://baike.baidu.com/item/度/5622311)为0的结点称为[叶结点](https://baike.baidu.com/item/叶结点/9795627)；

非终端结点或分支结点：[度](https://baike.baidu.com/item/度/5622311)不为0的结点；

双亲结点或[父结点](https://baike.baidu.com/item/父结点/9796346)：若一个结点含有[子结点](https://baike.baidu.com/item/子结点/9795653)，则这个结点称为其[子结点](https://baike.baidu.com/item/子结点/9795653)的[父结点](https://baike.baidu.com/item/父结点/9796346)；

[兄弟结点](https://baike.baidu.com/item/兄弟结点/9796359)：具有相同[父结点](https://baike.baidu.com/item/父结点/9796346)的结点互称为[兄弟结点](https://baike.baidu.com/item/兄弟结点/9796359)；

树的[度](https://baike.baidu.com/item/度/5622311)：一棵树中，最大的结点的度称为树的度；

结点的层次：从根开始定义起，根为第1层，根的子结点为第2层，以此类推；

树的高度或深度：树中结点的最大层次；

堂兄弟结点：双亲在同一层的结点互为堂兄弟；

结点的祖先：从根到该结点所经分支上的所有结点；

子孙：以某结点为根的子树中任一结点都称为该结点的子孙。

森林：由m(m >=0)棵互不相交的树的集合称为森林；

## 树的种类

无序树：树中任意节点的子结点之间没有顺序关系，这种树称为无序树,也称为自由树;

有序树：树中任意节点的子结点之间有顺序关系，这种树称为有序树；

二叉树：每个节点最多含有两个子树的树称为二叉树；

满二叉树：叶节点除外的所有节点均含有两个子树的树被称为满二叉树

完全二叉树：有![img](https://bkimg.cdn.bcebos.com/formula/94854d05669c053a705656ef4fe3c2d7.svg)个节点的满二叉树称为完全二叉树

哈夫曼树（最优二叉树）：带权路径最短的二叉树称为哈夫曼树或最优二叉树；

## 树节点的定义

```python
class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left,self.right = None, None
```

```java
public class TreeNode {
  public int val;
  public TreeNode left,right;
  public TreeNode(int val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}
```



## 树的遍历

树根据`根`,`左子树`,`右子树`的遍历顺序不同分为

- 前序遍历(Pre-order)：根-左-右
- 中序遍历(In-order)：左-根-右
- 后序遍历(Post-order)：左-右-根

### 遍历代码模版

```python
# 前序遍历
def preOreder(self, root):
  if root:
    self.traverse_path.append(root.val)
    preOreder(self.left)
    preOreder(self.right)

# 中序遍历
def inOreder(self, root):
  if root:
    preOreder(self.left)
    self.traverse_path.append(root.val)
    preOreder(self.right)
    
# 后序遍历
def postOreder(self, root):
  if root:
    preOreder(self.left)
    preOreder(self.right)
    self.traverse_path.append(root.val)

```

思考：为什么树的遍历大多都基于递归？

由树的定义知，树无法有效的进行循环。且拥有重复性

[树的理解演示](https://visualgo.net/zh/bst)