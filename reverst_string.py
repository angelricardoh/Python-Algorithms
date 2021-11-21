sentence = 'hola mundo'
n = len(sentence)
result = ''
for i in reversed(range(n)):
# for i in range(n - 1, -1, -1):
    result += sentence[i]
print(result)