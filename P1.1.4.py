Python 3.9.0a1 (v3.9.0a1:fd757083df, Nov 19 2019, 10:51:29) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>> transposed = []
>>> for i in range(4):
	transposed.append([row[i] for row in matrix])

	
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>> transposed = []
>>> for i in range(4):
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])
		transposed.append(transposed_row)

		
>>> transposed
[[1, 5, 9], [1, 5, 9], [1, 5, 9], [2, 6, 10], [2, 6, 10], [2, 6, 10], [3, 7, 11], [3, 7, 11], [3, 7, 11], [4, 8, 12], [4, 8, 12], [4, 8, 12]]
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
>>> 