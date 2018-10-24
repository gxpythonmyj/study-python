a1 = 5<9 #真
a2 = 5>9 #假
b1 = 6<10 #真
b2 = 6>10 #假
#and  的含义是先看and前面的内容是真还是假，是真再去看and后面的真假并以后面真或假为最终结果，如果and前面就是假那后面就不用看了结果肯定是假了。
c1 = a1 and b1
print(c1)
c2 =a1 and b2
print(c2)
c3 =a2 and b1
print(c3)
c4 =a2 and b2
print(c4)
print('* '*20)
# or　的含义先看or前面的内容是真还是假，是真那最终结果就是真不用再看or后面，如果or前面是假那再看or后面,并以后面真或假为最终结果.
c5 = a1 or b1
print(c5)
c6 = a1 or b2
print(c6)
c7 = a2 or b1
print(c7)
c8 = a2 or b2
print(c8)
#not 把真的说成不是真的是假，把假的说成是假的是真的。
print('* '*20)
c9 = not(a1)
print(c9)
c10 = not(a2)
print(c10)
print('* '*20)




