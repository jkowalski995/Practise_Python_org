text = input("Please write a string: ")

for i in text:
    text_r = text[::-1]

if text == text_r:
    print("Yes, it's a palindrome!")
else:
    print("Sorry, it's not a palindrome...")