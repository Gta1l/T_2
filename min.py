import sys

a = sys.argv[1:]

temp = int(a[0])
print(a)
for i in a:
    if int(i) < temp:
        temp = int(i)

print(temp)