# 연도가 4로 나누어지지만 100으로 나누어지지 않거나 또는 연도가 400으로 나누어 떨어지면 윤년이다.
# 사용자가 연도를 입력하면 윤년을 판별할 수 있는 프로그램을 작성하라.

year = int(input("연도를 입력하시오: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")