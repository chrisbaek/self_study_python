a=input("염기서열을 입력해주세요:")
b={}
for i in range(0,len(a),3):
    c=a[i:i+3]
    if len(c) < 3 :
        continue
    elif c in b:
        b[c]+=1
    else :
        b[c]=1

print(b)


