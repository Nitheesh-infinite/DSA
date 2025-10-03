# Problem: deque-and-inheritance

In this problem, you will implement a Deque class that will be inherited by a Queue and a Stack class.
The Deque class will have the following functions:

1. Constructors: Take arguments like the capacity of the deque, scaling factor etc.
2. Destructor: Deallocate the dynamic array that stores the deque.

3. push_back: Push data to the back of the deque.
4. pop_front: Remove and return the front element of the deque.
5. push_front: Push data to the front of the deque.
6. pop_back: Remove and return the back element of the deque.
7. peek_front: Return the front element of the deque without removing it.
8. peek_back: Return the back element of the deque without removing it.

9. get_capacity: Return the capacity of the deque.
10. get_size: Return the size of the deque.
11. is_empty: Return true if the deque is empty, and false otherwise.

NOTE: The Deque class should be able to resize itself when it is full and auto_resize is true. The capacity
of the deque should be scaled by the resize factor. 

-> Rescaling should only happen when the deque is full and auto_resize is true. If the existing array is not full,
but the back of the array is the end of the array, then you need to work in a circular manner and keep track of the 
start and end of the array. 

You need to implement the Deque, Queue, and Stack classes as described above. 
Overload << operator so that cout works. You need to implement the overloaded << operator for the Queue
class. You need to implement the overloaded << operator for the Stack class. You need to implement the copy
constructor for the Queue class. You need to implement the copy constructor for the Stack class. You need to
make the necessary member functions of the Deque class public in the Queue and Stack classes.

Read about class inheritance and friend functions. Understand copy constructors and how to use them before you 
attempt this problem.


# Your Task

Implement the above functions in deque_inheritance.h

# Input/Output

Read main.cpp to understand input and output pattern.

- **Input** (stdin):
We read a sequence of commands: 
  - queue : selects queue.
  - stack : selects stack.
  - push  : pushes an element
  - pop   : pops an element
  - peek  : peeks at at the front/back of the queue/stack (look at main.cpp) 
  - print : the content of the queue/stack

- **Output** (stdout):
 These commands response with some print in stdout. Please look at the main.cpp


Use command line inputs from the Inputs floder to test your code and validate against the Outputs folder.
