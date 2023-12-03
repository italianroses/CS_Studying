# Quiz) 당신은  Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
#
# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
#
# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번쩨 손님 (소요시간 : 16분)
#
# 총 탑승 승객 : 2 분

from random import *
count = 0
index = 1
while index <= 50:
    time = randint(5, 50)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(index, time))
        index += 1
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(index, time))
        index += 1

print("총 탑승 승객 : {0} 분".format(count))


 # Answer
from random import *

count = 0

for index in range(1, 51):
    time = randint(5, 50)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(index, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(index, time))

print("총 탑승 승객 : {0} 분".format(count))




