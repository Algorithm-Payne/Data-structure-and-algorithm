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

## Queue

## Stack

