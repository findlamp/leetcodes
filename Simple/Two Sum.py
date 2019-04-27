def TwoSum(array,target):
    '''
    :param array:List[int]
    :param target:int
    :return: List[int]
    '''
    for i,num1 in enumerate(array):
        if target-num1<=0:
            break
        else:
            for j,num2 in enumerate(array):
                if target-num1-num2==0:
                    return [i,j]
                else:
                    continue


def official_solution(array,target):
    '''

    :param array:List[int]
    :param target:int
    :return: List[int]
    '''
    d={}
    for i,num in enumerate(array):
        if target-num in d:
         return [d[target-num],i]
        d[num]=i

def main():
    array=[2,7,11,15]
    target=9
    return TwoSum(array,target),official_solution(array,target)
if __name__=='__main__':
    print(main())




