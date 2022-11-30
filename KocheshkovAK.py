print("Калькулятор! Пожалуйста, введите выражение вида: 1 + 2")
a, f, b = input().split(" ")
a, b = int(a), int(b)
if f == "+":
    print(a + b)
if f == "-":
    print(a - b)
if f == "*":
    print(a * b)
if f == "/":
    print(a / b)
