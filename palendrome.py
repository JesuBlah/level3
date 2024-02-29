string = input("Enter a string: ")

if string.lower() == string[::-1].lower():
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
