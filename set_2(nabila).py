#Union set:
# it is combined all different sets all togther. it is worked as update in set.

set1 = {'germany', 'italy', 'netherlands', 'sweden', 'belgium', 'France'}
set2 = {'dog', 'cow', 'goat', 'cat', 'sheep', 'rat', 'rabbit'}
set3 = {'rose', 'merry gold', 'jasmin', 'night queen', 'jarbara'}
set4 = {'ferary', 'teslan', 'bmw' 'mercedez'}

union = set1.union(set2)
print(union)

print(set1 | set2)   # another way to find union
# multiple set in union
union1 = set1.union(set2, set3, set4)
print(union1)
print(set1 | set2 | set3 | set4)
# Intersection:
# it is just print the combined data bewteen to data.

country = {'germany', 'italy', 'netherlands', 'sweden', 'belgium', 'France'}
animal = {'dog', 'cow', 'goat', 'cat', 'sheep', 'rat', 'rabbit', 'germany'}

intersection = animal.intersection(country)
print(intersection)

# symentric difference:
# it is print those data which are not common between two set of data.
country = {'germany', 'italy', 'netherlands', 'sweden', 'belgium', 'France'}
animal = {'dog', 'cow', 'goat', 'cat', 'sheep', 'rat', 'rabbit', 'germany'}
set3 = {'rose', 'merry gold', 'jasmin', 'night queen', 'jarbara'}
set4 = {'ferary', 'teslan', 'bmw' 'mercedez'}
sym_dif = country.symmetric_difference(animal)
print(sym_dif)

print(set3^set4^country^animal)   # symentic difference for multiple data

# set difference:
country = {'germany', 'italy', 'netherlands', 'sweden', 'belgium', 'France', 'night queen'}
animal = {'dog', 'cow', 'goat', 'cat', 'sheep', 'rat', 'rabbit', 'germany'}
set3 = {'rose', 'merry gold', 'jasmin', 'night queen', 'jarbara'}
set4 = {'ferary', 'teslan', 'bmw' 'mercedez', 'rose'}
print(animal.difference(country))

print(set3-set4-country)