# 최댓값을 구하기

def f_max(a):
  n = len(a)
  max_num = a[0]
  for i in range(1, n):
    if a[i] > max_num:
      max_num = a[i]
  return max_num

s = [30, 15, 87, 63, 28, 96]
f_max(s)


# 최댓값의 위치 구하기

def f_index(a):
   n = len(a)
   max_index = 0
   for i in range(1, n):
    if a[i] > a[max_index]:
      max_index = i
   return max_index

s = [30, 15, 87, 63, 28, 96]
f_index(s)


# 최솟값의 위치 구하기

def f_min(a):
  n = len(a)
  min_num = a[0]
  for i in range(1, n):
    if a[i] < min_num:
      min_num = a[i]
  return min_num

s = [30, 15, 87, 63, 28, 96]
f_min(s)
