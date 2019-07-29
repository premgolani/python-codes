"""#the below code will give the sum of odd nos in the given range
num=int(input('enter number'))
oddtotal=0
for i in range (1,num):
    if(i%2!=0):
         print("{0}".format(i)) #to display the odd no's in the range
         sumtotal=sumtotal+i
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(i, sumtotal))
"""

#the below code will give the sum of even nos in the given range:
num =int(input("enter the number"))
eventotal=0
for i in range(1,num+1):
    if(i%2==0):
        eventotal=eventotal+i
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(i, eventotal))
    
               





