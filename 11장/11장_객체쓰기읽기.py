import	pickle

my_list	= ['this', 'is', 'my', 'list']

with open('my_data.pickle', 'wb') as f:
	pickle.dump(my_list, f)
	
with open('my_data.pickle', 'rb') as f:
	my_list	= pickle.load(f)
    
print(my_list)