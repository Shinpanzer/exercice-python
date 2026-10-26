def fibonacci(n):
    if n < 1:
        return "Erreur"

    if n <= 2:
        return 1

    a = 1
    b = 1

    for i in range(3, n + 1):
        a, b = b, a + b

    return b


n = int(input("Entre un nombre : "))
print(f"Le terme {n} est {fibonacci(n)}")