import wfuzz

def get_direnum_info(target):
    enumtable=""
    for r in wfuzz.fuzz(url=str(target.strip()+"/FUZZ"), hc=[404], payloads=[("file",dict(fn="./payloads/directory-list-2.3-medium.txt"))]):
        print(r)
        enumtable=enumtable + str(r) + "\n"
    return enumtable

