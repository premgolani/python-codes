'''
str1 ='how'
str2='are'
str3='you'
vowels='aeiou'
for i in str1:
    if i in vowels:
        #print(str1)
for i in str2:
    if i not in vowels:
        str2=str2.replace(i,'%')
        #print(str2)
for i in str3:
    
    str3=str3.upper()
print(str1,str2,str3)
'''
n = int(input('enter the number: '))

a= 0

b= 0

for i in range(1, n+1):

    if(i%2!=0):

       

        a = a+2

    else:      

        b = b+1

if(n%2!=0):

    print('\n{} term of series is {}\t'.format(n,a-2))

else:

    print('\n{} term of series is {}\t'.format(n,b-1))
