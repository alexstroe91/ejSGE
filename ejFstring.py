import math

num1= 20.3
num2 = 50.3
num3 = 34.9

stringFstring = f'''
{math.sqrt(num1):.2f}
{math.sqrt(num2):.2f}
{math.sqrt(num3):.2f}

SUMA: 
{math.sqrt(num1) + math.sqrt(num2 ) + math.sqrt(num3):.2f}
'''
print(stringFstring)