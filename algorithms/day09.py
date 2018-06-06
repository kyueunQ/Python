# 삽입정렬

# 첫번째 방법
# 1. 위치 찾기
def sort_insert_ind(a, x):
  n = len(a)
  for i in range(0, n):
    if x < a[i]:
      # 17(i번째), 23, 33이 있을 때,
      # 15가 들어간다면 15 < 17
      # 15(i번째), 17, 23, 33 으로 재정렬
      return i
  return n


# 2. 새로운 리스트에 순서대로 넣기
def sort_insert(a):
  new_a = []
  while a:
     x = a.pop(0)
     ind = sort_insert_ind(new_a, x)
     # append(): takes exactly one argument
     # new_a.append(ind, x)
     new_a.insert(ind, x)
  return new_a


v = [55, 33, 13, 46, 82, 28]
print(sort_insert(v))



# 두번째 방법
# 기존 배열을 재배열하기
def sort_ins(a):
  n = len(a)
  for i in range(1, n):
    x = a[i]
    j = i - 1
    while j >= 0 and x < a[j]:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = x

arr = [33, 76, 29, 11, 58, 99]
sort_ins(arr)
print(arr)


# 응용. 삽입정렬 내림차순
def sort_ins2(a):
  n = len(a)
  for i in range(1, n):
    x = a[i]
    j = i - 1
    while j >= 0 and x > a[j]:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = x

arr = [33, 76, 29, 11, 58, 99]
sort_ins2(arr)
print(arr)
