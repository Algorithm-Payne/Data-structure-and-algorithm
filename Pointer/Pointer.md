[TOC]

# Pointer

> It includes python, but not just python, but also C, Java, any programming language

## Introduction

Pointers are an essential part of a programming language, and if you don't use them correctly, you're basically losing all the functionality and flexibility that programming languages allow.Pointer is not only a language foundation or characteristic, but also an idea. if you want learning well.

The pointer can be understood as a bridge of communication，So，It's really important！

## what's Pointer?

A pointer is a variable which contains the address in memory of another variable. We can have a pointer to any variable type.

The *unary* or *monadic* operator **&** gives the ``address of a variable''.

The *indirection* or dereference operator ***** gives the ``contents of an object *pointed to* by a pointer''.



## When and where to use it?

- When you want find anyone in tuple\List\Array\number from numbers\ string from str...
- Where you want to swap places
- When you want to sort
- In computer memory
- Method or object

- 。。。

Oh，It has so many uses

## How to use it？

> The use of the foundation can be found in other articles. I will use the pointer or pointer thought to accomplish something

### Practical topics

[Answer source code](https://github.com/Algorithm-Payne/Question-bank/tree/master/Sundries),Suggest doing it first

1. [LeetCode-Two-sum](https://leetcode-cn.com/problems/two-sum/)
2. [LeetCode-Three-sum](https://leetcode-cn.com/problems/two-sum/)
3. [LeetCode-Four-sum](https://leetcode.com/problems/4sum/)
4. [LeetCode-move-zeroes](https://leetcode-cn.com/problems/move-zeroes/)
5. [LeetCode-reverse-linked-list](https://leetcode.com/problems/reverse-linked-list/)
6. [LeetCode-container-with-most-water](https://leetcode.com/problems/container-with-most-water/)
7. [LeetCode-reverse-linked-list](https://leetcode.com/problems/reverse-linked-list/)
8. [LeetCode-swap-nodes-in-pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
9. [LeetCode-linked-list-cycle](https://leetcode.com/problems/linked-list-cycle/)
10. [LeetCode-linked-list-cycle-ii](https://leetcode.com/problems/linked-list-cycle-ii/)
11. ... ...

#### TwoSum

> Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.
>
> You may assume that each input would have ***exactly\* one solution**, and you may not use the *same* element twice.
>
> You can return the answer in any order.

```python
# Method 1 
'''
Tow Pointer,Nested loop.
'''
# Pseudo code 
for loop -> i(nums.index)
	for loop -> j(nums.index)
    	if nums[i] + num[j] == target and nums[i] != nums[j]:
            # two pointer: i, j
            return i, j
# Method 2 
'''
Because of this relationship: nums[i] + nums[j] == target
therefore:  nums[i] = target - nums[j]
'''
# Pseudo code
for loop -> i (nums.index)
a = target - nums[i]
if a in nums and nums.index(a) != i:
	return i, nums.index(a)
# Method 3 - other ideas
'''
Pursuing speed
You might think about the relationship between index and number
if you know dcit from key -> values find is fast, you maybe use it  
'''
new HashMap
index -> Value - > index
```

#### Move Zore

> Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.
>
> Note:
>
> 1. You must do this **in-place** without making a copy of the array.
> 2. Minimize the total number of operations.

```shell
# two pointers slow and fast: -> i, j
i -> start
j -> for loop 
when j != 0, Move it to the front that from nums
```

#### Linked List Cycle

> Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
>
> There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
>
> Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.
>
> **Follow up:**
>
> Can you solve it using `O(1)` (i.e. constant) memory?
>
> **Constraints:**
>
> - The number of the nodes in the list is in the range `[0, 104]`.
> - `-105 <= Node.val <= 105`
> - `pos` is `-1` or a **valid index** in the linked-list.

```shell
# two pointer: slow and fast
when  slow == fast 
	return
```



> Pointers are basic, but flexible. I believe you can also learn its flexible characteristics, as well as the idea of pointer.
>
> All changes do not depart from their ancestorsBelieve me, you can, too.
>