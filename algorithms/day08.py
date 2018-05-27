# 선택 정렬

# frist trial: err:

def sort_select(a):
  n = len(a)
  v = []
  s = 0

  for i in range(0, n-1):
    for j in range(1, n):
      if a[i] > a[j]:
        s = j
        return v.append(a[s])
      return v.append(a[s])
  return v

x = [2, 4, 5, 1, 3]
print(sort_select(x))
