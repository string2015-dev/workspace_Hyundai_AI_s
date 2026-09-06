#8 두 딕셔너리 병합하기
menu1 = {"커피": 4000, "라떼": 4500}
menu2 = {"라떼": 5000, "쿠키": 3000}

# 강사님 코드
# 기존 데이터는 백업해두는게 좋다! 그럴떄 어떤 함수를 사용해야할까??? < 찾아보기

merged = menu1.copy()
merged.update(menu2)
# 원본을 살리기 위해서 .copy() 함수로 원본을 복사해와 거기서 작업한다.
# .update()를 사용해서 정보를 업데이트 한다.
for name,price in merged.items():
    print(f"새롭게 리뉴얼된 메뉴 {name}:{price}")

print(menu1)
print(menu2)
print()
# 컴프리헨션 형태
merged2 = {k:v for d in (menu1,menu2) for k,v in d.items()}
print(merged2)