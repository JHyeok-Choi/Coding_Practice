def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
                
    num = 1
    while num < len(basket):
        if basket[num] == basket[num-1]:
            basket.pop(num-1)
            basket.pop(num-1)
            if num != 1:
                num -= 1
            answer += 2
        else:
            num += 1
            
    return answer