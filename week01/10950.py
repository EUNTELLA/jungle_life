# a + b - 3

# 테스트 케이스 개수 t
# 테스트 케이스 한줄, 각줄에 a,b 주어짐 (0<a,b<10)


t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    print(a+b)



