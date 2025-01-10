def solution(score):
    averages = [(sum(scores) / 2) for scores in score]
    sorted_avg = sorted(averages, reverse=True)
    ranks = [sorted_avg.index(avg) + 1 for avg in averages]
    return ranks
