def parseOBJ(objPath: str) -> dict:
    obj = open(objPath)
    v = []
    vn = []
    vt = []
    f = []
    fn = []
    ft = []
    x = obj.readline()
    while (x):
        a = x.split()
        if (len(a) == 0):
            x = obj.readline()
            continue
        if (a[0] == 'v'):
            v.extend([float(a[1]), float(a[2]), float(a[3])])
        elif (a[0] == "vn"):
            vn.extend([float(a[1]), float(a[2]), float(a[3])])
        elif (a[0] == "vt"):
            vt.extend([1.0 - float(a[1]), 1.0 - float(a[2])])
        elif (a[0] == "f"):
            ar1 = a[1].split('/')
            ar2 = a[2].split('/')
            ar3 = a[3].split('/')
            assert len(ar1) == len(ar2) == len(ar3)
            f.extend([int(ar1[0]) - 1, int(ar2[0]) - 1, int(ar3[0]) - 1])
            if (len(ar1) > 1):
                if (ar1[1] != ""):
                    ft.extend([int(ar1[1]) - 1, int(ar2[1]) - 1, int(ar3[1]) - 1])
                if (len(ar1) > 2):
                    fn.extend([int(ar1[2]) - 1, int(ar2[2]) - 1, int(ar3[2]) - 1])
        elif (a[0] in ['o', 'g', "vp", 's', "usemtl", "mtllib"]):
            # ignore this crap
            pass
        else:
            pass
        x = obj.readline()
    # Now we need to make links to vertices unique

    vUsed = set()
    tc = []
    #TODO vnUsed = set()
    # vtUsed = set() --- it's already ok
    for i in range(len(f)):
        vCoords = [v[3 * f[i]], v[3 * f[i] + 1], v[3 * f[i] + 2]]
        if (ft != []):
            tCoords = [vt[2 * ft[i]], vt[2 * ft[i] + 1]]
        if (f[i] in vUsed):
            v.extend(vCoords)
            f[i] = len(v) // 3 - 1
        else:
            vUsed.add(f[i])
        if (ft != []):
            tc.extend(tCoords)
    # print(*tc)
    return {
        "v": v,
        "vn": vn,
        "vt": vt,
        "f": f,
        "fn": fn,
        "ft": ft,
        "tc": tc,
    }
