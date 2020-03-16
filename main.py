# Напишите сюда домашку.
string = input("enter string: ")
words = {}
for i in set(string.split(" ")):
    if len(i.strip())>0:
        words[i] = (string.split(" ")).count(i)

print(words)
