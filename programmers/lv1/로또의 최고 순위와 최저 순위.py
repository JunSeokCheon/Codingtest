def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    pure_count = 0
    
    for lottos_num in lottos:
        if lottos_num in win_nums:
            pure_count += 1
    
    zero_count = lottos.count(0)
    max_count = pure_count + zero_count
    min_count = pure_count
    
    answer.append(rank[max_count])
    answer.append(rank[min_count])
    return answer