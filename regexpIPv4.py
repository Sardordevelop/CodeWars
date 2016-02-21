import re
def ipv4_address(address):
    pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    test = pat.match(address)
    return test

print ipv4_address("127.0.1")