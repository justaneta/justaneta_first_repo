num1=int(input('Enter first num'))
num2=int(input('Enter second num'))

if num1<num2:
    print(True)
    print('first number less than second number')
elif num1>num2:
    print(False)
    print('first number more than second number')
else:
    print("Equal")