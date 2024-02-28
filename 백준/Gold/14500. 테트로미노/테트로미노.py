def case_1(i, j):  # 2x2정사각형
    try: return (arr[i][j] + arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1])
    except: return 0
def case_2(i, j):  # 1x4 줄
    try: return (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3])
    except: return 0
def case_2T(i, j):  # 4x1 줄
    try: return (arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j])
    except: return 0
case1_2 = [case_1, case_2, case_2T]

def case_3a(i,j):
    try: return (arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1])
    except: return 0
def case_3b(i,j):
    try: return (arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2] + arr[i][j+2])
    except: return 0
def case_3c(i,j):
    try: return (arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1])
    except: return 0
def case_3d(i,j):
    try: return (arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i][j+2])
    except: return 0

def case_3aT(i,j):
    try: return (arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1] + arr[i+2][j])
    except: return 0
def case_3bT(i,j):
    try: return (arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2])
    except: return 0
def case_3cT(i,j):
    try: return (arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j])
    except: return 0
def case_3dT(i,j):
    try: return (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2])
    except: return 0
case3 = [case_3a, case_3aT, case_3b, case_3bT, case_3c, case_3cT, case_3d, case_3dT]

def case_4a(i,j):
    try: return (arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1])
    except: return 0
def case_4b(i,j):
    try: return (arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] + arr[i][j+2])
    except: return 0
def case_4c(i,j):
    try: return (arr[i+2][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1])
    except: return 0
def case_4d(i,j):
    try: return (arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2])
    except: return 0
case4 = [case_4a, case_4b, case_4c, case_4d]

def case_5a(i,j):
    try: return (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1])
    except: return 0
def case_5b(i,j):
    try: return (arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j])
    except: return 0
def case_5c(i,j):
    try: return (arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] + arr[i+1][j+2])
    except: return 0
def case_5d(i,j):
    try: return (arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1])
    except: return 0
case5 = [case_5a, case_5b,  case_5c, case_5d]



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = 0
for i in range(N):
    for j in range(M):
        for c in case1_2:
            mx = max(mx, c(i, j))
        for c in case3:
            mx = max(mx, c(i, j))
        for c in case4:
            mx = max(mx, c(i, j))
        for c in case5:
            mx = max(mx, c(i, j))
print(mx)