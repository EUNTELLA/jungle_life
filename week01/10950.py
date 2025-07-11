# a + b - 3

# 테스트 케이스 개수 t
# 테스트 케이스 한줄, 각줄에 a,b 주어짐 (0<a,b<10)


t = int(input())

for i in range(1,t+1):
    a,b = map(int,input().split())
    for t in range(1, t+1):
        print(a+b)




