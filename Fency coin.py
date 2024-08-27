import sys
def EOF():
  for i in sys.stdin:
    yield i
print(list(EOF()))
    

            
            
        
