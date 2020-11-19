# 队列与栈

## 队列(Queue)

队列是一种特殊的[线性表](https://baike.baidu.com/item/线性表)，特殊之处在于它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作，和栈一样，队列是一种操作受限制的线性表。进行插入操作的端称为队尾，进行删除操作的端称为队头。队列中没有元素时，称为空队列。

队列的数据元素又称为队列元素。在队列中插入一个队列元素称为入队，从队列中删除一个队列元素称为出队。因为队列只允许在一端插入，在另一端删除，所以只有最早进入队列的元素才能最先从队列中删除，故队列又称为先进先出（FIFO—first in first out）[线性表](https://baike.baidu.com/item/线性表)。

### 顺序队列

建立顺序队列结构必须为其静态分配或动态申请一片连续的存储空间，并设置两个指针进行管理。一个是队头指针front，它指向队头元素；另一个是队尾指针rear，它指向下一个入队元素的存储位置，

### 循环队列

在实际使用队列时，为了使队列空间能重复使用，往往对队列的使用方法稍加改进：无论插入或删除，一旦rear指针增1或front指针增1 时超出了所分配的队列空间，就让它指向这片连续空间的起始位置。自己真从MaxSize-1增1变到0，可用取余运算rear%MaxSize和front%MaxSize来实现。这实际上是把队列空间想象成一个环形空间，环形空间中的存储单元循环使用，用这种方法管理的队列也就称为循环队列。除了一些简单应用之外，真正实用的队列是循环队列。

## 栈(Stack)

栈作为一种[数据结构](https://baike.baidu.com/item/数据结构)，是一种只能在一端进行插入和删除操作的特殊[线性表](https://baike.baidu.com/item/线性表)。它按照先进后出的原则存储数据，先进入的数据被压入栈底，最后的数据在栈顶，需要读数据的时候从栈顶开始弹出数据（最后一个数据被第一个读出来）。栈具有记忆作用，对栈的插入与删除操作中，不需要改变栈底[指针](https://baike.baidu.com/item/指针)。

栈是允许在同一端进行插入和删除操作的特殊[线性表](https://baike.baidu.com/item/线性表)。允许进行插入和删除操作的一端称为栈顶(top)，另一端为栈底(bottom)；栈底固定，而栈顶浮动；栈中元素个数为零时称为空栈。插入一般称为[进栈](https://baike.baidu.com/item/进栈)（PUSH），删除则称为退栈（POP）。栈也称为先进后出表。

栈可以用来在[函数](https://baike.baidu.com/item/函数)调用的时候存储断点，做[递归](https://baike.baidu.com/item/递归)时要用到栈！

## Queue & Stack 关键点

- Queue 先入先出:添加删除皆为O(1),查找O(N)

- Stack 先入后出:添加删除皆为O(1),查找O(N)

  #### 实现Queue（Python）

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop()

    def length(self):
        return len(self.queue)

```

#### 实现Stack（Python）

```python
class stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        self.item.pop()

    def length(self):
        return len(self.item)
```

## 双端队列(duque)

deque （double-ended queue，双端队列）是一种具有[队列](https://baike.baidu.com/item/队列/14580481)和[栈](https://baike.baidu.com/item/栈/12808149)的性质的[数据结构](https://baike.baidu.com/item/数据结构/1450)。双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。

双端队列是限定插入和删除操作在表的两端进行的[线性表](https://baike.baidu.com/item/线性表/3228081)。这两端分别称做端点1和端点2。也可像栈一样，可以用一个铁道转轨网络来比喻双端队列。在实际使用中，还可以有输出[受限的双端队列](https://baike.baidu.com/item/受限的双端队列/6918051)（即一个端点允许插入和删除，另一个端点只允许插入的双端队列）和输入受限的双端队列（即一个端点允许插入和删除，另一个端点只允许删除的双端队列）。而如果限定双端队列从某个端点插入的元素只能从该端点删除，则该双端队列就蜕变为两个栈底相邻的栈了。

```python
class deque(object):
    """
    deque([iterable[, maxlen]]) --> deque object
    
    A list-like sequence optimized for data accesses near its endpoints.
    """
    def append(self, *args, **kwargs): # real signature unknown
        """ Add an element to the right side of the deque. """
        pass

    def appendleft(self, *args, **kwargs): # real signature unknown
        """ Add an element to the left side of the deque. """
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        """ Remove all elements from the deque. """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of a deque. """
        pass

    def count(self, value): # real signature unknown; restored from __doc__
        """ D.count(value) -> integer -- return number of occurrences of value """
        return 0

    def extend(self, *args, **kwargs): # real signature unknown
        """ Extend the right side of the deque with elements from the iterable """
        pass

    def extendleft(self, *args, **kwargs): # real signature unknown
        """ Extend the left side of the deque with elements from the iterable """
        pass

    def index(self, value, start=None, stop=None): # real signature unknown; restored from __doc__
        """
        D.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        return 0

    def insert(self, index, p_object): # real signature unknown; restored from __doc__
        """ D.insert(index, object) -- insert object before index """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """ Remove and return the rightmost element. """
        pass

    def popleft(self, *args, **kwargs): # real signature unknown
        """ Remove and return the leftmost element. """
        pass

    def remove(self, value): # real signature unknown; restored from __doc__
        """ D.remove(value) -- remove first occurrence of value. """
        pass

    def reverse(self): # real signature unknown; restored from __doc__
        """ D.reverse() -- reverse *IN PLACE* """
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        """ Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left. """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of a deque. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, iterable=(), maxlen=None): # known case of _collections.deque.__init__
        """
        deque([iterable[, maxlen]]) --> deque object
        
        A list-like sequence optimized for data accesses near its endpoints.
        # (copied from class doc)
        """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __reversed__(self): # real signature unknown; restored from __doc__
        """ D.__reversed__() -- return a reverse iterator over the deque """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ D.__sizeof__() -- size of D in memory, in bytes """
        pass

    maxlen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """maximum size of a deque or None if unbounded"""


    __hash__ = None
```



## 优先队列

插入0(1)，删除O(log n)

底层实现的数据结构较为多样与复杂：Heap、BST(binary search Tree)、AVL、Treap

优先队列(priority queue)

普通的队列是一种先进先出的数据结构，元素在队列尾追加，而从队列头删除。在优先队列中，元素被赋予优先级。当访问元素时，具有最高优先级的元素最先删除。优先队列具有最高级先出 （first in, largest out）的行为特征。通常采用堆数据结构来实现。

```python
class priority_queue:
    def __init__(self):
        self.queue = []

    def put(self, val):
        self.queue.append(val)
        cur = len(self.queue) - 1
        while cur > 0:
            parent = (cur - 1) // 2
            if self.queue[parent] > self.queue[cur]:
                self.queue[cur], self.queue[parent] = self.queue[parent], self.queue[cur]
            else:
                break
            cur = parent

    def get(self):
        first = self.top()
        last = self.queue.pop()
        if not self.empty():
            self.queue[0] = last
            cur = 0
            while cur < len(self.queue):
                left_child = 2 * cur + 1
                right_child = 2 * cur + 2
                # 越界
                if right_child >= len(self.queue) or left_child >= len(self.queue):
                    break
                # 无需向下调整
                if self.queue[cur] <= min(self.queue[left_child], self.queue[right_child]):
                    break
                # 与哪个结点交换
                if self.queue[left_child] < self.queue[right_child]:
                    self.queue[left_child], self.queue[cur] = self.queue[cur], self.queue[left_child]
                    cur = left_child
                else:
                    self.queue[right_child], self.queue[cur] = self.queue[cur], self.queue[right_child]
                    cur = right_child
        return first

    def top(self):
        if self.empty():
            raise Exception('the queue is empty!')
        return self.queue[0]

    def find(self, val):
        return val in self.queue

    def get_index(self, index):
        if index >= len(self.queue):
            raise Exception('the index is out of the range!')
        return self.queue[index]

    def empty(self):
        return len(self.queue) == 0
```

![](https://tva1.sinaimg.cn/large/0081Kckwgy1gkulvrtx9mj31ao0tk0zk.jpg)

此图来自：<https://www.bigocheatsheet.com/>

## 推荐阅读

- [Java 的 PriorityQueue 文档](http://docs.oracle.com/javase/10/docs/api/java/util/PriorityQueue.html)
- [Java 的 Stack 源码](http://developer.classpath.org/doc/java/util/Stack-source.html)
- [Java 的 Queue 源码](http://fuseyism.com/classpath/doc/java/util/Queue-source.html)
- [Python 的 heapq](http://docs.python.org/2/library/heapq.html)
- [高性能的 container 库](http://docs.python.org/2/library/collections.html)