numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)
print(numbers_v2) # => -[2, 4, 6, 8]

numbers_v3 = (lambda i:i*2, numbers)
print(numbers_v3) # => (<function <lambda> at 0x7fcb2fd63d90>, [1, 2, 3, 4])
numbers_v3 = map(lambda i:i*2, numbers)
print(numbers_v3) # => <map object at 0x7f4f37657f40>
numbers_v3 = list(map(lambda i:i*2, numbers))
print(numbers_v3) # => [2, 4, 6, 8]


frutas = ["manzana", "banana", "uva", "sandía", "naranja"]
frutas_deliciosas = list(map(lambda nombre: "deliciosa " + nombre, frutas))
print(frutas_deliciosas) # => ['deliciosa manzana', 'deliciosa banana', 'deliciosa uva', 'deliciosa sandía', 'deliciosa naranja']

