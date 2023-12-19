## 2-Dimensional List

So far, all the lists we've used are one-dimensional.

```python
some-list = ["blue", "red", "green"]
```

We can create two-dimensional lists that in short, are multiple lists inside a bigger list.

```python
som_ 2d_list = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
		   # r  c
some_2d_list[0][0] # -> 1
some_2d_list[0][1] # -> 2
```

## Tuples

Tuples (toopels or tuhpels) are like lists except for one main thing.

Tuples are immutable. Immutable means that you can't change the contents of a tuple.

Because they are immutable they have some performance benefits.

```python
some_tuple = (1, 2, 3, 4, 5)
```

To create a tuple, use parentheses instead of brackets.

## Images and Tuples

The basic unit of measurement in images a pixel.
The pixel information is stored in a tuple of three-values (3-tuple).

The 3-tuples tells us for ONE PORTION of the image, what the RED, GREEN, BLUE values are. (red, green, blue)

```python
	     r,  g,  b
RED -   (255, 0, 0)
BLUE -  (0, 0, 255)
GREEN - (0, 255, 0)
```
