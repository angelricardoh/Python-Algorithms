# Grayscale code challenge. Find largest path between numbers with a difference of 1

m = 4
n = 4

# mat = [[1, 2, 9, 10],
#                      [5, 3, 8, 11],
#                      [4, 6, 7, 13],
#                      [17,16,15,14]]

mat = [[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13,14,15,16]]

def find_path(local_path, longest_path, i, j):
	if not i + 1 > n - 1 and mat[i+1][j] == mat[i][j] + 1:
		local_path.append(mat[i+1][j])
		find_path(local_path, longest_path, i + 1, j)

	if not i - 1 < 0 and mat[i-1][j] == mat[i][j] + 1:
		local_path.append(mat[i-1][j])
		find_path(local_path, longest_path, i - 1, j)

	if not j - 1 < 0 and mat[i][j-1] == mat[i][j] + 1:
		local_path.append(mat[i][j-1])
		find_path(local_path, longest_path, i, j-1)

	if not j + 1 > m - 1 and mat[i][j+1] == mat[i][j] + 1:
		local_path.append(mat[i][j+1])
		find_path(local_path, longest_path, i, j+1)

	if len(local_path) > len(longest_path):
		longest_path = local_path

	return longest_path

if __name__ == '__main__':
	longest_path = []

	current_path = []
	for i in range(0, n):
		for j in range(0, m):
			current_path = []
			current_path.append(mat[i][j])
			longest_path = find_path(current_path, longest_path, i, j)
	
	print(len(longest_path))
	print(longest_path)
