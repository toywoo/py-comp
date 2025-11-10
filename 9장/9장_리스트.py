myList = []
myList.append("우유")
myList.append("사과")
print(myList)

myList.extend(["두부", "소고기"])
print(myList)

myList.insert(0, "고등어")
print(myList)

myList.remove("소고기")
print(myList)

del myList[1]
print(myList)