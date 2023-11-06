# print("a" + "b")
# print("a", "b")


# 방법 1
print("나는 %d살 입니다." %20) # d는 언제나 정수값만 출력가능
print("나는 %s을 좋아해요." % "파이썬") # s는 문자
print("Apple 은 %c로 시작해요." % "A") # c는 한글자
# %s는 정수 문자 한글자 모두 출력 가능

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))


# 방법 2
print("나는 {}살 입니다.".format(20)) # format(값) 값을 {}에 대입
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 0번째 1번째 format 값을 대입
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))


# 방법 4(v3.6 ~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")



