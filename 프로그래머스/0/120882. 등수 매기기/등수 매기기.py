def solution(score):
    averages = [(sum(s) / 2, i) for i, s in enumerate(score)]
    sorted_scores = sorted(averages, key=lambda x: -x[0])
    ranks = [0] * len(score)

    rank = 1
    for i in range(len(sorted_scores)):
        if i > 0 and sorted_scores[i][0] == sorted_scores[i - 1][0]:
            ranks[sorted_scores[i][1]] = ranks[sorted_scores[i - 1][1]]
        else:
            ranks[sorted_scores[i][1]] = rank
        rank += 1

    return ranks
