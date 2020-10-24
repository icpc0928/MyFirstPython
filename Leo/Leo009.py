#轉二進位

a = 100
ba = bin(a)
b = 200
bb = bin(b)

c = ba + bb
ca = ba[2::]
cb = bb[2::]
cab = int(ca) + int(cb)

print(bin(a))
print(c)
print(ba)
print(cab)
