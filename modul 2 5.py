
is_matrix =  True
def get_matrix(n = int()  , m = int(), value = int()):
    matrix = []
    for i in range(1, n+1):
        matrix_1 = []
        for j in range(1, m+1):
            matrix_1 = [value]
            matrix = [matrix_1 * m] * n
    return matrix
    

result_1 = get_matrix(2 , 2, 10)
result_2 = get_matrix(3, 5 , 42)
result_3 = get_matrix( 4, 2, 13)
print(result_1)
print(result_2)
print(result_3)


            



    















