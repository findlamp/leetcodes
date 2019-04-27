def PalindromeNumber1(num):
    '''
    normal version
    :param num: int
    :return: bool
    '''
    origin_num=num
    if num<0:
        return False
    else:
        result=0
        while int(num):
            result=result*10+num%10
            num=int(num/10)

        if origin_num==result:
            return True
#faster version
def PalindromeNumber2(num):
    '''

    :param num: int
    :return: bool
    '''
    if num<0 or (num!=0 and num%10==0):
        return False
    else:
        half=0
        while num>half:
            half=half*10+num%10
            num=int(num/10)
        return num==half or int(half/10) ==num




def main():
    num=121
    print(PalindromeNumber1(num))
    print(PalindromeNumber2(num))


if __name__=="__main__":
    main()