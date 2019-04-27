def LongestCommonPrefix(array):
    '''
    This function is to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    :param array: list[str]
    :return: string
    '''
    if len(array)==0:
        return ""

    LongestCommonPrefix=""
    CommonPrefix=""
    for end in range(1,len(array[0])+1):
        Prefix=array[0][0:end]
        for row in range(1,len(array)):
            if Prefix!=array[row][:end]:
               CommonPrefix=LongestCommonPrefix
               break
            CommonPrefix=Prefix
        LongestCommonPrefix=CommonPrefix

    return LongestCommonPrefix




def official_solution(strs):
    '''
    This function has some error.
    The
    :param strs: List[str]
    :return: str
    '''
    if len(strs)==0:
        return ""
    i=0
    j=0
    end=0
    while j<len(strs) and i<len(strs[j]):

        if i==0:
            char=strs[j][i]
        else:
            if strs[j][i]!=char:
                break
        if j==len(strs)-1:
            i+=1
            j=0
            end+=1
        else:
            j+=1
    return strs[j][:end]
if __name__=="__main__":
    print(LongestCommonPrefix(["flower","flow","flight"]))
    print(LongestCommonPrefix(["dog","racecar","car"]))
    print(official_solution(["flower","flow","flight"]))
    print(official_solution(["dog","racecar","car"]))