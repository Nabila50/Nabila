# Dictionary
# data are stored in Key: Value form
# Key is always being in string form. never being a bullian or integer form.
# always work with curley brackets.
# It is mutable but Keys must be immutable.
# it is dynamic.
# No duplicate key is allowed
# two types of dictionary: 1. Ordered Dictionary 2. Regular or inordered dictionary
# Ordered Dictionary: it is a type which remembers the insertion in order of (key, value) pairs in the dictionary and preserve in order form.
# Order dictionary consume more memory than a regular dictionary.
nabila= {
    'age': 30,
    'first_name': 'nabila',
    '2nd_name:': 'nawshin',
    'home town': 'jessore',
    'occupation': 'student',
    'country': 'Bangladesh',
    'contact_num': '017476548245',
}
print(nabila)
print(type(nabila))
print(nabila['country'])
print(len(nabila))

# another system to write the dictionary
nawshin = dict(age=31, first_name= 'nabila', last_name= 'nawshin,')
print(nawshin)