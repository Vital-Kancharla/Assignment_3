#program to perform arthimetic operations(Add,sub,mul,div)
def add(a,b):#Addition block
  return a+b
def sub(a,b):#Subtraction block
  return a-b
def mul(a,b):#Multiplication block
  return a*b
def div(a,b):#Division block
  return a/b
print("\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")  
while True:
  ch=input("\nEnter your prefered arthimetic option from the provided options\n")#Takes the input of prefered option from the user
  if ch in ('1','2','3','4'):
    n1=float(input("Enter value for first number:"))#Taking input for first number
    n2=float(input("Enter value for second number:"))#Taking input for second number
    if(ch=='1'):
      print("The sum of ",n1," and ",n2," is = ",add(n1,n2))
    elif(ch=='2'):
      print("The difference of ",n1," and ",n2," is = ",sub(n1,n2))
    elif(ch=='3'):
      print("The product of ",n1," and ",n2," is = ",mul(n1,n2))
    elif(ch=='4'):
      if(n2==0):
        print("Zero Division Error!!!!\nCannot divide with zero")
      print("The quotient of ",n1," and ",n2," is = ",div(n1,n2))
    another=input("Do you want to perform another calculation?(yes/no):::")
    if (another=="no"):
      break
  else:
    print("Invalid input\nPlease check again.....")