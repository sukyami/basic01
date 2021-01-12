num = input("Enter an integer number : ")
if type (num) != int:
    print("wrong input...BYE!")

def sumOfIntegers(num):
  sum = 0 
  for i in range(0,num+1):
    sum = i + sum 
  print(sum)

sumOfIntegers(num)