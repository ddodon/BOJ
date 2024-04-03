from collections import deque


def robot_move(robot, hp):
    for i in range(N - 2, -1, -1):
        if robot[i] > 0:
            if robot[i + 1] == 0 and hp[i + 1] > 0:
                hp[i + 1] -= 1
                robot[i + 1], robot[i] = robot[i], robot[i + 1]
    return (robot, hp)


N, K = map(int, input().split())
hp = deque(map(int, input().split()))
robot = deque([0] * 2 * N)

time = 1
while 1:
    # 1. 벨트의 회전
    hp.rotate(1)
    robot.rotate(1)
    # 로봇 내리기
    if robot[N - 1] > 0:
        robot[N - 1] = 0

    # 2. 로봇 이동
    robot, hp = robot_move(robot, hp)

    # 로봇 내리기
    if robot[N - 1] > 0:
        robot[N - 1] = 0

    # 3. 로봇 올리기
    if hp[0] > 0:
        robot[0] = 1
        hp[0] -= 1

    # 4. 칸 내구도 검사
    if hp.count(0) >= K:
        break

    time += 1
print(time)