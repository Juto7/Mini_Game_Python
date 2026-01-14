# bangun datar segitiga
n = 5
for i in range (n, 0, -1):
    print("*" *i)
#  rata kanan
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

# sama kaki
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    

# segitiga kebalik
print("\n")

n = 5

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

