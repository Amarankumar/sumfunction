
def sum_numbers(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum
numbers =list(map(int,input("Enter a number:").split())) # [8, 2, 3, 0, 7]
result=sum_numbers(numbers)
print('sum of the given numbers is :',result)

# output;
# Enter a number:1 2 3
# sum of the given numbers is : 6
