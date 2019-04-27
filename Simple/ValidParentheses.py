def ValidParentheses(strs):
    '''
    Given a string containing just the characters '(',')','{','}','[' and ']',determine if the input string
    is valid.
    :param strs: string
    :return: bool
    '''
    stacks=[]
    LeftSymbol=['(','{','[']
    for elements in strs:
        if elements in LeftSymbol:
            stacks.append(elements)
        else:
            symbol=stacks.pop()
            if symbol=='(' and  ')'!= elements:
                return False
            if symbol=='{' and  '}'!=elements:
                return False
            if symbol=='[' and  ']'!=elements:
                return False
    return True

def official_solution(s):
    '''

    :param s: str
    :return: bool
    '''
    stack=[]
    d=["()","()","{}"]
    for i in range(0,len(s)):
        stack.append(s[i])
        if len(stack)>=2 and stack[-2]+stack[-1] in d:
            stack.pop()
            stack.pop()

    return len(stack)==0


if __name__=="__main__":
    print(ValidParentheses("()"))
    print(ValidParentheses("()[]{}"))
    print(ValidParentheses("(]"))
    print(ValidParentheses("([)]"))
    print(ValidParentheses("{[]}"))

    print(official_solution("()"))
    print(official_solution("()[]{}"))
    print(official_solution("(]"))
    print(official_solution("([)]"))
    print(official_solution("{[]}"))