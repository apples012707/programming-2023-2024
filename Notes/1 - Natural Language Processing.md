y typ
Properties

#notes #programming 




### Output
We can display text and symbols using output

We us the print( ) function to. display output



```python
print ( )
```



## [Headers]
3

# Comments
Comments are pieces of text that are Not interpreted by Python 
This means that the text is ignored
We us the # symbol to make comments


# Variables
Variables allow us to store information for the time our app is running.

```python
favourite_food = input("what is your favourite food?")
```

#Respond to their answer
print(f"ooo,fav_food)





# Lists
In python,  lists are a collection of items
We store value inside of lists
The values of the items can be different
Order matters in a list

# Creating a List
To make a list, we use brackets to surround our list
We separate the indvidual items with commas

```python
come_list = ["Jimmy", "Sara", "Frederique"]
```


# Access Elements in the Lists
We can access the individual things from lists using brackets notation 
In the ecample below, we'll use bracket notation to access "Sara"

```python
some_list[1]# "Sara"
some_list[0]# "Jimmy"
some_list[2]# "Frederique"
```


Inside the brackets, we give the index of the item we want
python uses 0-index counting, which means we start counting at 0



## [Modules]

Modules are pieces of code that we can borrow in Python
This includes things like functions

For example, in random w used the .choice( ) function
to choose something randomly from lists 

These pieces of code are not automatically included
so w need to import them into our code explicitly



# **Import
The *import keyword loads the module in our Python file
**import should be at the top of our file, under the header


# The Time Module
Time allows us to play around with anything related to time
Specifically, we can use time to pause our code


```python
import time

# pause our code for 1 second
time.sleep(1)
```



# Iterating *n* Number of Times

Recall that when we iterate over lists, the item tells us the current element we are on.

When we iterate using rang( ) , the item tells us how many times we've looped since the beginning.

For example, we can leverage this in the way below:

```python
for i in range (5):
	print(i)
```



# Range (<number>)

range( ) is a faction that gives you a sequence of numbers starting at 0 by default. By default it also goes up by 1. It stops right before the number that we provide as input.

We can modify range( ) to start, stop, and count up/down with different numbers
