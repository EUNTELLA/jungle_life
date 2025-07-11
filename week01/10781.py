# x 보다 작은 수

# n과 x
# 수열 a를 이루는 정수 n개 

n,x = map (int,input().split())
a = list(map(int,input().split()))

for num in a:
    if num < x:
        print(num, end=' ')

