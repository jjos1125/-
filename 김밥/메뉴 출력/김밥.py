import RPi.GPIO as GPIO
from time import sleep # 라즈베리파이에서 sleep함수 가져오는것

''' 1 라즈베리파이에 파이선 제어기 설치
    2 실제 사용을 위해 pip install RPi.GPIO 를 이용해 라즈베리파이 라이브러리에 설치 후 사용
    GPIO 핀 설정 (번호는 임의로 설정)'''
data_pins = [17, 18, 27]  # 데이터 핀 번호 리스트
latch_pin = 22  # 래치 핀 번호
clock_pin = 23  # 클럭 핀 번호

# GPIO 핀 모드 설정
GPIO.setmode(GPIO.BCM)
for pin in data_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)

def toggle_switch(pin, state):
    GPIO.output(pin, state)

def refresh():
    GPIO.output(latch_pin, 1)
    GPIO.output(latch_pin, 0)

def print_braille(character):
    braille_dict = {
        '⠈': [[0, 0, 1, 0, 0, 0]],  # '⠈'에 해당하는 점자
        '⠕': [[1, 0, 0, 1, 1, 0]],  # '⠕'에 해당하는 점자
        '⠢': [[0, 0, 1, 0, 0, 1]],  # '⠢'에 해당하는 점자
        '⠘': [[0, 1, 0, 1, 0, 0]],  # '⠘'에 해당하는 점자
        '⠃': [[1, 0, 1, 0, 0, 0]]   # '⠃'에 해당하는 점자
    }
    for i in range(len(data_pins)):
        for row in braille_dict[character][i]:
            toggle_switch(data_pins[i], row)
            refresh()

def main():
    try:
        # '⠈⠕⠢' 출력
        for _ in range(3):  # 3개의 점자 출력기에 출력
            print_braille('⠈')
            print_braille('⠕')
            print_braille('⠢')
            sleep(0.5) # 500밀리초후 밥 출력


        # '⠘⠃' 출력
        for _ in range(3):  # 3개의 점자 출력기에 출력
            print_braille('⠘')
            print_braille('⠃')
            sleep(0.5) #그대로 대기

    finally:
        # 점자 출력기 종료
        for pin in data_pins:
            GPIO.output(pin, 0)
        GPIO.output(latch_pin, 0)
        GPIO.cleanup()

# 함수가 실행될떄 main 함수를 호출
if __name__ == "__main__":
    main()
