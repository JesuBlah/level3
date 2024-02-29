sentence = input("Enter a sentence: ")
words = sentence.split()
words.sort()
print("Words in alphabetic order:", ' '.join(words))