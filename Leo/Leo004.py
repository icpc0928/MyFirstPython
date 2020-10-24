#圓周率3.14 半徑 7.77 計算周長及面積
pi = 3.14
r = 7.77

peri = r * 2 * pi
print(peri)
print(r * 2 * pi)

area = r * r * pi
area2 = r ** 2 * pi
print(r ** 2 * pi)
print(area)
print(area2)
print(id(r ** 2 * pi))
print(id(area))
print(id(area2))        #這的記憶體位置就不一樣惹
