# 슬라이싱은 필요한 정보만 가저오는 기술


jumin = "990120-1234567"

print("성별 : " ,jumin[7]) # 성별 정보는 1
print("연 :", jumin[0:2]) # 연 정보 (a:b 는 a자리 부터 b자리 직전 까지)
print("월 :", jumin[2:4])
print("일 :", jumin[4:6])

print("생년월일 :", jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 :", jumin[7:]) # 7부터 끝까지

print("뒤 7자리 (뒤에부터) : ", jumin[-7:])