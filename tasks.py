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


