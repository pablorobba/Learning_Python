citys = ["Rome","BsAs","Sao Paulo","Brasilia","Paris","The Cairo"]

citys [2] ="Athens"
citys.append ("New York")
citys.insert(0,"Berlin")
del citys[4]

popped_citys = citys.pop()
print(popped_citys)

citys.remove("Rome")
print(sorted(citys)[0])

print(sorted(citys))
citys.reverse
print(citys)

citys.sort()

print(citys)

len_citys = len(citys)
print(len_citys)