import random

# 선택한 자리 수에 맞춰 중복 없는 정답 만들기
def create_answer(digit_count):
	numbers = "0123456789"

	# 0~9에서 서로 다른 숫자 선택.
	selected_numbers = random.sample(numbers, digit_count)

	# 선택한 숫자들을 하나의 문자열로 연결.
	answer = "".join(selected_numbers)

	return answer

# 정답과 추측을 비교하여 스트라이크와 볼 계산.
def check_guess(answer, guess):
	strike = 0
	ball = 0
	
	# 각 위치의 숫자를 하나씩 비교.
	for index in range(len(answer)):
		# 숫자와 위치가 모두 같으면 스트라이크.
		if guess[index] == answer[index]:
			strike += 1

		# 위치는 다르지만 정답에 있는 숫자이면 볼.
		elif guess[index] in answer:
			ball += 1

	return strike, ball 