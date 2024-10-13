#this code displays the various combinations when 2 dice are rolled
# a dice can be rolled 6 times for all the sides to show. 
#the code will iterate through the first dice 6 times and the second 
#one 6 times at the same time.

for i in range(7):
    if i > 0:
        for j in range(7):
            if j > 0:
                print(i, ",", j)
for i in range(3):
    category = input("Enter a category: ")
    something_string = ""
    for i in range(3):
        something = input("Enter something in that category: ")
        something_string += something + " "
    print(f"{category}: {something_string}")