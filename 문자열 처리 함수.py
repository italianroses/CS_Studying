python = "Python is Amazing"

print(python.lower()) # lower() 소문자 변환
print(python.upper()) # upper() 대문자 변환

print(python[0].isupper()) # 몇번째 문자가 대문자가 맞는지 틀린지
print(len(python)) # 전체길이 계산

print(python.replace("Python", "Java")) # 문자열 안의 문자 바꾸기



index = python.index("n") # "n"이 몇번째에 있는지?
print(index)

index = python.index("n", index + 1) # 두번째 n 찾기
print(index)

print(python.find("n")) # 문자 찾기
print(python.find("Java")) # 없을경우 -1을 반환한다

print(python.index("Java")) # Error 발생

print(python.count("n")) # 