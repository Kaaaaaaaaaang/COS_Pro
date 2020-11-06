def solution(price, money):
    answer = 0
    total = sum(price)
    if(total>money):
        return -1
    else : 
        answer = money-total
    return answer
