#check if a number is prime or not

num=int(input('enter a number'))
if num==1:
    print('not prime')

for i in range(2,num):
    if num%i==0:
        print('not prime')
    else:
        print('prime')




#
num=int(input('enter a number'))
is_prime=True
if num==1:
    is_prime=False
     
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
    
if is_prime==True:
    print('prime')
else:
    print('not prime')
