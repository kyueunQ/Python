# 탐색과 정렬_순차 탐색

# first trial: error:
# a[0]과 x가 같지 않다면 무조건 -1만 출력
# return -1이 if절에 속해, for 문의 반복이 이뤄지지 않았기 때문

def find_loc_err(a, x):
  n = len(a)
  
  for i in range(0, n):
    if a[i] == x:
      return i
    else:
      return -1

c = [44, 20, 47, 14, 22, 99, 63, 86]

print(find_loc_err(c, 20))
print(find_loc_err(c, 18))

# second trial

def find_loc(a, x):
  n = len(a)
  
  for i in range(0, n):
    if a[i] == x:
      return i
  
  return -1

c = [44, 20, 47, 14, 22, 99, 63, 86]

print(find_loc(c, 20))
print(find_loc(c, 29))


# 활용 1. 찾고자하는 값(x)의 list 내 모든 위치를 출력하는 알고리즘 (결과를 리스트 형태로 출력하며, x값이 리스트에 없을 경우 []를 출력)

# first trial: error:

def find_loc2_err(a, x):
  n = len(a)
  s = []
  for i in range(0, n):
    if a[i] == x:
      return i
      s.append(i)

  return s

c = [12, 36, 27, 58, 36, 23, 10]

print("--------------")
print(find_loc2_err(c, 36))
print(find_loc2_err(c, 55))

# second trial

def find_loc2(a, x):
  n = len(a)
  s = []
  for i in range(0, n):
    if a[i] == x:
      s.append(i)

  return s

c = [12, 36, 27, 58, 36, 23, 10]

print("--------------")
print(find_loc2(c, 36))
print(find_loc2(c, 55))
