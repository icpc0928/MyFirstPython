# tuple 固定長度固定元素的串列
tpl = ("1", "2", "3", "4", 5)
print(tpl)
print(tpl[1])

a, b, c, d, e = tpl   # 將tpl的所有元素一一給到每個變數內(變數數量與元素數量一樣)

print(a)
print(c)

# tuple 因為不能修改的特性 所以不能有append/ extend的方法
# 好處是占用較少 元素不會任意更動