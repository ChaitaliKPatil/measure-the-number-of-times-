l=[1,3,5,7,2,4,6,8,2,5,1,6,6,3,7,9,2,6,8,4,6,3,7,9,10,3,1,1,1]
def measure(li):
    di={}
    for num in li:
        di[num]=li.count(num)
    sdi=sorted(di.items())
    sdi.reverse()
    maxm=max(di.values())
    print(maxm)
    array_a=[]
    for x in di.keys():
        if di[x]==maxm:
            a=x
            array_a.append(a)
    print(array_a)
    return dict(sdi)
print(measure(l))