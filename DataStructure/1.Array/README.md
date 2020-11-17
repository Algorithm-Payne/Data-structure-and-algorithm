# Python-Array

## List

> 在其他语言中通常有数组这么一个概念，而Python衍生出，动态数组-列表、及静态数组-元组。
>
> **数组**（Array）是有序的元素序列。 [1] 若将有限个类型相同的变量的[集合](https://baike.baidu.com/item/集合/2908117)命名，那么这个名称为数组名。组成数组的各个变量称为数组的分量，也称为数组的元素，有时也称为[下标变量](https://baike.baidu.com/item/下标变量/12713827)。用于区分数组的各个元素的数字编号称为下标。数组是在[程序设计](https://baike.baidu.com/item/程序设计/223952)中，为了处理方便， 把具有相同类型的若干元素按有序的形式组织起来的一种形式。 这些有序排列的同类数据元素的集合称为数组。

序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

Python有6个序列的内置类型，但最常见的是列表和元组。

序列都可以进行的操作包括索引，切片，加，乘，检查成员。

此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表的数据项不需要具有相同的类型

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

```python
# 列表的定义
_list = []

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

# 列表的索引取值(索引有正负之分，符号代表方向) [start:end] or [::sep]
print("list1[0]: ", list1[0])       # list1[0]:  physics
print("list2[1:5]: ", list2[1:5])   # list2[1:5]:  [2, 3, 4, 5]
print(list1[:])                    # ['physics', 'chemistry', 1997, 2000]
print("list2[::-1]", list2[::-1])   # list2[::-1] [5, 4, 3, 2, 1]   倒序取值

# 列表的循环遍历
# 索引遍历
for _ in range(len(list1)):
    print(list1[_], end=" ")        # physics chemistry 1997 2000
print()
# 直接遍历
for i in list2:
    print(i, end=" ")               # 1 2 3 4 5

print()
for j in enumerate(list3):          # (0, 'a') (1, 'b') (2, 'c') (3, 'd')
    print(j, end=" ")
```

- 列表的操作

```python
operating_list = [1]
# append:追加，在末尾追加元素
operating_list.append(2)
print(operating_list)           # [1, 2]
# 清空:clean
# print(operating_list.clear())   # None
# 计数
print(operating_list.count(1))  # 1

# 根据值获取索引，从前往后，返回且仅返回第一个"找到"的值
print(operating_list.index(1))  # 0
print(operating_list.index(2))  # 1

# 插入, 若插入的索引已有数据，则会将其后移一位，进行插入。若超出索引则会实现appeend
operating_list.insert(1, 6)
print(operating_list)           # [1, 6, 2]

# pop：与append恰恰相反，pop(index) 如果index为空时，默认推出最后一位数字。
# 若有索引值，则pop出索引所对应的值
print(operating_list.pop())     # 2 pop出的值
print(operating_list)           # [1, 6]
operating_list.pop(1)           # [6]
print(operating_list)           # [1]
# remove 从列表中删除对应的值
operating_list.remove(1)
print(operating_list)              # []


# reverse： 列表反转


# sort			列表排序
```

List Api

```python
class list(object):
    """
    Built-in mutable sequence.
    
    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified.
    """
    def append(self, *args, **kwargs): # real signature unknown
        """ Append object to the end of the list. """
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        """ Remove all items from list. """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of the list. """
        pass

    def count(self, *args, **kwargs): # real signature unknown
        """ Return number of occurrences of value. """
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        """ Extend list by appending elements from the iterable. """
        pass

    def index(self, *args, **kwargs): # real signature unknown
        """
        Return first index of value.
        
        Raises ValueError if the value is not present.
        """
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        """ Insert object before index. """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """
        Remove and return item at index (default last).
        
        Raises IndexError if list is empty or index is out of range.
        """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        """
        Remove first occurrence of value.
        
        Raises ValueError if the value is not present.
        """
        pass

    def reverse(self, *args, **kwargs): # real signature unknown
        """ Reverse *IN PLACE*. """
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        """
        Sort the list in ascending order and return None.
        
        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).
        
        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.
        
        The reverse flag can be set to sort in descending order.
        """
        pass

```

| 操作 | 最好 | 最坏 |
| :--: | :--: | :--: |
| 增加 | O(1) | O(n) |
| 删除 | O(1) | O(n) |
| 查找 | O(1) | O(1) |



## Tuple

> Python的元组与列表类似，不同之处在于元组的元素不能修改。
>
> 元组使用小括号，列表使用方括号。
>
> 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

```python
tup1 = ()	# 创建空元组
tup1 = ('physics', 'chemistry', 1987, 2010)
tup2 = (1, 2, 3, 4, 5 )
tup1 = (20,)	# 元组中只包含一个元素时，需要在元素后面添加逗号
```

元组操作

```python
# 访问元组
tuple_1 = (1, 2, 3, 4, 5, 6)
print(tuple_1[0])   # 1
print(tuple_1[1])   # 2
print(tuple_1[2])   # 3

# 元组遍历
for _ in range(len(tuple_1)):
    print(tuple_1[_], end=" ")  # 1 2 3 4 5 6
print()
for i in enumerate(tuple_1):
    print(i, end=" ")   # (0, 1) (1, 2) (2, 3) (3, 4) (4, 5) (5, 6)
print()
for j in tuple_1:
    print(j, end=" ")   # 1 2 3 4 5 6

# 删除元组
del tuple_1
print(tuple_1)  # print(tuple_1) NameError: name 'tuple_1' is not defined

# 修改元组

# 我们仅可对元组进行拼接，无法像list一样修改内部的值

```

> 元组与列表的区别
>
> `元组`固定且不可变，这意味着元组一旦被创建，和列表不同它的内容无法被修改及它的大小也无法被改变
>
> 虽然他并不支持改变大小，但是我们的可以将两个元组合并生成一个新的元组。这一操作类似于列表的resize操作，但我们不需要为新生成的元组分配任何额外的空间
>
> 元组与列表的append 相比较，我们会开到他们的复杂度时O(n)而不是列表的O(1)。这是因为对元组没添加一个新元素都会有分配与复制的操作。而不是列表那样仅在额外空间耗尽的时候发生
>
> 
>
> 元组的静态特性的另一个好处在于Python后台发生的事情：资源缓存
>
> Python是一门垃圾回收语言，这意味着当一个变量不再被使用时，Python会将该变量使用的内存释放会操作系统，以供其他程序或变量使用。然而，对于长度为1～20 的元组，即使他们不在被使用，他们的内存空间并不会立即返还给操作系统，而是留下来以待未来使用。

## Linked List

### 为什么需要链表

​    顺序表的构建需要预先知道数据大小来申请连续的存储空间，而在进行扩充时又需要进行数据的搬迁，所以使用起来并不是很灵活。链表结构可以充分利用计算机内存空间，实现灵活的内存动态管理。

### 链表的定义

 链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是不像顺序表一样连续存储数据，而是在每一个节点（数据存储单元）里存放下一个节点的位置信息（即地址）。

### 单向链表

单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。

![](https://tva1.sinaimg.cn/large/0081Kckwgy1gkslghdw85j30lc05lt9g.jpg)

- 表元素域elem用来存放具体的数据。
- 链接域next用来存放下一个节点的位置（python中的标识）
- 变量p指向链表的头节点（首节点）的位置，从p出发能找到表中的任意节点。

链表失去了顺序表随机读取的优点，同时链表由于增加了结点的指针域，空间开销比较大，但对存储空间的使用要相对灵活。链表与顺序表的各种操作复杂度如下所示：

- 增加删除：O(1)
- 查找O(n)

### 链表的实现

#### 单向链表实现

```python
#首先定义节点类Node

class LinkNode(object):
#1. __init__初始化结点信息
    def __init__(self, data, pnext = None):
        '''
        data:节点保存的数据
        '''
        self.data = data
        self._next = pnext
#2. 用于定义Node的字符输出
    def __repr__(self):
        '''
        用于定义Node的字符输出，
        print为输出data
        '''
        return str(self.data)

#初始化链表的类
class LinkList(object):
#1. 初始化链表
    def __init__(self):
        #属性：链表头head,链表长度length
        self.head = None
        self.length = 0

#2. 链表初始化函数，尾插法，插入data
    def initlist_tail(self, data):
        #创建头结点，其实是第一个有值节点
        self.head = LinkNode(data[0])
        pnext = self.head
        for i in data[1:]:
            node = LinkNode(i)
            pnext .next = node
            pnext = pnext .next

#3. 判断链表是否为空
    def isEmpty(self):
        return (self.length == 0)

#4. 增加一个节点（在链为添加）
    def append(self, dataOrNode):
        '''在链表尾添加'''
        item = None

        if isinstance(dataOrNode, LinkNode):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

#5. 删除一个节点： delete()
    def delete(self, index):
        '''
        删除一个节点，需要把链表长度减一
        '''
        if self.isEmpty():
            print("this linked list is empty.")
            return
        
        if index < 0 or index >= self.length:
            print('error: out of index')
            return

        '''
        要注意删除第一个节点的情况
        '''
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        '''
        prev为保存前导节点
        node为保存当前节点
        '''
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            prev.next = node._next
            self.length -= 1
#6. 修改一个节点： update()
    def update(self, index, data):
        '''修改一个节点'''
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
            
        j = 0
        node = self.head
        while node.next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

#7. 查找一个节点: getItem()
    def getItem(self, index):
        '''查找节点'''
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
        
        j = 0
        node = self.head

        while node._next and j < index:
            node = node._next
            j += 1

        return node.data
#8. 查找一个节点的索引： getIndex()
    def getIndex(self, data):
        '''查找索引'''
        j = 0
        if self.isEmpty():
            print("this linked list is empty")
            return
        
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            print("%s not found" %str(data))
            return

#9. 查找一个节点：insert()
    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print("this linked list is empty")
            return

        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            item._next = node
            prev._next = item
            self.length += 1
#10. 清空链表
    def clear(self):
        '''清空链表'''
        self.head = None
        self.length = 0

#11. 取链表长度
    def getLength(self):
        return self.length

#12. 在索引值为 index 的结点后插入结点key
    def insertElem(self, key, index):
        pnext= self.head
        j = 1
        while pnext and j < index:
            pnext = pnext.next
            j += 1
        if(pnext == 0 or j > index): #若出错则退出
            exit(0)
            print('insert error')
        node = LinkNode(key)
        node.next = pnext.next
        pnext.next = node
        print('inserted LinkList:')
        self.ReadList()

#13. 删除第 index个 结点后的那一个节点
    def deleteElem(self, index):
        pnext = self.head
        j = 1
        while pnext and j < index:
            pnext = pnext.next
            j += 1
        if(pnext == 0 or j > index): #若出错则退出
            exit(0)
            print('insert error')
        q = pnext.next
        pnext.next = q.next
        print('deleted LinkList:')
        self.ReadList()

#14. 链表逆序
    def reverseList(self):
        pnext = self.head


    def __repr__(self):
        if self.isEmpty():
            return "empty chain table"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist

    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print "error: out of index"
            return
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print "error: out of index"
            return
        self.update(ind, val)

    def __len__(self):
        return self.length
```

#### 双向链表实现

双向循环链表

一种更复杂的链表是“双向链表”或“双面链表”。每个节点有两个链接：一个指向前一个节点，当此节点为第一个节点时，指向空值；而另一个指向下一个节点，当此节点为最后一个节点时，指向空值。

```python
lass Node(object):
    """双向链表节点"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):
    """双向链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print cur.item,
            cur = cur.next
        print ""

    def add(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self._head
            # 将_head的头节点的prev指向node
            self._head.prev = node
            # 将_head 指向node
            self._head = node

    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 移动到链表尾部
            cur = self._head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur



    def search(self, item):
        """查找元素是否存在"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
```



### 跳表

增加了向前指针的链表叫作跳表。跳表全称叫做跳跃表，简称跳表。跳表是一个随机化的数据结构，实质就是一种可以进行二分查找的有序链表。跳表在原有的有序链表上面增加了多级索引，通过索引来实现快速查找。跳表不仅能提高搜索性能，同时也可以提高插入和删除操作的性能。

他的最大优势是原理简单、方便拓展、效率更高

只适用于元素有序的情况下

#### 跳表的实现

```python
# coding: utf-8

import random


class Node(object):
    """
    跳跃表节点
    """

    def __init__(self, key, level):
        self.key = key

        # 当前节点的指向的下一个节点, 用列表维护对应的层数, 列表的索引是层数, 对象是节点
        self.forward = [None] * (level + 1)

    def __str__(self):
        return "Node({})".format(str(self.key))


class SkipList(object):
    """
    跳跃表
    """

    def __init__(self, max_lvl, P):
        self.max_level = max_lvl  # 最高层数
        self.P = P  # 掷硬币的建层概率
        self.header = Node(-1, self.max_level)  # 初始化头节点
        self.level = 0  # 当前层数

    def random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.max_level:
            lvl += 1

        return lvl

    def insertElement(self, key):
        update = [None] * (self.max_level + 1)
        current = self.header

        """
        从跳越列表的最高层开始向后移动当前引用
        当要插入的键大于当前节点旁边的键值时，向后移动当前引用
        否则在 update 中插入当前值，向下移动一层并继续搜索
        """
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]  # 往右挪
            update[i] = current

        current = current.forward[0]

        """
        如果 current 是 NULL 意味着我们已经到达了列表尾部或当前节点和要插入的节点值不一样, 我们要在 update[0] 和 current 之间插入
        """
        if current is None or current.key != key:
            # 为节点随机生成层数
            rlevel = self.random_level()

            # 如果超过当前层, 补全中间层
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                # 更新当前跳跃表的层数
                self.level = rlevel

            # 生成新的节点
            n = Node(key, rlevel)

            # 插入每一层
            for i in range(rlevel + 1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

            # print("Successfully inserted key {}".format(key))

    def delete_element(self, search_key):

        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < search_key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is not None and current.key == search_key:

            for i in range(self.level + 1):

                # 如果往上层没有要删除的节点则提前结束
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            del current

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

            print("Successfully deleted {}".format(search_key))

    def search_element(self, key):
        current = self.header
        n = 0
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
                n += 1
        print(n, "次")

        current = current.forward[0]

        if current and current.key == key:
            # print("Found key ", key)
            pass

    def display_list(self):
        print("*****Skip List******")
        head = self.header
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl))
            node = head.forward[lvl]
            node_list = []
            while node is not None:
                node_list.append(str(node.key))
                node = node.forward[lvl]
            print("->".join(node_list))


if __name__ == '__main__':
    lst = SkipList(5, 0.5)
    lst.insertElement(3)
    lst.insertElement(7)
    lst.insertElement(12)
    lst.insertElement(6)
    lst.insertElement(19)
    lst.insertElement(9)
    lst.insertElement(26)
    lst.insertElement(21)
    lst.insertElement(17)
    lst.insertElement(25)
    lst.display_list()

    lst.search_element(12)

    lst.delete_element(12)
    lst.display_list()

    # print("*" * 20)
    # print(lst.header)
    # print(lst.header.forward[0])
    # print(lst.header.forward[0].forward[0])
    # print(lst.header.forward[0].forward[0].forward[0])
    # print("*" * 20)
    # print(lst.header.forward[2])
    # print(lst.header.forward[2].forward[2])
    # print(lst.header.forward[2].forward[2].forward[2])
```

> 跳表的实现参考：https://blog.csdn.net/jiangbo721/article/details/106336940

推荐阅读

- [Java 源码分析（ArrayList）](http://developer.classpath.org/doc/java/util/ArrayList-source.html)

- [Linked List 的标准实现代码](http://www.geeksforgeeks.org/implementing-a-linked-list-in-java-using-class/)

- [Linked List 示例代码](http://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked Lists/code/LinkedList.java)
- [Java 源码分析（LinkedList）](http://developer.classpath.org/doc/java/util/LinkedList-source.html)

- LRU Cache - Linked list：[ LRU 缓存机制](http://leetcode-cn.com/problems/lru-cache)
- Redis - Skip List：[跳跃表](http://redisbook.readthedocs.io/en/latest/internal-datastruct/skiplist.html)、[为啥 Redis 使用跳表（Skip List）而不是使用 Red-Black？](http://www.zhihu.com/question/20202931)