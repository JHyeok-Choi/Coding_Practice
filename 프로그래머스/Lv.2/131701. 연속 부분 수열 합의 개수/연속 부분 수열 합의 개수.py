def solution(elements):
    return len(set(sum((elements*2)[i:i+j]) for j in range(len(elements)) for i in range(len(elements))))
