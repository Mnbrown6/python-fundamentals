"""Strings Lab Task 1"""
milkshake: str = 'This statement has empty spaces '

def get_pos_value():
    print(milkshake[6:17])

def get_neg_value():
    print(milkshake[-17:-6])

get_pos_value()
get_neg_value()


"""Task 2"""

method_sample: str = 'This statement has empty spaces '

# strip()
print(method_sample.strip())

# upper()
print(method_sample.upper())

# find()
print(method_sample.find('eme'))

# find()
print(method_sample.count('s'))

"Task3"

def basic_escape_seq():
    value_a: str = 'Jack and Jill' '\n went up the hill ' '\n to fetch a pail of water.''\n Jack fell down\n'\
' and broke his crown\n'' and Jill came tumbling after.'

    print(value_a)


basic_escape_seq()

