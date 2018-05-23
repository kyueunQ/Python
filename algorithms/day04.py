# factorial 알고리즘 (2가지 방법)
# (1) 1~n까지 연속한 정수의 곱을 구하기

def facto(n):
  s = 1
  for i in range(1, n+1):
    s = i * s
  return s

print(facto(10))


# (2) 재귀호출을 통한 구현

def facto2(n):
  if n <= 1:
    return 1
  return n * facto2(n-1)

print(facto2(10))


# 활용1. 1~n까지 연속된 숫자 합을 재귀 함수로 구하기

# firtst trial
def sum_num(n):
  if n<= 1:
    return 1
  return n + sum_num(n-1)

print(sum_num(100))
# n=0 일 경우, return 1 ? 해당 조건일 경우 바로 종료 ?

# 활용2. 숫자 n개 중에서 재귀 함수를 이용해 최댓값 찾기

# for 문을 이용했을 때

def find_max(a):
  s = a[0]
  n = len(a)
  for i in range(0, n-1):
    for j in range(i+1, n):
      if a[i] < a[j]:
        s = a[j]
  return s

v = [13, 66, 83, 92, 100]
print(find_max(v))

# 재귀 함수를 이용했을 때

