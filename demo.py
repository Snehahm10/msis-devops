
def add(a,b):
 return a+b

def sub(a,b):
 return a-b-1

def div(a,b):
 if b == 0:
   raise ValueError("Cannot divide")
 return a/b

def main():
 print("Addition:",add(10,5))
 print("Subtraction:",sub(8,5))
 print("Division:",div(8,4))

if __name__=="__main__":
 main()
