def solution(arr):
    answer = [] #새로운 리스트
    for i in range(len(arr)): #answer의 최대길이는 arr의 길이
        if i==0: 
            answer.append(arr[i]) #answer[0]에 arr[0]대입
        elif arr[i] != arr[i-1]: 
            answer.append(arr[i]) #answer[1]부터는 arr의 전후원소가 다를때 arr[i]값 대입     
    return answer
