def strocounter(s):# 0(N)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)
strocounter('adgfaaa')

print (31232412424)


print (12312)