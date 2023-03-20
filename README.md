# CIS3301-CODE-12-Fibonacci-With-Recursion

## Instructions

In this CODE assignment, you are asked to create a program that computes the Fibonacci number using recursion. 

* To complete the assignment, you need to implement the code inside the function `get_fibonacci_number` and `get_fibonacci_number_sequence`
* The `get_fibonacci_number` function receives a `position` numeric value as argument.
* The `get_fibonacci_number` uses recursion to calculate the number that is the `position` specified by the argument.
* The `get_fibonacci_number` returns a int() **number**.
  + For example, the Fibonacci number for position 3 is 2 and the Fibonacci number for position 5 is 5.
* The `get_fibonacci_number_sequence` function receives a `number` as an argument.
* The `get_fibonacci_number_sequence` relies on the function `get_fibonacci_number` to create a list with the Fibonaccie sequence numbers.
* The `get_fibonacci_number_sequence` should return a **list** that corresponds to the Fibonacci number sequence for a given `number` of elements.

  + For example, the Fibonacci sequence for 7 should return a list with the following nunbers:1,1,2,3,5,8,13
## Fibonacci Number

Fibonacci number (i.e., Fn) is a sequence of mathematically calculated numbers in which each number in the sequence is computed by adding the two precedent numbers in the list. For example, the **sixth** (located in the 6th position) Fibonacci number is **5** and its sequence is below:

* 1,1,2,3,5,8

The Fibonacci number appears in many contexts. Researchers in biology have found that the Fibonacci number sequence appears in several phenomena (e.g., flowers, branches, honeybees). In the world of computation, research has implemented optimization algorithms (e.g., search technique, heap data structure). Finally, in the context of business, many recognize a golden ratio obtained from the Fibonacci number sequence that is often used in trading and investing.

## Recursion

In programming, recursion is an algorithmic method in which a function calls itself to operate. Implementing recursion can speed up algorithms (e.g., search, sort, optimization) that otherwise will have to implement nested loops, which decreases the efficiency. Recursion is a popular method utilized in algorithms that follow the **divide and conquer** algorithmic paradigm.

## References

https://en.wikipedia.org/wiki/Fibonacci_sequence

https://science.howstuffworks.com/math-concepts/fibonacci-nature.htm

https://www.investopedia.com/articles/technical/04/033104.asp
