from collections import deque


N = int(*map(int, input().split()))
waitings, entrance_order = deque(), []
for _ in range(N):
    waiting_people = list(map(str, input().split()))
    temp_waitings = deque()
    for wp in waiting_people:
        a, b = wp.split('-')
        temp_waitings.append((a,int(b)))
    waitings.append(temp_waitings)
    entrance_order.append(list(temp_waitings))

entrance_order = deque(sorted(sum(entrance_order, [])))

temp = []
while entrance_order:

    person = entrance_order[0]

    if waitings and waitings[0] and person == waitings[0][0]:
        entrance_order.popleft()
        waitings[0].popleft()

    elif temp and person == temp[-1]:
        temp.pop()
        entrance_order.popleft()

    else:
        if not waitings:
            break
        temp.append(waitings[0].popleft())

    if waitings and not waitings[0] and N >= 2:
        waitings.popleft()

if not entrance_order:
    print('GOOD')
else:
    print('BAD')