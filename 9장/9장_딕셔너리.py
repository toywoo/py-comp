phone_book = {}
phone_book["홍길동"] = '1234'
phone_book["이순신"] = '1235'
phone_book["강감찬"] = "1236"

print(phone_book)

value = phone_book.get("홍길동", "Not Found")
print(value)

print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())

for person, score in phone_book.items():
    print(person, "=", score)

for key in sorted(phone_book.keys()):
    print(key, phone_book[key])

if "한사랑" not in phone_book:
    phone_book["한사랑"] = "1237"

print(phone_book)

phone_book.pop("홍길동")
print(phone_book)

del phone_book["이순신"]
print(phone_book)

phone_book.clear()
print(phone_book)