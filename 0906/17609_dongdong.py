# 백준 17609 회문 날쩌ㅏㅏ  

# 투포인터를 이용해서 회문검사

def is_pal(left, right):

    while left < right: # 만나기 전까지 돌리기
        # left와 right 문자 동일 => left + 1, right +1 다음으로 넘어가서 체크
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return 0

    return 1



T = int(input())
for _ in range(T):
    s = input()
    check = 0
    left_num = 0
    right_num = len(s) -1

    while left_num < right_num:
        if s[left_num] == s[right_num]:
            left_num += 1
            right_num -= 1
        else:
            if s[left_num] == s[right_num-1]:
                if is_pal(left_num, right_num-1):
                    check = 1
                    break

            if s[left_num + 1] == s[right_num]:
                if is_pal(left_num+1, right_num):
                    check = 1
                    break

            check = 2
            break

    print(check)
