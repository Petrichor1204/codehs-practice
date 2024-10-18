counts = dict() 
words = input("Enter a sentence: ")
word_list = words.split()
print(word_list)
for word in word_list:
    counts[word] = counts.get(word, 0) + 1
print("Count:", counts)
for x, y in counts.items():
    print(x, y)
d = {"a": 5, "c" : 12, "b" : 3}
tmp = list()
for (k, v) in d.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse = True)
print(tmp)    