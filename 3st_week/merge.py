array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
	result = []
	i, j = 0, 0
	len1, len2 = len(array1), len(array2)

	while i < len1 and j < len2:
		if array1[i] < array2[j]:
			result.append(array1[i])
			i += 1
		else:
			result.append(array2[j])
			j += 1

	# 남은 요소들 추가
	result.extend(array1[i:])
	result.extend(array2[j:])

	return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1, 2, 3, 5, 40], [10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1, -1, 0], [1, 6, 9, 10]))
