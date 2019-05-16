class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        
        n = len(org)
        #if seq = [] return false
        if len(seqs) == 0:
            return False
        
        #if seq = [[],[]] or if the numbers in seqs are larger than n or less than 0
        # return false
        total = 0
        for seq in seqs:
            total = total + len(seq)
            for num in seq:
                if num > n or num <= 0:
                    return False

        if total == 0:
            return False
        
        #index contains the order of which number appears first in org
        index = [None] * (n)
        dic = {}
        for i in range(n):
            index[org[i]-1] = i
            
        #this loop test if the numbers in seqs appears in the same order in org
        #also, this loop also keeps a record of the adjcent pairs in seqs.
        for seq in seqs:
            if len(seq) == 0:
                continue
            for i in range(len(seq)):
                print(seq[i],n,seq[i]>n)
                if i < len(seq) - 1:
                    dic[str(seq[i])+'-'+str(seq[i+1])] = 1

                if i < len(seq) - 1 and index[seq[i]-1] >= index[seq[i+1]-1]:
                    return False
            
        #this last loop test if the adjcent pairs appears in org also
        #appears in sequs
        for i in range(n-1):
            if dic.get(str(org[i])+'-'+str(org[i+1])) == None:
                return False
        
        
        
        return True
