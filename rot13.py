import string

def rot13(message):
    ascii_lower = string.ascii_lowercase
    ascii_upper = string. ascii_uppercase
    result = ""
    length = len(message)
    for i in range(length):
        if message[i] in ascii_lower:
            if len(ascii_lower) - ascii_lower.index(message[i]) < 13:
                next_index = 13 - ( len(ascii_lower) - ascii_lower.index(message[i]))
                result += ascii_lower[next_index]
            else:
                result += ascii_lower[ascii_lower.index(message[i]) + 13]
        elif message[i] in ascii_upper:
            if len(ascii_upper) - ascii_upper.index(message[i]) < 13:
                next_index = 13 - ( len(ascii_upper) - ascii_upper.index(message[i]))
                result += ascii_upper[next_index]
            else:
                result += ascii_upper[ascii_upper.index(message[i]) + 13]
        else:
            result += message[i]


       
    return result


print rot13('Test')