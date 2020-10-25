# List

# 宣告方式
lt = []
llt = list()
print(lt, llt)

lt = ["hi", "how", "old", "are", "you?"]
print(lt)
lt = " ".join(lt)  # join 會接在各元素中間 轉成字串
print(lt)
lt = lt.split();  # 字串切割(預設空白) 轉 list
print(lt)

llt = list("apple pen")  # 將字串每個字元單一分成list
print(llt)
print(len(llt))

llt.append("hi")        # 串列後增加元素
print(llt)
llt.extend(lt)          # 在後面擴展串列
print(llt)
llt.insert(1, "p")      # 插入元素放到第index個,其餘向後
print(llt)
del llt[0]              # 刪除第index個元素
print(llt)
llt.remove("hi")        # 刪除第一個此元素只會刪除遇到的第一個
llt.remove("p")
print(llt)
print(llt.index("e"))   # indexOf 回傳該元素的索引值 (找到的第一個)
print("how" in llt)     # 這個值是否含在這個list的元素當中 回傳bool
print(llt.count("p"))   # 此元素出現過幾次

lt2 = sorted(llt)       # 產生新串列並由小排到大 但llt並不會受到影響
print(lt2)
print(llt)
print(id(lt2))
print(id(llt))          # 占用不同記憶體

llt.sort()              # 自行排序
print(llt)

llt1 = llt              # llt1~llt4 都是複製 llt的所有元素 並產生新的list 只有llt1記憶體位置共用 其餘都是新的
llt2 = llt.copy()
llt3 = list(llt)
llt4 = llt[:]
print(str(id(llt)) + " " + str(id(llt1)) + " " + str(id(llt2)) + " " + str(id(llt3)) + " " + str(id(llt4)))



