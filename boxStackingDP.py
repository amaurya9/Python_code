class Box:
    def __init__(self,h,w,d):
        self.h = h
        self.w = w
        self.d = d

def max_hight(arr,n):
    rot = [Box(0,0,0) for _ in range(3*n)]
    i = 0
    index = 0
    while i < 3*n:
        rot[i].h = arr[index].h
        rot[i].w = max(arr[index].w,arr[index].d)
        rot[i].d = min(arr[index].w, arr[index].d)
        i += 1

        rot[i].h = arr[index].w
        rot[i].w = max(arr[index].h, arr[index].d)
        rot[i].d = min(arr[index].h, arr[index].d)
        i += 1

        rot[i].h = arr[index].d
        rot[i].w = max(arr[index].h, arr[index].w)
        rot[i].d = min(arr[index].h, arr[index].w)
        i += 1
        index += 1

    rot = sorted(rot, key=lambda x:x.w*x.d, reverse=True)

    max_h = []
    for i in range(3*n):
        max_h.append(rot[i].h)

    result = [i for i in range(3*n)]

    for i in range(3*n):
        for j in range(i):
            if rot[i].w < rot[j].w and rot[i].d < rot[j].d:
                if max_h[i] < max_h[j]+rot[i].h:
                    max_h[i] = max_h[j]+rot[i].h
                    result[i] = j
    mx_value = -1

    for i in range(3*n):
        if mx_value < max_h[i]:
            mx_value = max_h[i]
            index = i

    while index > 0:
        print(rot[index].w,rot[index].d,rot[index].h)
        index = result[index]

    return mx_value

if __name__ == "__main__":
    arr = [Box(4, 6, 7), Box(1, 2, 3), Box(4, 5, 6), Box(10, 12, 32)]
    n = len(arr)
    print("max hight of boxes is :",max_hight(arr,n))