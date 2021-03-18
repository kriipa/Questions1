#print mupltiplication table of 5 upto 10

num=int(input('enter the number for multiplication:'))
product=1
for i in range(1 , 11):
    product = num*i
    print(f'the multiplication of {num} is {product}')


num=int(input('enter the number for factorial:'))
product =1
for i in range(1 , num+1):
    product =product * i
print(f'the factorial of {num} is {product}')

num=int(input('enter the number for factorial:'))
product =1
for i in range(num,0 , -1):
    product =product * i
print(f'the factorial of {num} is {product}')


