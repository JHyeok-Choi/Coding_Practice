def solution(prices):
    answer = [i for i in range(len(prices) -1, -1, -1)]
    stk = []
    
    for i in range(len(prices)):
        while stk and prices[i] < prices[stk[-1]]:
            answer[stk[-1]] = i - stk[-1]
            stk.pop()
        stk.append(i)
        
    return answer