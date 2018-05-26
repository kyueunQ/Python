# 하노이이의 탑 옮기기
# 총 n개의 블록으로 이뤄진 탑
# ① 맨 바닥의 n번째를 남겨두고, 우선 그 n-1개의 블록을 여러 과정을 거쳐서 1번 기둥 → 2번 기둥
# ② 맨 바닥의 n번째 블록을 1번 기둥 → 3번 기둥
# ③ n-1개의 블록들을 2번 기둥 → 3번 기둥
# 탑 옮기기 종료

def move_tower(n, start_pole, end_pole, sub_pole):
  # 종료 
  if n == 1:
    print(start_pole, "->", end_pole)
    return

  
  # ① : 목표 기둥이 2번째(sub_pole) 
  move_tower(n-1, start_pole, sub_pole, end_pole)
  # ② : 맨 바닥의 n번째 블록 이동
  print(start_pole, "->", end_pole)
  # ③ : 목표 기둥이 3번째(end_pole)
  move_tower(n-1, sub_pole, end_pole, start_pole)


move_tower(3, 1, 3, 2)
print("------------------")
move_tower(7, 1, 3, 2)
