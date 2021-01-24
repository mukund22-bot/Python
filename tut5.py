list_1 = [1,32,4,5,45,4,4,3,3,5,6,7,343] 

divide_by_3 = [] 
for item in list_1:
    if item%3 == 0:
        divide_by_3.append(item) 

print('Without using list comprehensions', divide_by_3) 
print('Using List comprehensions', [item for item in list_1 if item%3==0]) 

dict1 = {'a':45, 'b':65, 'A':5} 
print({k.lower():dict1.get(k.lower(), 0)+dict1.get(k.upper(), 0) for  k in dict1.keys()}) 


squared = {x**2 for x in [1,2,3,4,4,5,5,5,1]}
print(squared) 


gen = (i for i in range(56) if i%3==0) 
for item in gen:
    print(item)  