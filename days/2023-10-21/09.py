b = bin(int(input()))[2:]

print(b)

print(b.count('1'))

print(sum([int(smb) for smb in b]))

print([smb for smb in b if smb == '1'])
print(len([smb for smb in b if smb == '1']))
