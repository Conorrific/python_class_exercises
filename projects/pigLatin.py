#inputs I puts in and I takes out. takes your name and says hi.
name = input("what is your name? ")
print('Welcome to the Pig Latin Translator ' + name + "!")
#separate
pyg = "ay"
original = input("Enter a word: ")
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = original + first + pyg
    new_word = new_word[1:len(new_word)]
    print(new_word)
else:
  print("empty")





