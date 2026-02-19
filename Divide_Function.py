x = int(input("Enter a number 1 : "))
y = int(input("Enter a number 2 : "))

def divide(x, y):
    if y == 0:
        print("Sıfıra bölme işlemi yapılamaz! Kuralları çiğneyemezsin.")
        return

    if x % y == 0:
        print(f"Sonuç: {int(x / y)}")
    else:
        z = x % y
        print(f"Tam bölünmüyor. Kalan: {z}")

divide(x, y)