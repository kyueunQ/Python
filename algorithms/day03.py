# pr_03
# 리스트 내의 동일한 요소를 찾아 출력

# first trial: error:
# 1번째 숫자 3과 나머지 요소들을 비교하고 끝남 (2번째-3번째.. 비교 불가)

def find_comm(a):
  b = set()
  n = len(a)
  comm_num = a[0]
  for i in range(1, n-1):
    if a[i] == comm_num:
      b.add(comm_num)
  return b

s = [3, 6, 7, 9, 3, 5, 6]
find_comm(s)


# second trial
def find_comm2(a):
  new_set = set()
  n = len(a)
  for i in range(0, n-1):
    for j in range(i+1, n):
      if a[i] == a[j]:
        new_set.add(a[i])
  return new_set

s = [3, 6, 7, 9, 3, 5, 6]
print(find_comm2(s))
        

# pr_03_1 : n명 중 2명을 뽑아 짝 만들기

def distin(a):
  n = len(a)
  new_set = set()
  for i in range(0, n-1):
    for j in range(i+1, n):
      v = print(a[i] + " - " + a[j])
      new_set.add(v)

s = ["Jane", "Max", "Con", "Hun"]
print(distin(s))
