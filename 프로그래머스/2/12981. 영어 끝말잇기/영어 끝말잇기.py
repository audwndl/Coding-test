def solution(n, words):
    answer = [words[0]]
    for i in range(1, len(words)):
        if answer[-1][-1]==words[i][0] and words[i] not in answer:
            answer.append(words[i])
        else :
            return [(i%n)+1,(i//n)+1] #[누가, 몇번째턴]
    if answer == words:
        return [0,0]