
text=str(input('enter any string'))

count1=0
count2=0
count3=0
count4=0
for i in range (len(text)):
    if text[i]>='A' and text[i]<='Z':
        count1+=1
    elif text[i]>='a' and text[i]<='z':
        count2+=1
    elif text[i]>='0' and text[i]<='9':
        count3+=1
    else:
        count4+=1
print('number of upper char is {}'.format(count1))
print('number of lower char is {}'.format(count2))
print('number of integer char is {}'.format(count3))    
print('number of special char is {}'.format(count4))
#to check whether the string is in upper case lower case or non char
'''
def check(ch):
    if ch>='A' and ch<='Z':
        print(ch,'is an upper case char')
    elif ch>='a' and ch<='z':
        print(ch,'is a lower case char')
    else:
        print(ch,'is a non char')
ch=str(input('enter char'))
check(ch)        
'''
