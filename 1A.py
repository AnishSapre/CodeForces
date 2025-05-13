numbers = input()
n, m, a = numbers.split(' ')
n = int(n)
m = int(m)
a = int(a)

if a == 1:
    print(n*m)
else:
    if n%a == 0:
        length = n//a
    else:
        length = (n//a) + 1
    if m%a == 0:
        breadth = m//a
    else:
        breadth = (m//a) + 1

    print(length * breadth)