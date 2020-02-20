All=list(range(2,101))
for n in range(2,51):
    an=2*n
    bn=3*n
    cn=5*n
    dn=7*n
    for e in All:
        if an==e:
            All.remove(an)
        if bn==e:
            All.remove(bn)
        if cn==e:
            All.remove(cn)
        if dn==e:
            All.remove(dn)
print(All)
