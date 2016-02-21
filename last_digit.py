def last_digit(n1, n2):
    res = n1%10
    mod_ = n2%4
    table = [[0,0,0,0],
            [1,1,1,1],   
            [2,4,8,6],   
            [3,9,7,1],   
            [4,6,4,6],   
            [5,5,5,5],   
            [6,6,6,6],   
            [7,9,3,1],   
            [8,4,2,6],   
            [9,1,9,1]]  
    
    return table[res][mod_-1]


print last_digit(4, 1)