###1. For given input A5B7D3 output should be sorted alphabets and then sorted numbers like
A5B7D3 should return ABD357

s='A5B7D2'
s1=s2=output=''
for i in s:
    if i.isalpha():
        s1+=i
    if i.isdigit():
        s2+=i
for i in sorted(s1):
    output+=i
for i in sorted(s2):
    output+=i
print(output)

###2. WAP where input=A3B5D2 output=AAABBBBBDD
s='A5B7D2'
output=''
for i in s:
    if i.isalpha():
        output+=i
        previous=i
    if i.isdigit():
        output+=previous*(int(i)-1)
print(output)

###3. WAP where input=A5B7D2, output=AFBIDF
s='A5B7D2'
output=''
for i in s:
    if i.isalpha():
        output+=i
        previous=i
    if i.isdigit():
        output+=chr(ord(previous)+int(i))
print(output)

###4. WAP where input=AAABBCCEEDD output=A3B2C2E2D2
s='AAABBCCEEDD'
out=''
prev=s[0]
count=counter=0
for i in s:
    counter+=1
    if i==prev:
        count+=1
        if counter==len(s):
            out=out+prev+str(count)
    else:
        out=out+prev+str(count)
        count=1
        prev=i
print(out)
