#print

print("a" + "b")

print("a" * 2)      #將字串印兩次
print("a" + "b" * 3)
print(("a" + "b") * 4)

a = "0123456789"
print(a[3])         #取第3位 (從0開始算)
print(a[0:4:1])     #字串切片從0開始到4結束每次跳1單位
print(a[0:9:2])
print(a[0:len(a):2])
print(a[1:])        #自第一個開始 :預設就是字串長度 : 預設每次跳1單位
print(a[:4])        #預設為第0個開始: 直到4 : 預設每次跳1單位
print(a[:4:1])      #預設:4:1  (結果同上)
print(a[::-1])      #等於反轉字串

b = "Hi nice to meet you.  i'm fine 3Q."
print(b.split())    #split() 括號內的關鍵字作為切割 並匯出成陣列 (沒寫預設為空白)
print(b.split(".")) #最後的.右邊已經沒東西了但還是會給一個空字串
c = b.split()
print(c)
d = "\n".join(c)    #"字串".join(將要被接起來的串列) 並且為字串
print(d)
e = "qq".join(c)
print(e)