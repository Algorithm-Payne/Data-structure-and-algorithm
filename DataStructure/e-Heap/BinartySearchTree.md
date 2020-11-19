## Heap

堆：可以迅速查找到``一维度``数组中最大或最小的值(最大或最小择一)

根具根节点最大的堆叫做大顶堆(大根堆)

根具根节点最小的堆叫做小顶堆(小根堆)

### 常见的堆

有二叉堆、斐波那契堆等

假设为大顶堆，常见API：

find-max：O（1）

delete-Max：O（logN）

insert（create）： O（logN） or O(1)

![](https://tva1.sinaimg.cn/large/0081Kckwgy1gkusplmxosj30wu0g4djd.jpg)

## 二叉堆

通过二叉树实现二叉堆(注意：不是二叉搜索树)

二叉堆满足以下性质：

1. 是一颗完全的二叉树
2. 树中任意节点的值>=其子节点的值

### 二叉堆实现细节

1. 二叉堆一般基于“数组”实现
2. 假设“第一个”在索引为0的位置，父节点与子节点关系如下
   1. 索引为i其左子树索引为(2 * i + 1)
   2. 索引为i其右子树索引为(2 * i + 2)
   3. 索引为i其根子树索引为floor((i - 1) / 2 )

插入：0（logN）

新元素一律插入到堆尾部

向上调整整个堆 

删除:O(logN)

将堆尾元素替换到顶部

依此从根部向下调整整个堆 

### 实现堆

#### Java

```java
import java.util.Arrays;
import java.util.NoSuchElementException;


public class BinaryHeap {


    private static final int d = 2;
    private int[] heap;
    private int heapSize;


    /**
     * This will initialize our heap with default size.
     */
    public BinaryHeap(int capacity) {
        heapSize = 0;
        heap = new int[capacity + 1];
        Arrays.fill(heap, -1);
    }


    public boolean isEmpty() {
        return heapSize == 0;
    }


    public boolean isFull() {
        return heapSize == heap.length;
    }




    private int parent(int i) {
        return (i - 1) / d;
    }


    private int kthChild(int i, int k) {
        return d * i + k;
    }


    /**
     * Inserts new element in to heap
     * Complexity: O(log N)
     * As worst case scenario, we need to traverse till the root
     */
    public void insert(int x) {
        if (isFull()) {
            throw new NoSuchElementException("Heap is full, No space to insert new element");
        }
        heap[heapSize] = x;
        heapSize ++;
        heapifyUp(heapSize - 1);
    }


    /**
     * Deletes element at index x
     * Complexity: O(log N)
     */
    public int delete(int x) {
        if (isEmpty()) {
            throw new NoSuchElementException("Heap is empty, No element to delete");
        }
        int maxElement = heap[x];
        heap[x] = heap[heapSize - 1];
        heapSize--;
        heapifyDown(x);
        return maxElement;
    }


    /**
     * Maintains the heap property while inserting an element.
     */
    private void heapifyUp(int i) {
        int insertValue = heap[i];
        while (i > 0 && insertValue > heap[parent(i)]) {
            heap[i] = heap[parent(i)];
            i = parent(i);
        }
        heap[i] = insertValue;
    }


    /**
     * Maintains the heap property while deleting an element.
     */
    private void heapifyDown(int i) {
        int child;
        int temp = heap[i];
        while (kthChild(i, 1) < heapSize) {
            child = maxChild(i);
            if (temp >= heap[child]) {
                break;
            }
            heap[i] = heap[child];
            i = child;
        }
        heap[i] = temp;
    }


    private int maxChild(int i) {
        int leftChild = kthChild(i, 1);
        int rightChild = kthChild(i, 2);
        return heap[leftChild] > heap[rightChild] ? leftChild : rightChild;
    }


    /**
     * Prints all elements of the heap
     */
    public void printHeap() {
        System.out.print("nHeap = ");
        for (int i = 0; i < heapSize; i++)
            System.out.print(heap[i] + " ");
        System.out.println();
    }


    /**
     * This method returns the max element of the heap.
     * complexity: O(1)
     */
    public int findMax() {
        if (isEmpty())
            throw new NoSuchElementException("Heap is empty.");
        return heap[0];
    }


    public static void main(String[] args) {
        BinaryHeap maxHeap = new BinaryHeap(10);
        maxHeap.insert(10);
        maxHeap.insert(4);
        maxHeap.insert(9);
        maxHeap.insert(1);
        maxHeap.insert(7);
        maxHeap.insert(5);
        maxHeap.insert(3);


        maxHeap.printHeap();
        maxHeap.delete(5);
        maxHeap.printHeap();
        maxHeap.delete(2);
        maxHeap.printHeap();
    }
}
```

#### Python

```python
import sys 
class BinaryHeap: 
  
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.Heap = [0]*(self.capacity + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    def parent(self, pos): 
        return pos//2
  
    def leftChild(self, pos): 
        return 2 * pos 
  
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    def isLeaf(self, pos): 
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
  
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    def heapifyDown(self, pos): 
  
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.heapifyDown(self.leftChild(pos)) 
  
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.heapifyDown(self.rightChild(pos)) 
  
    def insert(self, element): 
        if self.size >= self.capacity : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
   
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.heapifyDown(pos) 
  
    def delete(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.heapifyDown(self.FRONT) 
        return popped 
    def isEmpty(self):
        return self.size == 0
        
    def isFull(self): 
        return self.size == self.capacity
if __name__ == "__main__": 
      
    print('The minHeap is ') 
    minHeap = BinaryHeap(5)
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    minHeap.minHeap() 
  
    minHeap.Print() 
    print("The Min val is " + str(minHeap.delete())) 
```

[wiki-堆](https://en.wikipedia.org/wiki/Heap_(data_structure))

