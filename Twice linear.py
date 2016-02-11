def dbl_linear(n):
    set_ = list()
    x = 1
    index = 0
    set_.append(x)
    while len(set_) <= n:
    	tmp_set_ = set_
    	for x in set_:
    		tmp_set_.append(2*x+1)
    		tmp_set_.append(3*x+1)
    	set_ = tmp_set_
    set_.sort()
    return set_

print(dbl_linear(10)[10])

 