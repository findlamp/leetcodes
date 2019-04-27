def RomanToInteger(RomanNum):
    '''

    :param RomanNum: String
    :return: int
    '''

    RomanCharToInt={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result=0
    for i in range(len(RomanNum)-1):
        if RomanCharToInt[RomanNum[i]] >= RomanCharToInt[RomanNum[i+1]]:
            result += RomanCharToInt[RomanNum[i]]
        else:
           result -= RomanCharToInt[RomanNum[i]]
        
    result+=RomanCharToInt[RomanNum[-1]]


    return result

def official_solution(s):
    ans=0
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(s)-1):
        c=s[i]
        cafter=s[i+1]
        if d[c]<d[cafter]:
            ans-=d[c]
        else:
            ans+=d[c]
    ans+=d[s[-1]]
    return ans



def main():
    RomanNum="MCMXCIV"
    print(RomanToInteger(RomanNum))
    print(official_solution(RomanNum))
if __name__=='__main__':
    main()
