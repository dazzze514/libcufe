cities=['Beijing','Tianjin','Shanghai','Guangzhou']
print(cities[0])
message="My favorite city is "
print(message+cities[0]+".")
cities[3]='Nanjing'
print(cities)
cities.append('Guangzhou')
print(cities)
cities.insert(0,'Shanxi')
print(cities)
del cities[1]
print(cities)
popped_city=cities.pop()
print(cities)
cities.remove('Shanghai')
print(cities)
cities.sort()
print(cities)
cities.reverse()
print(cities)
len(cities)
