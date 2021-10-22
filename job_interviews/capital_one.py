def boundedRatio(a, l, r):
    result = []
    for i, element in enumerate(a):
        satisfies = False
        for x in range(l, r + 1):
            if (i + 1) * x == element:
                satisfies = True
                break
        result.append(satisfies)

    return result

def removeOneDigit(s, t):
    
    result = 0
    for i, char in enumerate(s):
        if not char.isdigit():
            continue
            
        new_string = s[0:i] + s[i+1:len(s)]
        if new_string < t:
            result += 1
            
    for i, char in enumerate(t):
        if not char.isdigit():
            continue
            
        new_string = t[0:i] + t[i+1:len(t)]
        if s < new_string:
            result += 1
        
    return result

def trafficMap(directions):
    previous_direction = -1
    i = 0
    j = 0
    
    if directions[0][0] != 0:
        return False
    
    while i < len(directions) and j < len(directions[0]) and i >= 0 and j >= 0:
        current_direction = directions[i][j]
        if current_direction == 0: 
            if previous_direction == -1 or previous_direction == 0 or previous_direction == 3 or previous_direction == 4:
                j += 1
            else:
                return False
        elif current_direction == 1:
            if (previous_direction == -1 or previous_direction == 2 or previous_direction == 4):
                i += 1
            else:
                return False  
        elif current_direction == 2:
            if (previous_direction == -1 or previous_direction == 0 or previous_direction == 3 or previous_direction == 4):
                i += 1
            else:
                return False
        elif current_direction == 3:
            if (previous_direction == -1 or previous_direction == 1 or previous_direction == 5):
                j += 1
            else:
                return False
        elif current_direction == 4:
            if (previous_direction == -1 or previous_direction == 1 or previous_direction == 2):
                j += 1
            else:
                return False   
        elif current_direction == 5:
            if (previous_direction == -1 or previous_direction == 0 or previous_direction == 3 or previous_direction == 4):
                i -= 1
            else:
                return False
                
        previous_direction = current_direction
    
    if j>len(directions[0]) - 1:
        return True
    return False