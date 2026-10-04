# 게임 시작 시 3자리 또는 4자리를 선택했는지 검사.
def validate_digit_count(choice):
	if choice == "3" or choice == "4":
		return ""

	return "\n[경고] 자리 수는 3 또는 4를 입력하세요."

# 추측 입력의 길이, 문자, 숫자가 중복인지 검사.
# guess: 사용자가 입력한 문자열
# digit_count: 선택한 자리 수인 정수 3 또는 4
def validate_guess(guess, digit_count):
	# 1. 선택한 자리 수와 입력 길이가 같은지 확인
	if len(guess) != digit_count:
		return f"\n[경고] {digit_count}자리로 입력하세요."
	
	# 2. 입력한 각 문자가 0~9 중 하나인지 확인.
	for digit in guess:
		if digit not in "0123456789":
			return "\n[경고] 0부터 9까지의 숫자만 입력하세요."

	# 3. 같은 숫자가 두 번 이상 포함되어 있는지 확인.
	for digit in guess:
		if guess.count(digit) > 1:
			return "\n[경고] 중복된 숫자 없이 입력하세요."

	# 모든 검사를 통과하면 빈 문자열 반환.
	return ""