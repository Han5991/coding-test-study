def find_max_plus_or_multiply(array):
	if not array:
		return 0
	# 첫 번째 요소로 초기화
	[result, *rest] = array

	for num in rest:
		# 더하기와 곱하기 중 더 큰 결과 선택
		result = max(result + num, result * num)

	return result


print("정답 = 728 현재 풀이 값 =", find_max_plus_or_multiply([0, 3, 5, 6, 1, 2, 4]))
print("정답 = 8820 현재 풀이 값 =", find_max_plus_or_multiply([3, 2, 1, 5, 9, 7, 4]))
print("정답 = 270 현재 풀이 값 =", find_max_plus_or_multiply([1, 1, 1, 3, 3, 2, 5]))
