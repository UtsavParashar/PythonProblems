FORM1:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
Code:
n=int(input('Enter a no: '))
for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

FORM2:
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
Code:
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i, end=' ')
    print()

FORM3:
AAAA
BBBB
CCCC
DDDD
EEEE
Code:
a='A'
for i in range(1,n+1):
    print(a*4)
    a=chr(ord(a)+1)

FORM4: Pyramid
     *
    ***
   *****
  *******
 *********
Code:
for i in range(1,n+1):
    print(' '*(n-i), '*'*(2*i-1))

Form 5: Reverse Pyramid:
 ***********
 *********
  *******
   *****
    ***
     *
Code:
for i in range(n+1,0,-1):
    print(' '*(n-i), '*'*(2*i-1))

Form 6: Character pyramid
     A
    BBB
   CCCCC
  DDDDDDD
 EEEEEEEEE
a='A'
for i in range(1, n+1):
    print(' '*(n-i),a*(2*i-1))
    a=chr(ord(a)+1)

Form 7:
*
**
***
****
*****
Code:
for i in range(1,n+1):
    print('*'*i)

Form 8:
     *
    ***
   *****
  *******
 *********
 *********
  *******
   *****
    ***
     *
for i in range(1, n+1):
    print(' '*(n-i),'*'*(2*i-1))
    if i==5:
        for i in range(n,0,-1):
            print(' '*(n-i),'*'*(2*i-1))

Form 9:
*****
****
***
**
*
**
***
****
*****
for i in range(n,0,-1):
    print('*'*i)
    if i==1:
        for i in range(i+1,n+1):
            print('*'*i)