# 선택 정렬 (오름차순)

# frist trial: err:

def sort_select(a):
  n = len(a)
  v = []
  s = 0

  for i in range(0, n - 1):
    for j in range(i + 1, n):
      if a[i] > a[j]:
        s = j
        return v.append(a[s])
      return v.append(a[s])
  return v

x = [2, 4, 5, 1, 3]
print(sort_select(x))


# second trial
# 1. 제일 작은 수의 위치 파악하기

def min_index(a):
  n = len(a)
  s = 0
  for i in range(1, n - 1):
    if a[s] > a[i]:
      s = i
  return s

y = [67, 23, 18, 56, 72]
print(min_index(y))

# 2. 제일 작은 수를 새로운 리스트에 순서대로 추가하기

def add_min(a):
  v = []
  
  # pop기능으로 결과적으로 len(a) = 0,
  # len(v) = n이 될 것이기 때문에 당연히 성립X
  #while len(v) == len(a):
  while a:
    sort_min = min_index(a)
    s = a.pop(sort_min)
    v.append(s)
  return v

y = [67, 23, 18, 56, 72]
print(add_min(y))


# third trial: 또 다른 방법

def sort_select2(a):
  n = len(a)
  for i in range(0, n - 1):
    min_ind = i
    for j in range(i + 1, n):
      if a[min_ind] > a[j]:
        min_ind = j
        a[i], a[min_ind] = a[min_ind], a[i]

y = [67, 23, 18, 56, 72]
sort_select2(y)
print(y)
# print(sort_select2(y))는 왜 None이 출력될까?
    

# 활용. 내림차순 선택정렬

def sort_select3(a):
  n = len(a)
  for i in range(0, n-1):
    max_ind = i
    for j in range(i+1, n):
      if a[max_ind] < a[j]:
        max_ind = j
        a[max_ind], a[i] = a[i], a[max_ind]

y = [67, 23, 18, 56, 72]
sort_select3(y)
print(y)
