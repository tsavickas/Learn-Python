sentence = "This is a common interview question"
char_dict = {}

for char in sentence:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1

char_dict_sorted = sorted(
    char_dict.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_dict_sorted[0])
