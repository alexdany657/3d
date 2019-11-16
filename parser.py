def parseOBJ(objPath: str) -> dict:
    obj = open(objPath)
    v = []
    vn = []
    vt = []
    f = []
    fn = []
    _ft = []
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
            vt.extend([float(a[1]), float(a[2])])
        elif (a[0] == "f"):
            ar1 = a[1].split('/')
            ar2 = a[2].split('/')
            ar3 = a[3].split('/')
            f.extend([int(ar1[0]) - 1, int(ar2[0]) - 1, int(ar3[0]) - 1])
            if (len(ar1) > 1):
                if (ar1[1] != ""):
                    _ft.extend([int(ar1[1]) - 1, int(ar2[1]) - 1, int(ar3[1]) - 1])
                if (len(ar1) > 2):
                    fn.extend([int(ar1[2]) - 1, int(ar2[2]) - 1, int(ar3[2]) - 1])
        elif (a[0] in ['o', 'g', "vp", 's', "usemtl", "mtllib"]):
            # ignore this crap
            pass
        else:
            pass
        x = obj.readline()
    ft = []
    for i in _ft:
        ft.append(vt[_ft])
    return {
        "v": v,
        "vn": vn,
        "vt": vt,
        "f": f,
        "fn": fn,
        "ft": ft,
    }