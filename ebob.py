def ebob(a, b):
    while b:
        a, b = b, a % b
    return a    

print("Ilk sayiyi giriniz:")
y = int(input())
print("Ikinci sayiyi giriniz:")
x = int(input())

print("Ebob:", ebob(y, x))