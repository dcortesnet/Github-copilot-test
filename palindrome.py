def is_palindrome(string):
    # Remove any whitespace and convert to lowercase
    string = string.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return string == string[::-1]