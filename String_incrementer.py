# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# 000000042153909 -> 000000042153910
# Attention: If the number has leading zeros the amount of digits should be considered.


def increment_string(strng):
    result = ''
    num = ''
    i = len(strng) - 1
    while i >= 0:
        c = strng[i]
        if not c.isdigit():
            break
        num = c + num
        i -= 1
    if num == '':
        strng = strng + '1'
        return strng
    x = int(num)
    x += 1
    result += strng[0: i + 1]
    if len(num) > len(str(x)):
        result += '0'*(len(num) - len(str(x)))
    result += str(x)
    return result