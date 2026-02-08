num = int(input('Enter your number:- '))
temp = num
num_leng = len(str(num))
arm = 0

while num>0:
    digit = num % 10
    arm = arm + (digit ** num_leng)
    num = num // 10
if arm == temp:
    print(arm,'is an armstrong number')
else:
    print(arm,'is not an armstrong number')