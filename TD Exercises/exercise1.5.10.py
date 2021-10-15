def palindrome(x):
    if x == x[::-1]:
        isPalindrome = True
    else:
        isPalindrome = False 

    return isPalindrome

x = input("Give a word: ")
print(palindrome(x))