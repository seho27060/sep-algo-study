N, M = map(int, input().split())
books = list(map(int, input().split()))

books.sort()

left = 0 if books[0] < 0 else 1e10
right = N - 1 if books[N - 1] > 0 else 1e10

step = []
while not(left == 1e10 and right == 1e10):
    leftBook = abs(books[left]) if left != 1e10 else 1e10
    rightBook = books[right] if right != 1e10 else 1e10

    if left != 1e10 and right != 1e10:
        if leftBook >= rightBook:
            step.append(leftBook)
            left += M
            if left >= N or books[left] > 0:
                left = 1e10
        else:
            step.append(rightBook)
            right -= M
            if right < 0 or books[right] < 0:
                right = 1e10
    elif left != 1e10 and right == 1e10:
        step.append(leftBook)
        left += M
        if left >= N or books[left] > 0:
            left = 1e10
    elif left == 1e10 and right != 1e10:
        step.append(rightBook)
        right -= M
        if right < 0 or books[right] < 0:
            right = 1e10


ans = step[0] + (sum(map(lambda x: x * 2, step[1:])) if len(step) > 1 else 0)
print(ans)
