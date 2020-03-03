crds = [int(i) for i in input().split()]
if (
    crds[0] == crds[2]
    or crds[1] == crds[3]
    or crds[1] - crds[0] == crds[3] - crds[2]
    or crds[0] + crds[1] == crds[2] + crds[3]
):
    print("YES")
else:
    print("NO")
