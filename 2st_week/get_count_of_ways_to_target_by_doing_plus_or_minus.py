import math

numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    total_sum = sum(array)

    # 불가능한 경우 체크
    if total_sum < abs(target) or (total_sum + target) % 2 != 0:
        return 0

    # 합이 (total_sum + target) / 2가 되는 부분 집합의 개수를 구합니다
    subset_sum = (total_sum + target) // 2

    # DP 테이블 초기화: dp[i]는 합이 i가 되는 부분 집합의 개수
    dp = [0] * (subset_sum + 1)
    dp[0] = 1  # 아무것도 선택하지 않아 합이 0이 되는 경우는 1가지

    # 각 숫자에 대해
    for num in array:
        # 거꾸로 순회하여 현재 숫자를 포함하는 경우 계산
        for i in range(subset_sum, num - 1, -1):
            dp[i] += dp[i - num]

    return dp[subset_sum]


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
print(get_count_of_ways_to_target_by_doing_plus_or_minus([2, 3, 1], 0))
