
def add(a,b):
 return a+b

def sub(a,b):
 return a-b

def div(a,b):
 if b==0:
   raise ValueError("Cannot divide by zero")
 return a/b

def main():
 print("Addition:",add(10,5))
 print("Subtraction:",sub(8,5))
 print("Division:",div(10,2))

if __name__=="__main__":
 main()
