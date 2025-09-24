nums = [1,2,3,4,5,6,7,8,9,10]
squares = [n * n for n in nums]
even_squares = [n * n for n in nums if n % 2 == 0]

words = ["apple", "banana", "kiwi"]
word_lengths = [len(w) for w in words]

print("Squares:", squares)
print("Even Squares:", even_squares)
print("Word Lengths:", word_lengths)