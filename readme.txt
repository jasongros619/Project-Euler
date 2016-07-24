Some of the problems in Project Euler are very interesting to me.
Below is a description of several problems that I am highlighting because they inspired
me to develop an efficient algorithm,
involved a great deal of analysis to simplify the problem,
or resulted in a very unexpected solution.



Problem 7 is the first problem where I use my prime sieve to generate a list of primes. I am
quite proud of my algorithm as it can calculate all the primes under a million in about a second.
I commonly reuse this algorithm in other Project Euler problems. Sometimes I need to use it for
finding primes up to a million or 10 million and the algorithm appears to work in O(n) time.

Problem 12 and 23 both further the prime sieve I used in Problem 7. For these problems however, I need to find
the full prime factorization of numbers from 1 to n so my sieve returns for each number, one of its prime
factors as opposed to a list of primes. I use this information with already computed prime factorizations
of smaller numbers to solve for each number efficiently with dynamic programming.

Problem 31 is a great problem. It asks for how many ways you can make 200 cents with various coins.
I analyzed it mathematically to find a recursive formula and was able to write an algorithm that uses
dynamic programming to solve the problem incredibly efficiently.

Problem 51 is very interesting. There are several problems on Project Euler that ask you to find
a set of numbers that share some property. An example problem is, "What is the largest set of primes with the same
sum of their digits squared?" For these sorts of problems, I generally create some hash function that purposefully has collisions
for numbers with the same property. Then I search my dictionary for which key has the most values.
Problem 51 is probably the hardest of those that I have done and requires a much more complicated hash function.
Other problems like this include #, #, and #.

There are several 'chain' problems in Project Euler that involve sequences of numbers based on some function.
An example might be each number is followed by the sum of each of their digits squared. Then you are asked
to find which number within a range takes the longest to reach the end of its sequence. For this type of problem, I create a
dictionary that stores the distance each number is from the end of its sequence. Then I
use a function that both recursively computes the next number's distance if it has not been computed already, 
and returns the next number's distance + 1.
I use this to solve problems:
Problem 14 - Longest Collatz sequence
Problem 55 - Lychrel numbers
Probelm 74 - Digit Factorial Sums
Problem 92 - Square digit chains
Probelm 95 - Amicable chains

Problem 94 is one of my favorite problems in all of Project Euler. I analyzed it very much mathematically
and kept reexamining it with techniques I learnt in CCS math classes. The problem asked me
to solve it for values up to 10^6. My program goes way beyond what problem writers expected
and can solve the problem in constant time for numbers of any value that the computer can reasonably handle.

Problem 104 asks for you to examine Fibonacci numbers. You are asked to find the smallest such number where
both the first 9 digits and the last 9 digits contain each of the numbers 1 through 9 exactly once. I figured out
a clever way to work around the problem of the fibonacci numbers growing exponentially and being impractical to
work with.

Problem 301 is very intersting problem. Although the algorithm leading to the solution isn't that complex
the result of the problem in itself is quite interesting and very unexpected.

Problem 500 asks for the smallest number with 2^500500 factors (as in 1, 2, 3, and 6 for number 6). This is a
really big number for a problem as there are only around 500 something problems and they get increasingly difficult.
Interestingly the solution for it is surprisingly simple.