def function_1(*args): 
    print(type(args)) 
    if(len(args) ==3):
        print("The name of the student is ",args[0], "and age is ",args[1], "and rollno is ",args[2]) 
    else:
        print("The name of the student is", args[0], "and age is", args[1])  


def printmarks(**kwargs):
    print(type(kwargs)) 
    for key, value in kwargs.items(): 
        print(key, value) 

def master(normal, *args, **kwargs): 
    print(normal)
    for i in args:
        print(i) 
    for key, value in kwargs.items(): 
        print(key, value) 


lis = ["mukund", 22, 7656] 

marklist = {"Harry":100, "mukund":100, "aman":76, "rajan":48, "dev":38}  

# printmarks(**marklist) 

(master("normal args", *lis, **marklist))

# function_1(*lis)   