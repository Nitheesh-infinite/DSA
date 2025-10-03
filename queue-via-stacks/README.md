# Problem: queue-via-stacks

We have seen both stacks and queues as part of our course. In this problem we will try to implement a queue using stacks.


# YOUR TASK

Stack implementation is already given In stack.h

In queue.h: Implement the queue functions using two stacks. 

The purpose of this exercise is to implement the functioning of a queue in C++.
The task is to implement a Queue using stacks. This requires two stacks.
Ensure that ALL of them are on average constant time. Amortized O(1) is OK.
You must NOT change the data members or ANY of the method signatures.
NOR are you allowed to add any additional methods or data members.
You are free to use only the PUBLIC methods of the Stack class here.

On empty queue dequeue and peek should throw the following exception:
```
      throw std::invalid_argument("Empty Queue Dequeue Error"); // For Dequeue
      throw std::invalid_argument("Empty Queue Peek Error")   ; // Peek
```

You must NOT add ANY other includes than what is already here.

# INPUT/OUTPUT

You are provided with main.cpp which will take input from the tests and show the status of 
whether you have passed the tests case or not. There will be 8 total test cases.


# Files to Edit [Do not edit any other files]:

queue-via-stack.h
