#Python program to perform matrix operations
#Addition
mat1 = [[10,9],[8,7]]
mat2 = [[6,5],[4,3]]
mat3 = [[0,0],[0,0]]
for i in range(0,2):
    for j in range(0,2):
       mat3[i][j] = mat1[i][j] + mat2[i][j]
       print("Addition of two matrices")
for i in range(0,2):
  for j in range(0,2):
       print(mat3[i][j], end = "")
       print()

#Multiplication
mat1 = [[10,9],[8,7]]
mat2 = [[6,5],[4,3]]
mat3 = [[0,0],[0,0]]
for i in range(0,2):
    for j in range(0,2):
       mat3[i][j] = mat1[i][j] * mat2[i][j]
       print("Multiplication of two matrices")
for i in range(0,2):
  for j in range(0,2):
       print(mat3[i][j], end = "")
       print()

#Tranpose
X = [[10,9],
    [8,7]]
result = [[0,0],
         [0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
       print("Transpose Of Two Matrices")
for r in result:
   print(r)
