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

def parseObject(objPath: str) -> dict:
    obj = open(objPath)
    vert = []
    tVert = []
    nVert = []
    indices = []
    
    x = obj.readline()
    while (x):
        a = x.split()
        if (len(a) == 0):
            pass
        elif (a[0] == "v"):
            assert len(a) >= 4
            vert.append(point(a[1], a[2], a[3]))
        elif (a[0] == "vt"):
            assert len(a) >= 3
            tVert.append(texPoint(a[1], a[2]))
        elif (a[0] == "f"):
            if (len(a) > 4):
                print("objParser: parseObject: only triangle faces supported")
                return {}
            f = []
            f.append()
            indices.append([])
        elif (a[0] in ["g", "o", "s", "vp", "vn", "usemtl", "mtllib"]):
            # ignore this crap
            pass
        else:
            # something strange
            # probably a typo
            pass
        x = obj.readline()
