# 이분 탐색
# 작은 수 부터 큰 수까지 크기순대로 정렬된 리스트에서 특정값을 찾고,
# 해당 값의 위치를 출력함

# 실생활에 적용 : 특정 책 페이지를 찾을 때, 출석부에서 이름 찾을 때, 방 번호를 찾을 때 등

def binary_sear(a, x):
  # 배열의 맨앞과 맨끝 값의 위치를 변수에 저장
  first_point = 0 
  last_point = len(a) - 1

  while first_point <= last_point:
    mid_point = (first_point + last_point) // 2

    # 세가지 경우의 수
    # (1) x가 중간 위치의 값과 같을 때
    if x == a[mid_point]:
      return mid_point
    # (2) x가 중간 위치의 값보다 클 때
    elif x > a[mid_point]:
      first_point = mid_point + 1
    # (3) x가 중간 위치의 값도가 작을 때
    else:
      last_point = mid_point -1
  
  return -1

v = [1, 9, 14, 27, 55, 78]
print(binary_sear(v, 78))
print(binary_sear(v, 10))
