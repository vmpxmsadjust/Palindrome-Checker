import string

def is_palindrome(s):
    # Remove punctuation and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is the same forwards and backwards
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_str = input("Enter a string: ")
    if is_palindrome(test_str):
        print("Palindrome!")
    else:
        print("Not a palindrome.")
