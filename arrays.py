def solution(numbers):
    # TODO: Implement solution here
    n = len(numbers)
    array_list = []
    for i in range((n+1)//2):
        add = numbers[i] + numbers[n-i-1] 
        array_list.append(add)
    return array_list     
numbers = [1, 2, 3, 4, 5]
print(solution(numbers))