from timeit import Timer
code1 = """\
i,j = 1,0
while i < 10001 :
    j += i
    i += 1
"""

t1 = Timer (stmt=code1)
print ("while:", t1.timeit (number=10000))
