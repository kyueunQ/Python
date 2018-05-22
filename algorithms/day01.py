# 1~N까지 연속한 숫자의 합 구하기 (2가지 방법)
# (1) for문 활용하기

def sum1(n):
  s = 0
  for i in range(1, n+1):
    s = s + i
  return s

print(sum1(10))


# (2) 공식 활용하기

def sum2(n):
  #return (1+n)*(n/2)
  return (1+n)*n // 2

print(sum2(10))
print(sum2(9))


# 1~N까지 연속한 숫자의 제곱합 구하기 (2가지 방법)
# (1) 각 숫자마다 제곱하여 더하기

def sum3(n):
  s = 0
  for i in range(1, n+1):
    s = s + i**2
  return s

print(sum3(10))

# (2) 공식 활용하기

def sum4(n):
  return n*(n+1)*(2*n+1) // 6

print(sum4(10))
