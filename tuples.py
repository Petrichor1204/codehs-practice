def solution(numbers):
    n = len(numbers)
    num_list = []
    for i in range(n):
        num_list.append((numbers[i], numbers[n - i - 1]))
    return(num_list)        
how_many = int(input("How many numbers do you want to enter?: "))
numbers = []
for i in range(how_many):
    number = int(input("Enter a number: "))
    numbers.append(number)
done = solution(numbers)
print(done)