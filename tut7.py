# def add(a, b):
#     s = a+b 
#     return s 
# print(add(4,6))  

# add = lambda x,y:x>y
# print(add(4,12))  


a = [(1,2), (4,5), (555,34)] 
a.sort(key=lambda x:x[1]) 

print(a) 