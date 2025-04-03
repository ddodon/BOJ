import sys
input = sys.stdin.readline

def build(arr, node, node_left, node_right):
    if node_left == node_right:
        tree[node] = arr[node_left]
        return
    mid = (node_left + node_right) // 2
    build(arr, 2 * node, node_left, mid)
    build(arr, 2 * node + 1, mid + 1, node_right)
    tree[node] = tree[2 * node] + tree[2 * node + 1]

def update(node, node_left, node_right, idx, diff):
    if idx < node_left or idx > node_right:
        return
    tree[node] += diff
    if node_left != node_right:
        mid = (node_left + node_right) // 2
        update(2 * node, node_left, mid, idx, diff)
        update(2 * node + 1, mid + 1, node_right, idx, diff)

def query(node, node_left, node_right, L, R):
    if R < node_left or node_right < L:
        return 0
    if L <= node_left and node_right <= R:
        return tree[node]
    mid = (node_left + node_right) // 2
    left_sum = query(2 * node, node_left, mid, L, R)
    right_sum = query(2 * node + 1, mid + 1, node_right, L, R)
    return left_sum + right_sum

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (4 * N)  # 충분한 크기 할당
build(arr, 1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:  # update
        diff = c - arr[b - 1]
        arr[b - 1] = c
        update(1, 0, N - 1, b - 1, diff)
    else:  # query (b ~ c 구간 합)
        print(query(1, 0, N - 1, b - 1, c - 1))