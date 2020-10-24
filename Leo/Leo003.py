a = 10
b = 3
c = 10

print(id(b))
b = a
print(b)

print(id(a))  #印出該記憶體位置
print(id(b))

a = 3
print(id(a))
print(id(b))  #a改變值並不會讓b的記憶體位置改變
print(id(c))