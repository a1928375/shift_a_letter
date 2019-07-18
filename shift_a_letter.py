def shift(letter):
    if ord(letter)==90:
        return "A"
    if ord(letter)==122:
        return "a"
    else:
        return chr(ord(letter)+1)

print shift('a')

print shift('n')

print shift('z')
