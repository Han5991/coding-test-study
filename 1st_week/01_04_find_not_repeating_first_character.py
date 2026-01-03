def find_not_repeating_first_character(string):
	strs = list(string)

	strs2 = {char: strs.count(char) for char in set(strs)}
	min_list = [key for key, value in strs2.items() if value == 1]

	if len(min_list) == 0:
		return '_'
	return min_list[0]


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))
