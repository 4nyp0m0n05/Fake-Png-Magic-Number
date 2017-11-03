#!/usr/bin/python3
head=bytes.fromhex('89504e470d0a1a0a0000000d494844520000')
end=bytes.fromhex('0000000049454e44ae426082')
with open('a.txt','rb') as file:
    data=file.read()

data1=head+data+end

with open('tmp.png','wb') as file:
    file.write(data1)
