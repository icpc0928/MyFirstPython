#型態轉換
a = 10
print(type(a))              #int
float(a)
print(type(a))              #int
print(type(float(a)))       #float

print(type(1))              #int
print(type(float(1)))       #float

print(int(1.6))             #1
print(float(1))             #1.0
print(int(-1.9))            #-1

print(bool(0))              #false
print(bool(2))              #true
print(bool(-1))             #true

print(int(True))            #1
print(int(False))           #0
print(float(True))

print(str(123))
print(type(str(123)))
a = True
print(str(a) + " 123")

print(str(0o130))            #會先將八進位的130轉為十進位的88 再轉成字串

#print(int("9.1"))           #編譯似乎OK 但會出錯
print(float("9.1"))             #這樣才行
print(bool("3"))            #因為不等於0 所以依然為True
print(bool("HI"))           #只要不是0 轉成bool就會試True