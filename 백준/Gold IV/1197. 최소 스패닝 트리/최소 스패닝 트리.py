'''
Memo BOJ 1197
돌아서면 까먹는 최소신장트리
union + find를 이용해 해결 가능
최소스패닝
=> 가중치 기준으로 정렬 후 간선의 개수 - 1 개 만큼만 반복
'''

def union(a,b):
    v[find(b)] = find(a)

def find(a):
    if v[a] != a:
        v[a] = find(v[a])
    return v[a]


V, E = map(int, input().split())
# 트리 노드 / 엣지 / 가중치를 입력받아서 가중치 기준으로 오름차순 정렬
arr = [list(map(int,input().split())) for _ in range(E)]
arr.sort(key=lambda x:x[2])
# 최소 스패팅 트리의 가중치 합 / 간선 연결 회수
sm = cnt = 0

# 노드 방문 표시 배열
v = [0]+ [i for i in range(1,V + 1)]

for a,b,c in arr:
    # 서로 연결되지 않은 노드라면 연결 후 가중치 저장
    if find(a) == find(b):
        continue
    sm += c
    cnt += 1
    union(a,b)
    if cnt>=(V-1):
        break
print(sm)