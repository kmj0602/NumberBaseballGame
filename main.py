from validation import validate_digit_count, validate_guess
from game import create_answer, check_guess



print("=========== 숫자야구게임 규칙(rule) ===========")
print()
print("- 0 ~ 9 사이의 숫자만 사용 가능")
print("- 첫 자리에 0 사용 가능, BUT 중복 숫자 금지")
print("- 숫자와 위치가 모두 같으면? 스트라이크(strike)")
print("- 숫자는 같지만 위치가 다르면? 볼(ball)")
print("- 일치하는 숫자가 없으면? 아웃(out)")
print("- 정답 확인: answer / 게임 종료: quit")
print()
print("===============================================")
print()



# 올바른 자리 수를 선택할 때까지 반복
while True:
	choice = input("> 자리 수를 입력하세요. (3 또는 4): ")
	
	# 자리 수 선택하는 단계에서도 종료 가능
	if choice == "quit":
		break

	error_message = validate_digit_count(choice)

	# 오류가 있으면 안내하고 다시 입력 받기
	if error_message != "":
		print(error_message)
		continue

	# 선택 검사를 통과한 뒤 자리 수만 정수로 바꾸기
	digit_count = int(choice)
	break

if choice == "quit":
	print("\n[정보] 게임 종료")

else:

	# 정답은 게임 시작 시 한 번만 생성
	answer = create_answer(digit_count)

	# 유효한 숫자 입력의 횟수를 기록
	attempt_count = 0

	# 이전 입력과 출력할 기록을 각각 보관
	previous_guesses = []
	history = []

	print(f"\n=========== {digit_count}자리 숫자야구게임 시작 ===========")



	# 정답을 맞힐 때까지 추측 입력을 반복
	while True:

		guess = input(
			f"\n> 중복 없는 {digit_count}자리 숫자 입력 "
			"(정답 확인: answer 입력): "
		)

		# 'answer'을 입력하면 정답을 보여주고 다시 입력받기 (시도 횟수 포함 X)
		if guess == "quit":
			print("\n[정보] 게임 종료")
			break

		if guess == "answer":
			print(f"\n[정보] 정답은 {answer} ㅋㅋ 줴줴이야~")
			continue

		# 숫자 입력에 대해서만 길이, 문자, 중복 검사
		error_message = validate_guess(guess, digit_count)

		# 잘못된 입력은 판정하지 않고 다시 입력 받기 (시도 횟수 포함 X)
		if error_message != "":
			print(error_message)
			continue

		# 이전에 입력한 숫자면 안내 (시도 횟수 포함 O)
		if guess in previous_guesses:
			print("\n[경고] 이전에 입력한 숫자")

		previous_guesses.append(guess)
	
		# 입력 검사를 통과한 경우에만 횟수 증가
		attempt_count += 1

		strike, ball = check_guess(answer, guess)
	
		if strike == 0 and ball == 0:
			result = "[결과] 아웃"
		else:
			result = (f"[결과] {strike} 스트라이크 {ball} 볼")

		print(f"\n시도 횟수: {attempt_count}회\n")	
		print(result)
	
		# 이번 입력과 판정 결과를 기록에 추가
		record = f"{attempt_count}회 | {guess} | {result}"
		history.append(record)

		# 유효한 입력을 할 때마다 전체 기록 보여주기
		print("\n------------ 입력 결과 기록 ------------")
		for record in history:
			print(record)

		# 모든 숫자와 위치를 맞히면 게임 종료 (시도 횟수 포함 O)
		if strike == digit_count:
			print("\n============= 정답 ㅊㅊ =============")
			break	