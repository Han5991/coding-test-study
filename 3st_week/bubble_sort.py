input = [4, 6, 2, 9, 1]


def bubble_sort(array):
	n = len(array)
	for i in range(n):
		for j in range(0, n - i - 1):
			if array[j] > array[j + 1]:  # 오름차순 정렬을 위해 부등호 방향 변경
				array[j], array[j + 1] = array[j + 1], array[j]
	return array


# bubble_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ", bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", bubble_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ", bubble_sort([100, 56, -3, 32, 44]))
