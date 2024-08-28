from bitarray import bitarray
import hashlib

def hash1(item):
    return int(hashlib.md5(item.encode()).hexdigest(),16) % sizeOfBitArray

def hash2(item):
    return int(hashlib.sha1(item.encode()).hexdigest(),16) % sizeOfBitArray

def hash3(item):
    return int(hashlib.sha256(item.encode()).hexdigest(),16) % sizeOfBitArray

def hash4(item):
    return int(hashlib.sha224(item.encode()).hexdigest(),16) % sizeOfBitArray

    
def addToBloom(item):
    indices = [hash1(item),hash2(item),hash3(item),hash4(item)]
    for index in indices:
        bitArray[index] = 1
def checkMembership(item):
    indices = [hash1(item),hash2(item),hash3(item),hash4(item)]
    for index in indices:
        if bitArray[index] == 0:
            return False
    return True
    
sizeOfBitArray = 1000
bitArray = bitarray(sizeOfBitArray)
bitArray.setall(0)
addToBloom("pizza")
result = checkMembership("pie")
if(result):
    print("Yes, It is present.")
else:
    print("No, It isn't present.")

