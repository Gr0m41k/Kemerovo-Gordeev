a = int(input())
c = []

def gf():
    print("1")
#sd
for i in range(1, a):
    number = int('1' * i)
    if number <= a:
        c.append(str(number ** 2))
print(', '.join(c))