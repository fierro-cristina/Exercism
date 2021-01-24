def is_isogram(string):
    if string == "":
        return True
    
    string_lower = string.lower()

    for i in string_lower:
        repeats = 0
        for j in string_lower:
            if i == j and j.isalpha():
                repeats += 1
        if repeats > 1:
            return False    
    
    return True