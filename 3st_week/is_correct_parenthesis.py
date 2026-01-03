from stack import Stack

def is_correct_parenthesis(string):
	stack = Stack()

	for char in string:
		if char == "(":
			stack.push(char)
		elif char == ")":
			if stack.is_empty():
				return False
			stack.pop()

	return stack.is_empty()


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))