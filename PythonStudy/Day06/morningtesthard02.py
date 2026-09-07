# 온라인 쇼핑몰 장바구니 계산기
# 정바구니에 답긴 상품("이름", "가격", "수량")의 총 결제 금액을 계산합니다.
cart = [      {"상품명": "키보드", "가격": 50000, "수량": 1},      
          {"상품명": "마우스", "가격": 20000, "수량": 2},  ]
def calculate_total(data_list):
    total = sum([price["가격"]*price["수랑"] for price in data_list])
    return total
