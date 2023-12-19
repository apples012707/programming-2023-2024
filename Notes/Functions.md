A function is a block of code that can be reused over and over again.

We can input data to the function
We can refer to the data as parameters

We use the term arguments to describe the ACTUAL data that we put into the function.

```python
def area_of_a_square(sidelength: float):
	"""Calculates the carea of a square.
	Results are in units squared.

	Params:

	sidelength - length of one side of the square"""

	area = sidelength ** 2
	
	print(f"The area of a squre with side length = {sidelength} is:{area} square units"")

area_of_a_square(12.2). # 12.2 is the argument
```




# Functions with Return Values


```python
def adder(x: int, y: int) -> int:
	"""Returns the sum of two given numbers."""
	sum = x + y

	return sum
adder(10, 2)        # 12
print(adder(10, 2)) # this will print the value
```


The return keyword does two things in a function:

1. Stops the function.
2. If there's a value after the return keyword, it sends the value back to where the function is called.

```python
def linear_seach(l: list, item: any) -> int:
	"""Search through a list and if found, returns the index of the first occuence of the item.

	Params:
		l - list we're search through
		item - item we're looking for
	"""

	counter = 0

	# Search algorithm
	for thing in l:
		if thing == item:
			return counter
		counter += 1

	return -1
```


# Recursion

Recursion is an elegant way to repeat a pattern.

Fractals are examples of patterns that can be described recursively.

A recursive function must have. three parts:

1. A *function*
2. Somewhere in the body code-block, the function should call itself.
3. A base case.


## Factorials and Recursion

```python
0! = 1
1! = 1

2! = 1 * 2
2! = 1! * 2

3! = 1 * 2 * 3
3! =   2!  * 3
```


