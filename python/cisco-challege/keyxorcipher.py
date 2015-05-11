


key = raw_input()
keyl = len(key)
cipher = raw_input()
message = ''
j = 0
for i in range(0,len(cipher),2):
    m = ord(key[j]) ^ ord(cipher[i:i+2].decode('hex'))
    message = message + chr(m)
    j = (j+1)%keyl
    
print message