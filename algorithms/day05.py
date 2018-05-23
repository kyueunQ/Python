# 최대공약수 구하기 (2가지 방법)
# 첫번째 방법
def get_gcd(a, b):
  i = min(a, b)
  while i != 0:
    if a % i == 0 and b % i == 0:
      return i
    i = i - 1
      
print(get_gcd(12, 15))
print(get_gcd(12, 36))
print(get_gcd(25, 35))


# 아래의 경우 오류를 출력하는 이유
# i = 12를 출력하고 종료하면 되는데,
# return 12를 한 후에 i = i - 1이 실행됨
# 다음으로 if 조건을 만족시키는 6으로 i가 출력됨
def get_gcd1(a, b):
  i = min(a, b)
  while i != 0:
    i = i - 1
    if a % i == 0 and b % i == 0:
      return i
    
print(get_gcd1(12, 36))


# 두번째 방법: 유클리드 알고리즘
# a, b의 최대공약수 = b와 a%b의 최대공약수
# n과 0의 최대공약수 = n

def get_gcd3(a, b):
  if b == 0:
    return a
  return get_gcd3(b, a % b)
  
print(get_gcd3(12, 26))


def get_gcd4(a, b):
  while b == 0:
    return a
  return get_gcd3(b, a % b)
  
print(get_gcd3(12, 36))
