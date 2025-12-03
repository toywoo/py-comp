import pickle

f=open('data.bin', 'wb')

numbers=[1,2,3,4,5]
strings=['Hello', 'world']

pickle.dump(32, f)
pickle.dump(numbers, f)
pickle.dump(strings, f)

f=open('data.bin', 'rb')
num=pickle.load(f)
numbers=pickle.load(f)
strings=pickle.load(f)

print(num)
print(numbers)
print(strings)

f.close()