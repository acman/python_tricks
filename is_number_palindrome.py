def is_number_palindrome(number):
    assert isinstance(number, int)

    original_number = number
    reversed_number = 0

    if number < 0 or not (number % 10):
        return False

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original_number == reversed_number


for number, result in [
        (10, False),
        (1, True),
        (111, True),
        (121, True),
        (-10, False),
        (123321, True),
        (0, False),
        (4444, True)]:
    assert is_number_palindrome(number) == result
