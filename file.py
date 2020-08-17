
def add_in_list(id):
    p = open("IdList.txt", "r+")
    p.seek(0, 0)
    allid = p.read()
    q = allid.find('\n' + id + '\n')
    qw = allid.find(id + '\n')
    if q == -1 and qw != 0:
        p.seek(0, 2)
        p.write(id + '\n')
        p.close()

def remove_in_list(id):
    p = open("IdList.txt", "r+")
    p.seek(0, 0)
    allid = p.read()
    x = len(allid)
    q = allid.find('\n' + id + '\n')
    qw = allid.find(id + '\n')
    if q != -1:
        p.close()
        p = open("IdList.txt", "w")
        i = 0
        while i <= q:
            p.write(allid[i])
            i += 1
        while allid[i] != '\n':
            i += 1
        i += 1
        while i < x:
            p.write(allid[i])
            i += 1
    if qw == 0:
        p.close()
        p = open("IdList.txt", "w")
        i = 0
        while allid[i] != '\n':
            i += 1
        i += 1
        while i < x:
            p.write(allid[i])
            i += 1
    p.close()

