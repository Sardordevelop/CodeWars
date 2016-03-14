import random
import string
import time
import numpy

def zfunc2(s):
    z=[len(s)]
    for i,c in enumerate(s):
        x,j=0,0
        while j<len(s) and s[0:j]==s[i:j]:
            j+=1
        z.append(j)
    return z

def zfunc(str_):
	z = []
	z.append(len(str_))
	l,r = 0,1
	for i in xrange(1,len(str_)):
		z.append(0)
		if i >= r:
			off = 0
			while i + off <z[0] and str_[i+off] == str_[off]:
				off += 1
			z[i],l,r = off, i, i + off - 1
		else:
			if z[i-l] < r - i:
				z[i] = z[i-l]
			else:
				off = 0
				while r + off < z[0] and str_[r-i+off] == str_[r+off]:
					off += 1
					z[i],l,r = r - i + off, i, r + off - 1
	return z

x = "a"*100000
N = 100
long_random_str = ''.join(random.choice(string.lowercase) for x in range(N))
#start_time = time.time()
print (zfunc('abracadabra'))
#print(time.time() - start_time)

