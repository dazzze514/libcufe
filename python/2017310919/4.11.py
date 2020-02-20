pizzas=['sausage pizza','cheese pizza','beef pizza']
friend_pizzas=pizzas[:]
pizzas.append('corn pizza')
friend_pizzas.append('chicken pizza')
print("My favorite pizzas are:")
for pizza in pizzas[0:4]:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas[0:4]:
    print(friend_pizzas)
