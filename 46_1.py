# 리스트 평탄화 : 리스트의 중첩을 제거하는 처리
# [1,2,[3,4],5,[6,7],[8,9,]]
# --> [1,2,3,4,5,6,7,8,9]

a=[1,2,[3,4],5,[6,7],[8,9,]]
k=[]
for i in a:
    if type(i)==list:
        for j in i:
            k.append(j)
    else:
        k.append(i)
print(k)
