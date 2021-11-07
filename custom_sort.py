import numpy as np
from functools import cmp_to_key
            
def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                    distance[row][col-1] + 1,          # Cost of insertions
                                    distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return (distance[row][col])
    
def hamming_distance(w1: str, w2: str) -> int:
    return sum(1 for k in range(6) if w1[k] != w2[k])

def editDistanceRec(str1, str2, m, n):
    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m-1] == str2[n-1]:
        return editDistanceRec(str1, str2, m-1, n-1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(editDistanceRec(str1, str2, m, n-1),    # Insert
                    editDistanceRec(str1, str2, m-1, n),    # Remove
                    editDistanceRec(str1, str2, m-1, n-1)    # Replace
                    )
def editDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    return editDistanceRec(str1, str2, m, n)

def edit_distance(word, string_to_take_distance_with = "someString"):
    '''
    Description:
        give you the edit distance between 2 words
        word                            : String 1 (dynamic) 
        string_to_take_distance_with    : String 2 (static)

    '''


    length_of_string  = len(word)+1
    length_of_string2 = len(string_to_take_distance_with)+1

    tbl = {}
    for i in range(length_of_string): tbl[i,0]=i
    for j in range(length_of_string2): tbl[0,j]=j
    for i in range(1, length_of_string):
        for j in range(1, length_of_string2):
            cost = 0 if word[i-1] == string_to_take_distance_with[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]

wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
letter_cmp_key = cmp_to_key(levenshtein_ratio_and_distance)
wordlist.sort(key=edit_distance)
print(wordlist)