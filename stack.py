def is_palindrome(s):
    s = s.lower().replace(" ", "")
    stack = list(s)
    for char in s:
        if char != stack.pop():
            return False
    return True

text = input("Enter a string: ")
print("Palindrome" if is_palindrome(text) else "Not a palindrome")
