#ask for three tests scores and finds their average
total = 0
for i in range(3):
    score = int(input("Enter your score: "))
    total += score
average = total/3
print("The average of your scores is ", average)    
    