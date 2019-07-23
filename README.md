# De-Anza-Python
Programs written during De Anza Python Summer Program

All these basic programs have been writen during Python Summer camp at De Anza College Cupertino

1. Declare variables directly using name = value. You do not have to mention it's type like Java
Eg: name = "John" number = 8

2. Lists to be created using square brackets []
   Lists are mutable
   
   Tuples to be created using parenthesis ()
   tuples are immutable
   
   Dictionaries to be created using {}
   Dictionaries are mutable but have a key and value
   Eg: myDict = {"Gaby":8, "John": 8}
   
3. Create regular functions using def keyword
   Eg: def sum(a, b):
          return a + b
         
   Or create lambda functions which have only 1 statement
   Eg: lambda x:x+x
  
3. maps can easily calculate things in order for you using lists
  
   def sum(a):
       return a+a
       
   list1  = [1, 2,  3, 4, 5]
   result = map(a, list1)
   
4. Random stuff
   import random to get random values from the computer
   Eg: import random
       number = random.randInt(1, 10)
