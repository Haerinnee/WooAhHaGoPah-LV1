N = int(input()) #첫줄에 막대기 개수를 나타내는 정수 N 입력

list1=[]
answer=[]
for i in range(N):
    list1.append(input())  #N개원소 list1에 입력
list1.reverse()           #list1거꾸로(오른쪽에서 막대기 봄)

for k in range(N):
    if k==0:
        answer.append(list1[k]) #answer리스트첫번째원소에 list1[0]입력
    elif list1[k]>max(answer):
        answer.append(list1[k]) #list1의k번째원소가 answer안의 최댓값보다 크면 answer에 입력
print(answer)
print(len(answer))
