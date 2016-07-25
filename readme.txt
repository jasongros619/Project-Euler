Highlights of Problem Solutions - Project Euler

I found out about Project Euler from several of my friends who are CCS computing majors. (Link to Euler). I found the site interesting and was inspired to see how many problems I could solve. Some of the problems are especially interesting to me. Below is a description of several problems that I am highlighting because they inspired me to develop an efficient algorithm, involved a great deal of analysis to simplify the problem, or resulted in a very unexpected solution.

PROBLEM 7
This is the first problem where I use my prime sieve to generate a list of primes. I am quite proud of my algorithm as it can calculate all the primes under a million in about a second. I commonly reuse this algorithm in other Project Euler problems. Sometimes I need to use it for finding primes up to a million or 10 million and the algorithm appears to work in O(n) time.

PROBLEM 12 and 13
Both problems further the prime sieve I used in Problem 7. For these problems however, I need to find the full prime factorization of numbers from 1 to n so my sieve returns for each number, one of its prime factors as opposed to a list of primes. I use this information with already computed prime factorizations of smaller numbers to solve for each number efficiently with dynamic programming.

PROBLEM 31
The problem asks for how many ways you can make 200 cents with various coins. I analyzed it mathematically to find a recursive formula and was able to write an algorithm that uses dynamic programming to solve the problem much more efficiently.

PROBLEM 51
There are several problems on Project Euler that ask you to find a set of numbers that share some property. An example problem is, "What is the largest set of primes with the same sum of their digits squared?" For these sorts of problems, I generally create some hash function that purposefully has collisions for numbers with the same property. Then I search my dictionary for which key has the most values. Problem 51 is probably the hardest of those that I have done and requires a much more complicated hash function.

PROBLEMS 14, 55, 74, 92, and 95
There are several 'chain' problems in Project Euler that involve sequences of numbers based on some function. An example might be each number is followed by the sum of each of their digits squared. Then you are asked to find which number within a range takes the longest to reach the end of its sequence. For this type of problem, I create a dictionary that stores the distance each number is from the end of its sequence. Then I use a function that both recursively computes the next number's distance if it has not been computed already, and returns the next number's distance + 1. I used this approach to solve these problems.

PROBLEM 94
This is my favorite problem in all of Project Euler. I analyzed it mathematically and kept reexamining it with techniques that I learnt in my CCS math classes. The problem asked me to solve it for values up to values of a million. My program goes way beyond what problem writers expected and can solve the problem in constant time for numbers of any value that the computer can reasonably handle.

PROBLEM 104
This problem asks for you to examine Fibonacci numbers. You are asked to find the smallest such number where both the first 9 digits and the last 9 digits contain each of the numbers 1 through 9 exactly once. I figured out a clever way to work around the problem of the fibonacci numbers growing exponentially and being impractical to work with.

PROBLEMS 301 and 500
These problems were also interesting.