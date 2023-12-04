a = int(input())
c = []

def gf():
    print("new branch 1")

for i in range(1, a):
    number = int('1' * i)
    if number <= a:
        c.append(str(number ** 2))
print(', '.join(c))