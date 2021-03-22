def isValidSubsequence2(array, sequence):
    import pdb; pdb.set_trace()
    print(f'Array >> {array} | Sequence >> {sequence}')
    for i in sequence:
        for j in array:
            print(f'i >> {i} | j >> {j}')
            if i != j:
                return False
    return True

def isValidSubsequence(array,sequence):
    import pdb; pdb.set_trace()
    j=0
    for i in range(0,len(array)):
        print(f'i >> {i} | j >> {j}\narray[i] >> {array[i]} | sequence[j] >> {sequence[j]}')
        if array[i]==sequence[j]:
            j+=1
        print(f'len(sequence) >> {len(sequence)} | j >> {j}')
        
        if j==len(sequence):
            print(f'i >> {i} | j >> {j}')
            return True
    return False

if __name__=="__main__":
    isValidSubsequence([5,1,22,25,6,-1,8,10],[1,6,-1,10])