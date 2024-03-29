import hashlib

def sha256(data):
    data=bytes(data,'utf-8')
    sha=hashlib.sha256()
    sha.update(data)
    return sha.hexdigest()


# s='harish gupta'
# print(sha256(s))


