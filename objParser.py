class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class texPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class fullPoint:
    def __init__(self, point, texPoint):
        self.v = point
        self.vt = texPoint

class vector(point):
    def __add__(self, a):
        return vector(self.x + a.x, self.y + a.y, self.z + a.z)

    def __mul__(self, a):
        return vector(self.y * a.z - self.z * a.y, self.z * a.x - self.x * a.z, self.x * a.y - self.y * a.x)

    def unitvector(self):
        norm = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        if (norm == 0):
            return vector(0, 0, 0)
        return vector(self.x / norm, self.y / norm, self.z / norm)

def vec(p1, p2):
    return vector(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)

def Int(a):
    try:
        return int(a)
    except:
        return 0

def parseOBJ(objPath: str) -> dict:
    obj = open(objPath)
    vert = [[0, 0, 0]]  #
    tVert = [[0, 0]]    # trush points
    # nVert = [[0, 0, 0]]
    indices = []
    fs = []
    vUsed = []
    vnUsed = []
    
    x = obj.readline()
    while (x):
        a = x.split()
        if (len(a) == 0):
            pass
        elif (a[0] == "v"):
            assert len(a) >= 4
            vert.append(point(float(a[1]), float(a[2]), float(a[3])))
        elif (a[0] == "vt"):
            assert len(a) >= 3
            tVert.append(texPoint(float(a[1]), 1-float(a[2])))
        elif (a[0] == "f"):
            if (len(a) > 4):
                print("objParser: parseOBJ: only triangle faces supported")
                return {}
            f = [list(map(Int, a[i].split('/'))) for i in range(1,4)]
            for i in range(3):
                if (len(f[i]) < 3):
                    f[i].extend([0] * (3 - len(f[i])))
            indices.append([])
            normal = (vec(vert[f[0][0]], vert[f[1][0]]) * vec(vert[f[0][0]], vert[f[2][0]])).unitvector()
            for i in range(3):
                tmpPoint = fullPoint(vert[f[i][0]], tVert[f[i][1]])
                if (tmpPoint in vUsed):
                    indices[-1].append(vUsed.find(tmpPoint))
                else:
                    indices[-1].append(len(vUsed))
                    vUsed.append(tmpPoint)
                    vnUsed.append(normal)
        elif (a[0] in ["g", "o", "s", "vp", "vn", "usemtl", "mtllib"]):
            # ignore this crap
            pass
        else:
            # something strange
            # probably a typo
            # just ignore this
            pass
        x = obj.readline()

    ans = dict()
    ans["v"] = []
    ans["tc"] = []
    ans["fn"] = [] # this has to be vn, but...
    ans["f"] = []
    for i in vUsed:
        ans["v"].extend([i.v.x, i.v.y, i.v.z])
        ans["tc"].extend([i.vt.x, i.vt.y])
    for i in vnUsed:
        ans["fn"].extend([i.x, i.y, i.z])
    for i in indices:
        ans["f"].extend([i[k] for k in range(3)])
    #print("v:", *ans["v"])
    #print("f:", *ans["f"])
    #print("tc:", *ans["tc"])
    #print("fn:", *ans["fn#"])
    return ans
