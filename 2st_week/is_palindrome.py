input = "abcba"


def is_palindrome(string):
    chars = list(string)
    left = 0
    right = len(chars) - 1

    while left < right:
        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1

    return True


print(is_palindrome(input))
