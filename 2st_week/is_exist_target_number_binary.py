finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    start = 0
    end = len(array) - 1
    # 바이너리 탐색은 정렬 되어 있어야 사용이 가능하다
    array = sorted(array)

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)