name = input("Enter your name: ")
print("Name is", name)

sentence = input("Enter a sentence: ")
print("Your sentence is:", sentence)

wordToReplace = input("Enter the word to replace: ")
replacementWord = input("Enter the replacement word: ")

sentence = sentence.replace(wordToReplace, replacementWord)
print("Your sentence is:", sentence)