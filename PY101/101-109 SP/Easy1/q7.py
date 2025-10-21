def short_long_short(string1, string2):
    string1_length = len(string1)
    string2_length = len(string2)

    if string1_length < string2_length:
        return string1 + string2 + string1
    else:
        return string2 + string1 + string2
    
    # These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")