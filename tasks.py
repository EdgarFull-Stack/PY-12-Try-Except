# Task 1
def dalinti(a:(int, float),b:(int, float)) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return 'Dalyba iš nulio negalima.'

print(dalinti(10,2))
print(dalinti(5,0))
print(dalinti(8,4))
print('----------------------------------------------')
# Task 2
input1 = input('Put integer: ')
input2 = input('Put second integer: ')

try:
    first_numb = int(input1)
    second_numb = int(input2)
    res = first_numb / second_numb
    print(f'Your result is: {res}')
except ZeroDivisionError:
    print('Change 0 to another integer')
except ValueError:
    print('Use numbers')
print('----------------------------------------------')
# Task 3
input3 = input('Put number: ')

try:
    int_number = int(input3)
    print('Accepted number', int_number)
except ValueError:
    print('Try to put integer')
else:
    print(f'Conversion is done: {int_number}')
finally:
    print('Program finished')
print('----------------------------------------------')
#  Task 4
def check_age(num: int, ) -> int:
    if (num<0):
        raise ('Age must be more than 0')
    if (num>= 18):
        return ('User legal age')
    if (num<18):
        return ('User under legal age')
# print(check_age(-5))
print(check_age(15))
print(check_age(21))

