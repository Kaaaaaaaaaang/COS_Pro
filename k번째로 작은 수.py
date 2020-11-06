def solution(arr, k):
    container = []
    for i in arr:
        container += i
    container.sort()
    return container[k-1]
