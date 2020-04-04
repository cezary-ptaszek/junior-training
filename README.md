# Universality tasks - Junior Python Dev - HCL
## Task 1.
Write a program that reads a number x and a positive integer n from the standard input and prints out x, 2x, ..., (n-1)x, nx to the standard output.

Consider the edge cases, e.g. n=1.

Input
Space separated two positive integers x and n.

Output
Integers x, 2x, ..., (n-1)x, nx, each in a separate line

Example\
Input:\
15 3

Output:\
15\
30\
45

## Task 2.
Write a program that reads from the standard input and will return the:

sum
difference
product
of all elements in the given list.

Input
An integer n (1 <= n <= 500) that denotes the number of elements in the list. The following n integers are the next elements of the list.

Output
Three integers:

sum
difference
product
of all the elements of the list.

Example\
Input:\
3\
4\
1\
6

Output:\
11\
-3\
24

## Task 3.
Write a class called Circle and implement methods given in the example below. A Circle is defined by its center and radius. Use the ValueError exception to handle incorrect data.

If needed, implement a class Point, which represents a point in 2-D space.

Input
integer r denoting the radius of circle1
space separated integers x and y denoting the center of circle1
integer r denoting the radius of circle2
space separated integers x and y denoting the center of circle2
space separated integers x1 and y1 denoting a shift of the center of circle1
Output
Three lines:

area of circle1 rounded down to the nearest integer
radius and center coordinates of the smallest circle containing both circle1 and circle2
center of circle1 shifted by (x1, x2)\
Example\
Input:\
10\
0 0\
5\
0 0\
1 1

Output:\
314\
10 0 0\
1 1

## Task 4.
Write a program that will (using regex) filter a file named atoms.txt so that only lines concerning a successful experiment remain. For example lines such as:

RUN 000039 COMPLETED. OUTPUT IN FILE yttrium.dat. 1 UNDERFLOW WARNING.

or

RUN 000058 COMPLETED. OUTPUT IN FILE cerium.dat. ALGORITHM DID NOT CONVERGE AFTER 100000 ITERATIONS.

should be discarded. You can assume every line in the file matches the scheme given below:

RUN [[NUMER Z DOKŁADNIE 6 CYFR]] COMPLETED. OUTPUT IN FILE [[NAZWA]].dat. [[COKOLWIEK]]

## Task 5.
Write a function decorator called *accepts* that checks whether a function was called with correct argument types.

## Task6.
Write a function decorator that will perform composition on a given function *n* times, where *n* is a parameter of the decorator.