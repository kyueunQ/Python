# 회문 찾기
# 큐와 스택
# : 자료를 넣고 일렬로 보관하는 것은 동일하지만, 자료를 빼는 방식이 다름

# 큐 : First In First Out
# 스택 : Last In First Out
# 따라서 큐 방식을 Out한 데이터와 스택 방식으로 Out한 데이터가 동일하면 회문임

def same (a) :
  # 배열 정의 (큐, 스택방식 각각의 결과물 저장)
  que = []
  stack = []
  for i in a:
    que.append(i.lower())
    stack.append(i.lower())
  # 큐 결과물 = 스택 결과물
    while que:
      if que.pop(0) == stack.pop():
       # 회문임을 알려줌
        print("회문")
      else:
        # 아니다면 아니라고 말해주기
        print("회문이 아닙니다.")

print(same("JON"))


# 큐와 스택을 이용하지 않은 회문 
word = input("문자를 입력하세요: ")
ww = word.replace(" ", "") 
w = ww.lower()
r= w[::-1]

if w == r:
    print(w + " is Palindrome")
else:
    print(w + " is not Palindrome")
