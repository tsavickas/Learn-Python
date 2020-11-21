def disemvowel(string):
    vowels = ['a', 'o', 'i', 'u', 'e']
    string = ''.join(item for item in string if item.lower() not in vowels)
    return string

# Test
assert disemvowel('Today is sunny Sunday!') == 'Tdy s snny Sndy!'