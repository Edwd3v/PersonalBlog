
from functools import reduce
numbers = [2, 3, 4, 5]
print(numbers)

# Definimos la función de multiplicación
def multiply(accumulated, next_num_for_multiply):
    print("acomulado = ",accumulated)
    print("numero a multiplicar = ", next_num_for_multiply)
    return accumulated * next_num_for_multiply

# Usamos reduce para aplicar la función de multiplicación a los números
result = reduce(multiply, numbers)

print(result)  # Imprimirá el resultado de 2 * 3 * 4 * 5 = 120