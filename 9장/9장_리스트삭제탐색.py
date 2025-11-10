myList = ["우유", "사과", "두부", "소고기"]

if "소고기" in myList:
    i =	myList.index( "소고기")
    print(i)
                                
if "소고기" in myList:
    myList.remove("소고기")
print(myList)

item = myList.pop(0)
print(myList)
print(item)

item = myList.clear()
print(myList)