def decode_message( s: str, p: str) -> bool:

# write your code here

    
    i, j = 0, 0
    star_idx = -1  
    match_idx = 0  

    while i < len(s):
        if j < len(p) and (p[j] == '?' or s[i] == p[j]):
           
            i += 1
            j += 1
        elif j < len(p) and p[j] == '*':
           
            star_idx = j
            match_idx = i
            j += 1
        elif star_idx != -1:
            
            j = star_idx + 1
            match_idx += 1
            i = match_idx
        else:
            return False

    while j < len(p) and p[j] == '*':
        j += 1

  
    return j == len(p)


print(decode_message("aa", "a"))  
print(decode_message("aa", "*"))  
print(decode_message("cb", "?a"))  
print(decode_message("aa", "a*"))  

  
