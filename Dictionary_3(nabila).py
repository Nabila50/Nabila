car = {
    'brand': 'BMW',
    'price': 25000,
    'color': 'black',
}

# Copy system of Dictionary

car1 = car.copy()
car2 = dict(car)
car['color'] = 'white'
print(car, car1, car2)

# Nested Dictionary

students={
    'nabila':{
        'name': 'Nawshin',
        'age': '31 years',
        'weight': '84.1 kg',
        'height': '5fee 2.5 inches',
        'cars': ['audi', 'tesla', 'bmw']
    },
    'Aysha':{
        'name': 'Akter',
        'age': '32years',
        'weight': '50kg',
        'height': '5feet',
        'cars': ['Marcedes', 'audi', 'Tesla', 'fiat']
    }
}
print(students['nabila'])
print(students['nabila']['cars'])
print(students['nabila']['cars'][1])