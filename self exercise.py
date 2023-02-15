laptop = {'name': 'Lenovo',
          'model': 'Z450',
          'processor': 'AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx',
          'color': 'blackish',
          'RAM_space': '8 GB',
          'ROM_space': '4 GB',
          'windows': 11,
          'System_type': '64-bit',
          'longibity': '5 years',
}
print(laptop)
# find one item-------------------------------------------------------
print(laptop['model'])
print(laptop.get("windows"))

# to identify the all keys----------------------------------------------
print(laptop.keys())

# to identify only all the values------------------------------------------
print(laptop.values())

# to identify only items--------------------------------------------------
print(laptop.items())

# system for changing data--------------------------------------------------
laptop['color'] = 'white'
print(laptop)

laptop['windows'] = 13
print(laptop)

# or
laptop.update({'ROM_space': '8 GB'})
print(laptop)

# # data deleting system--------------------------------------------------------------------------------------------------

laptop.popitem()
print(laptop)

laptop.pop('model')
print(laptop)

del laptop['processor']
print(laptop)

# # if need to clear all the items from the dictionary-------------------------------------------------------------------

laptop.clear()
print(laptop)