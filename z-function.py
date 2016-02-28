def zfunc(str_):
	z = []
	if len(str_) == 0:
		return z
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

print zfunc('')