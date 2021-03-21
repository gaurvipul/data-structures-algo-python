def findOdd1(l):
    import pdb
    pdb.set_trace()
    if isinstance(l,list):
        print(f'list >> {l}\n')
        for x in l:
            count = l.count(x)
            print(f'list >> {l}\n')
            print(f'x >> {x} | count >> {count}')
            if count % 2 != 0:
                res = x
        return res
    return None    
    
if __name__=='__main__':
    findOdd1([9,2,1,1,4,5,5,6,6,6,6,8,8,8,8,8,8,9,9,9])
    