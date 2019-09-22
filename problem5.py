sentence = input("Enter a sentence: ")
s = sentence.split()
s = s[ : :-1]
final = ' '.join(s).capitalize()

print(final)