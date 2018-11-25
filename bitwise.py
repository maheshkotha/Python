# & ==> If both bits are 1 then only result is 1 otherwise result is 0
# | ==> If atleast one bit is 1 then result is 1 otherwise result is 0
# ^ ==>If bits are different then only result is 1 otherwise result is 0
# ~ ==>bitwise complement operator
# 1==>0 & 0==>1
# << ==>Bitwise Left shift
# >> ==>Bitwise Right Shift

print(~20)
a , b = 1, 7
print(a,b)

a = a^b
b = a^b
a = a^b

print(a,b)


