def vecMul(a: list, b: list) -> list:
    assert len(a) == 3
    assert len(b) == 3
    c = [0, 0, 0]
    c[2] = a[0] * b[1] - a[1] * b[0]
    c[0] = a[1] * b[2] - a[2] * b[1]
    c[1] = a[2] * b[0] - a[0] * b[2]
    return c

def unitvector(c: list) -> list:
    assert len(c) == 3
    norm = (c[0] ** 2 + c[1] ** 2 + c[2] ** 2) ** 0.5
    if (norm == 0):
        return [0, 0, 0]
    return [c[k] / norm for k in range(3)]

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
            v.append([float(a[1]), float(a[2]), float(a[3])])
        elif (a[0] == "vn"):
            vn.append([float(a[1]), float(a[2]), float(a[3])])
        elif (a[0] == "vt"):
            vt.append([float(a[1]), 1 - float(a[2])])
        elif (a[0] == "f"):
            ar1 = a[1].split('/')
            ar2 = a[2].split('/')
            ar3 = a[3].split('/')
            assert len(ar1) == len(ar2) == len(ar3)
            f.append([int(ar1[0]) - 1, int(ar2[0]) - 1, int(ar3[0]) - 1])
            if (len(ar1) > 1):
                if (ar1[1] != ""):
                    ft.append([int(ar1[1]) - 1, int(ar2[1]) - 1, int(ar3[1]) - 1])
                # computing normals...
                a = [v[f[-1][1]][k] - v[f[-1][0]][k] for k in range(3)]
                b = [v[f[-1][2]][k] - v[f[-1][0]][k] for k in range(3)]
                c = unitvector(vecMul(a, b))
                # this is also crap...
                # we work only with triangles, so 3 points define normals
                # fn.append([int(ar1[2]) - 1, int(ar2[2]) - 1, int(ar3[2]) - 1])
                for _ in range(3):
                    fn.extend(c)
        elif (a[0] in ['o', 'g', "vp", 's', "usemtl", "mtllib"]):
            # ignore this crap
            pass
        else:
            pass
        x = obj.readline()

    # Now we need to make links to vertices unique

    vUsed = set()
    tc = []
    ind = []
    vertex = []
    #TODO vnUsed = set()
    # vtUsed = set() --- it's already ok
    for i in range(len(f)):
        _v = [v[f[i][k]] for k in range(3)]
        for k in range(3):
            ind.append(len(vertex) // 3)
            vertex.extend(_v[k])
    for i in ft:
        for k in range(3):
            tc.extend(vt[i[k]])
    '''print(len(vertex))
    print(*vertex)
    print(*ind)
    print(*tc)'''
    return {
        "v": vertex,
        "vn": vn,
        "vt": vt,
        "f": ind,
        "fn": fn,
        "ft": ft,
        "tc": tc,
    }
