# 1064
a, b, c = input().split(' ')
d = int(a)
e = int(b)
f = int(c)
print("%d" % (d if d<e else e) if (d if d<e else e)<f else f)