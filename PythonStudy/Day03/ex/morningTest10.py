# #10 계산기 오류 디버깅
# 아래 코드는 TypeError가 발생합니다. 오류의 원인을 설명하고, 오류를 해결한 전체 코드를 작성하세요.
price = input("상품 가격을 입력하세요: ")
quantity = input("수량을 입력하세요: ")
total = int(price) * int(quantity)
print("총 금액: " + str(total))