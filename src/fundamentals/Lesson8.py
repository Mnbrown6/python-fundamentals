""" Lesson 8 - Collections Part 1  """

""" List collection using square brackets. Allows
duplicates, is changeable, and is ordered list.
"""
colors = ['green', 'red', 'blue', 'magenta', 'yellow',
          'orange', 'purple', 'black', 'gray']
trucks = ['chevy', 'ford', 'dodge', 'toyota', 'nissan', 'jeep']

""" This list collection has different data types, duplicates 
and another list.
"""
my_list = [42,'Happy','Python','True',colors,'Happy']



def example_direct():
    """Print the list directly  provides result
    that mirrors the list directly. Including brackets and
    how each type was entered into the list.
    """
    print(colors)


# example_direct()

def example_for():
    """ To print a list it is best to use a for loop"""
    for color in colors:
        print(color)


# example_for()


def single_item():
    """ To get a single item from a list, you use bracket
    notation and the index number.
    """
    print(colors[2])

# single_item()



def slice_list():
    """ Slicking will get a range of values from the list
    This list includes a start and stop index. These items
    are added to a new variable as its own list.
    """
    examples = my_list [1:4]
    print(examples)
    for value in examples:
        print(value)


# slice_list()


def negative_slice():
    """ This slice used negative numbers. It begins
    from -1 instead of 0, when it comes to the first time
    """

    example2 = my_list[-4:-2]
    print(example2)
    for value in example2:
        print(value)

# negative_slice()


def slice_start():
    """ This slice has a start with no end defined.
    The slice will print to the end of the list.
    """
    print(trucks[3:])


# slice_start()


def slice_end():
    """ This slice has a stop with no start index.
    The slice will start from the beginning and print
    up to, but not including the end index"""

    print(trucks[:3])

# slice_end()

def example_len():
    """ The len function will return the total number
    of items in the list.
    """
    count = len(trucks)
    print(count)




# example_len()

def search_color():
    """ using the in membership operator, we can search
    in a list to find an item. This operator will return a
    True or False statement.
    """
    if 'blue' in colors:
        print('Blue is in the list of colors')
    else:
        print('Blue is not in the list of colors')


# search_color()


def while_demo():
    count = 0
    while count < len(trucks):
        if 'dodge'in trucks[count]:
            print('Dodge Ram')
        else:
            print(trucks[count])
        count += 1

# while_demo()



def append_list():
    """ The append method will add a item to
    the end of the list. """
    trucks.append('Rivian')
    for truck in trucks:
        print(truck)



#append_list()


def insert_list():
    """ The insert method will add an item
    at a specific index.
    """

    colors.insert(3, 'Lime')
    for color in colors:
        print(color)

#insert_list()

def extend_list():
    """ The extend method will join a list
    to another list."""
    odd_numbers = [1, 3, 5]
    even_numbers = [2, 4, 6]
    odd_numbers.extend(even_numbers)
    for number in odd_numbers:
        print(number)



#extend_list()


def example_remove():
    """ The remove method will remove an item
    based on its value.
    """

    my_list.remove(42)
    for value in my_list:
        print(value)

#example_remove()

def example_pop():
    """The pop method will remove the last item when no
    index value is supplied. Otherwise, with the index, it
     will remove the item by its index."""
    colors.pop()
    colors.pop(3)
    for color in colors:
        print(color)



#example_pop()

def example_del():
    """ The del keyword will remove on item based on
    its index.
    """
    del trucks[2]
    for truck in trucks:
        print(truck)


#example_del()

def example_del_complete():
    """ The del statement when used directly with a list,
    will remove the list completely. The variable will no longer
    have a reference to a list type. The variable will no longer
    be usable for a list or any other type.
    """
    del my_list
    for stuff in my_list:
        print(stuff)

# example_del_complete()

def example_clear():

    """ The clear method will remove all items from the list,
    but the list type will still be part of the variable it is
    assigned to.
    """
    my_list.clear()
    my_list.append('Monday')
    for stuff in my_list:
        print(stuff)

# example_clear()


def example_replace():
    """ Update or replace and item based on its index.
   """
    my_list[1] = 'Monday'
    for value in my_list:
        print(value)

#example_replace()

fruit= ('apple', 'banana', 'cherry', 'kiwi', 'melon','mango')

""" Tuple collection is an ordered collection that is immutable.
This means that once the collection is created, it can not be changed directly
"""

def example_tuple():
    print(fruit)
    print(fruit[2])
    print(fruit[-2])
    print('Tuple loop print below')
    for food in fruit:
        print(food)


# example_tuple()


def example_tuple_slice():
    print(fruit[1:3])
    print(fruit[-3:-1])


#example_tuple_slice()


def example_add_tuple():
    """ In order to change a tuple, we have to
    convert the existing tuple to a list. Then
    we can update the list. Then convert it back to
    a tuple.
    """
    my_fruit = list(fruit)
    my_fruit[2] = 'peach'
    new_fruit = tuple(my_fruit)
    for food in new_fruit:
        print(food)


example_add_tuple()
