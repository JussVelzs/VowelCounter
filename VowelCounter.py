string = str(input(""))
vowels = 'aeiou'
chars_list = []
for chars in vowels:
    x = string.count(chars)
    chars_list.append(x)
print(sum(chars_list))
