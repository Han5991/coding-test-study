from collections import Counter


def find_max_occurred_alphabet(string):
    # 모든 알파벳 문자만 추출하고 소문자로 변환
    letters = [char.lower() for char in string if char.isalpha()]

    # 빈 문자열 또는 알파벳이 없는 경우 처리
    if not letters:
        return None

    # Counter 사용하여 문자 빈도 계산
    char_counts = Counter(letters)

    # 가장 빈도가 높은 문자 찾기
    max_count = max(char_counts.values())

    # 빈도가 가장 높은 문자들 중 알파벳 순서가 가장 빠른 것 반환
    return min(char for char, count in char_counts.items() if count == max_count)


# 테스트 출력
print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))
print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("cccbbbaaa"))