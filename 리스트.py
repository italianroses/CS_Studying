# 리스트[]

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # append는 마지막 자리에 리스트 추가
print(subway)


# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") # insert는 사이에 추가
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # pop()은 꺼내기
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석")) # count로 숫자세기

# 정렬도 가능
num_List = [5, 2, 4, 3, 1]
num_List.sort()
print(num_List)

# 순서 뒤집기 가능
num_List.reverse()
print(num_List)

# 모두 지우기
num_List.clear()
print(num_List)

# 다양한 자료형 함깨 사용
max_list = ["조세호", 20, True]
print(max_list)

# 리스트 확장
num_List = [5, 2, 4, 3, 1]
num_List.extend(max_list)
print(num_List)