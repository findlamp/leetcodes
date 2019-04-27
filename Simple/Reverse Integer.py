def ReverseInt(num):
    '''

    :param num: int
    :return: int
    '''
    result=0
    sign= num <0 and -1 or 1

    num=abs(num)
    while int(num):
        result=result*10+num%10
        num=int(num/10)
    return sign*result if result <=0x7fffffff else 0

def official_solution(x):
    '''

    :param x: int
    :return: int
    '''
    ans=0
    sign= x<0 and -1 or 1
    x=abs(x)
    while x:
        ans=ans*10+x%10
        x/=10
    return sign*ans if ans <=0x7fffffff else 0

def main():
    num=123
    print(ReverseInt(num))
    print(official_solution(num))

if __name__=='__main__':
    main()

