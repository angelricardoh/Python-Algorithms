#!/bin/python3

# [bread, milk, cereal, juice, vegetables]

# [bread, milk]
# [cereal, anything, vegetables] 

#
# Complete the 'foo' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY codeList
#  2. STRING_ARRAY shoppingCart
#

def foo(codeList, shoppingCart):
    # Write your code here
    
    for code in codeList:
        code_words = code.split(" ")
        for i in range(0, len(shoppingCart) - len(code_words)):
            sameCodeList = True
            for j in range(0, len(code_words)):
                if code_words[j] != shoppingCart[i + j]:
                    sameCodeList = False
            if sameCodeList == True:
                return 1
    return 0


# Problem 2

# query:
# ‘mouse’
# Repository
# [‘mouse, mousepad, moron, moral’]

# [‘mouse, mousepad, moron’]
# [‘mouse, mousepad’]
# [‘mouse, mousepad’]
# [‘mouse, mousepad’]

def searchSuggestions(repository, customerQuery):
    # Write your code here
    suggestionListTyped = []
    for i in range(2, len(customerQuery) + 1):
        suggestionList = []
        for word in repository:
            if word[0:i] == customerQuery[0:i]:
                suggestionList.append(word.lower())
        sortedList = suggestionList.sort()
        if len(suggestionList) >= 3:
            suggestionList = suggestionList[0:3]
        suggestionListTyped.append(suggestionList)
    return suggestionListTyped
