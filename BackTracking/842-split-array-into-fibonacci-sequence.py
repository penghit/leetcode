class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(min(10, len(S))):
            firstS = S[:i+1]
            if firstS != '0' and firstS.startswith('0'):
                break
            firstN = int(firstS)
            for j in range(i+1, min(i+10, len(S))):
                secondS = S[i+1:j+1]
                if secondS != '0' and secondS.startswith('0'):
                    break
                secondN = int(secondS)
                k = j + 1
                res = [firstN, secondN]
                while k < len(S):
                    nextN = res[-1] + res[-2]
                    nextS = str(nextN)
                    if nextN <= 2**31 - 1 and S[k:].startswith(nextS):
                        k = k + len(nextS)
                        res.append(nextN)
                    else:
                        break
                
                else:
                    if len(res) >= 3:
                        return res
                
                
        return []
        
