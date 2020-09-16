def validBraces(string):
    validity = True;
    level = 0;
    brackets = [];
    closingBracket = False;
    for c in string:
        if c == "{" or c == "(" or c == "[":
            level += 1;
            brackets.append([c, level]);
        if c == "}" or c == ")" or c == "]":
            closingBracket = True;
            if c == "}": b = "{";
            if c == "]": b = "[";
            if c == ")": b = "(";
            found = False;
            for a in brackets:
                print(a);
                if a[0] == b:
                    found = True;
                    if not int(a[1]) == int(level):
                        found = False;
                    else:
                        found = True;
                        break;
            if found == False: return False;
            level -= 1;
    if closingBracket == False: return False;
    return True;
