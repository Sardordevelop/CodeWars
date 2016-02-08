def base64_to_base10(str_):
	alpabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
	length = len(str_)
	base_10 = 0
	for i in reversed(range(length)):
		base_10 += alpabet.index(str_[length-i-1])*(64**i)
	return base_10



print(base64_to_base10('BB'))