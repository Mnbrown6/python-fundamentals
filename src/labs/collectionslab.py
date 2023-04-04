""" Collections Lab"""

""" Task 1- Favorite Pizza"""


pizza = ['beef', 'green onions', 'cheese', 'red onion', 'chicken']


def pizza_toppings1():
    for toppings in pizza:
        print(toppings)

#pizza_toppings1()

def pizza_toppings2():
    pizza.append('Extra Beef')
    pizza.append('Spinach')
    for toppings in pizza:
        print(toppings)


#pizza_toppings2()


"""Task 2"""

""" Favorite Movies Collection"""
favorite_movies = {1985: 'Color Purple', 2022: 'Black Panther', 2023: 'Plane', 1982: 'Annie'}


def seen_flix():
    for key, value in favorite_movies.items():
        print(f'{key}: {value}')


seen_flix()











