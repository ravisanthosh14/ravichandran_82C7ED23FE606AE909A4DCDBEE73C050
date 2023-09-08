def recure_fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*recure_fact(n-1)

number = int(input("Enter a value : "))
res = recure_fact(number)

print ("  The Factorial of {} is {}.".format(number,res))