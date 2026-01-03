input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
	# 모두 0으로 만들기 위한 작업 횟수
	make_all_zeros = 0
	# 모두 1로 만들기 위한 작업 횟수
	make_all_ones = 0

	# 첫 번째 문자에 대한 처리
	if string[0] == '1':
		make_all_zeros += 1  # 첫 번째 문자가 1이면 0으로 만들기 위해 한 번 작업 필요
	else:
		make_all_ones += 1  # 첫 번째 문자가 0이면 1로 만들기 위해 한 번 작업 필요

	# 나머지 문자에 대해 연속된 그룹 확인
	for i in range(1, len(string)):
		if string[i] != string[i - 1]:  # 이전 문자와 다르면 새로운 그룹 시작
			if string[i] == '1':
				make_all_zeros += 1  # 1 그룹을 0으로 만들기 위한 작업 추가
			else:
				make_all_ones += 1  # 0 그룹을 1로 만들기 위한 작업 추가

	# 두 경우 중 최소값 반환
	return min(make_all_zeros, make_all_ones)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
