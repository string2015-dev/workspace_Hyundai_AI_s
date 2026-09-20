use bookstore;
insert into book_order values
('O011','BK006','서준호',2,'2025-08-14','2025-08-18','2025-08-19'),
('O012','BK009','한소연',1,'2025-08-15','2025-08-19','2025-08-20'),
('O013','BK001','김도윤',3,'2025-08-16','2025-08-20','2025-08-21'),
('O014','BK010','박지훈',2,'2025-08-17','2025-08-21','2025-08-27'),
('O015','BK003','정하늘',1,'2025-08-18','2025-08-22','2025-08-23'),
('O016','BK006','이수민',4,'2025-08-19','2025-08-23','2025-08-24');

-- 문제 1  전체 도서 수 세기
-- [난이도: 기초]  [학습 함수: COUNT(*)]
-- 서점 관리자 대시보드 상단에 "현재 등록된 전체 도서 수" 배지를 보여주려고 합니다.
-- 요구사항 : book 테이블에 등록된 전체 도서의 개수를 '전체도서수' 라는 별명으로 조회하시오.
select count(*) 전체도서수
from book;
-- 문제 2  취급 분야 수 세기
-- [난이도: 기초]  [학습 함수: COUNT(DISTINCT)]
-- 메인 화면의 카테고리 필터 버튼을 몇 개 만들어야 하는지 확인하려 합니다.
-- 요구사항 : book 테이블에 등록된 도서들의 분야(category)가 몇 종류인지 중복 없이 세어 '분야수' 라는 별명으로 조회하시오.
select count(distinct(category)) 
from book;

-- 문제 3  특정 분야 도서 수 세기
-- [난이도: 기초]  [학습 함수: COUNT(*), WHERE]
-- IT 자격증 특별전을 준비하며 몇 권이 진열 가능한지 먼저 확인해야 합니다.
-- 요구사항 : 분야(category)가 'IT'인 도서가 몇 권인지 'IT도서수' 라는 별명으로 조회하시오.
select count(category) IT도서수
from book
where category like '%IT%';

-- 문제 4  전체 재고 수량 합계
-- [난이도: 기초]  [학습 함수: SUM]
-- 창고 담당자가 전체 재고 현황을 경영진에게 보고해야 합니다.
-- 요구사항 : book 테이블에 있는 모든 도서의 재고수량(stock) 합계를 '전체재고수량' 이라는 별명으로 조회하시오.
select sum(stock) 전체재고수량
from book;

-- 문제 5  재고 부족 도서의 재고 합계
-- [난이도: 초급]  [학습 함수: SUM, WHERE]
-- 재고가 부족한 도서만 모아 추가 발주 수량을 가늠하려 합니다.
-- 요구사항 : 재고수량(stock)이 10권 미만인 도서들의 재고수량 합계를 '재고부족합계' 라는 별명으로 조회하시오.
select sum(stock) 재고부족합계
from book
where stock < 10;

-- 문제 6  전체 도서 평균 정가
-- [난이도: 기초]  [학습 함수: AVG, ROUND]
-- 가격 정책 회의를 위해 전체 도서의 평균 판매가를 파악하려 합니다.
-- 요구사항 : book 테이블에 있는 모든 도서의 정가(price) 평균을 반올림한 정수값으로 '평균정가' 라는 별명으로 조회하시오.
select round(avg(price),0) 평균정가
from book;

-- 문제 7  최고가·최저가 도서 가격
-- [난이도: 기초]  [학습 함수: MAX, MIN]
-- 프로모션 배너에 "최저 OO원부터"라는 문구를 넣기 위해 가격 범위를 확인합니다.
-- 요구사항 : book 테이블에서 가장 비싼 도서의 가격과 가장 저렴한 도서의 가격을 각각 '최고가', '최저가' 라는 별명으로 함께 조회하시오.
select max(price) 최고가, min(price) 최저가
from book;

-- 문제 8  전체 재고 자산 가치 계산
-- [난이도: 초급]  [학습 함수: SUM, 산술연산자]
-- 재무팀에서 현재 창고에 쌓여 있는 도서 재고의 총 자산 가치(정가 기준)를 요청했습니다.
-- 요구사항 : 모든 도서에 대해 '정가 × 재고수량'을 계산한 값의 총합을 '재고자산총액' 이라는 별명으로 조회하시오.
desc book;
select sum(price*stock) 재고자산총액
from book;

-- 문제 9  분야별 도서 수 집계
-- [난이도: 초급]  [학습 함수: GROUP BY, COUNT]
-- 분야별로 도서가 몇 권씩 있는지 한눈에 파악하는 표를 만들어야 합니다.
-- 요구사항 : 분야(category)별로 도서 수를 세어 '분야', '도서수' 컬럼으로 조회하되, 도서수가 많은 순서로 정렬하시오.
desc book;
-- select category as 분야, sum(stock) as 도서수
select category 분야, count(*) 도서수
from book
group by category
order by sum(stock) desc;

-- 문제 10  분야별 평균 정가 집계
-- [난이도: 초급]  [학습 함수: GROUP BY, AVG, ROUND]
-- 어느 분야가 상대적으로 고가 도서 위주인지 분석하려 합니다.
-- 요구사항 : 분야(category)별 평균 정가를 반올림한 정수값으로 조회하고, 평균 정가가 높은 순서로 정렬하시오. 컬럼명은 '분야', '평균정가'로 하시오.
select category 분야, round(avg(price),0) 평균정가
from book
group by category
order by 2 desc;

-- 문제 11  분야별 재고 합계 집계
-- [난이도: 초급]  [학습 함수: GROUP BY, SUM]
-- 어느 분야의 재고가 가장 많이 쌓여있는지 확인하려 합니다.
-- 요구사항 : 분야(category)별 재고수량 합계를 '분야', '재고합계' 컬럼으로 조회하고, 재고합계가 많은 순서로 정렬하시오.
select category 분야, sum(stock) 재고합계
from book
group by category
order by 2 desc;

-- 문제 12  분야별 최고가-최저가 격차 분석
-- [난이도: 중급]  [학습 함수: GROUP BY, MAX, MIN, 산술연산자]
-- 분야마다 가격 편차가 얼마나 되는지 분석해서 가격 정책에 참고하려 합니다.
-- 요구사항 : 분야(category)별로 '최고가-최저가'를 계산한 값을 '분야', '가격격차' 컬럼으로 조회하고, 가격격차가 큰 순서로 정렬하시오.
select category 분야, max(price)-min(price) 가격격차
from book
group by category;

-- 문제 13  2권 이상 계약된 출판사 찾기
-- [난이도: 중급]  [학습 함수: GROUP BY, HAVING, COUNT]
-- 여러 권을 함께 계약한 "주요 거래 출판사" 목록을 뽑아 관계 관리에 활용하려 합니다.
-- 요구사항 : 출판사(publisher)별 출간 도서 수를 구하되, 2권 이상 출간한 출판사만 '출판사', '출간도서수' 컬럼으로 조회하고, 출간도서수가 많은 순서로 정렬하시오.
select publisher 출판사, count(*) 출간도서
from book
group by publisher
having count(*) >=2
order by 2 desc;

-- 문제 14  평균 정가가 높은 프리미엄 분야 찾기
-- [난이도: 중급]  [학습 함수: GROUP BY, HAVING, AVG]
-- 평균 단가가 높은 분야를 "프리미엄 코너"로 별도 구성하려 합니다.
-- 요구사항 : 분야(category)별 평균 정가를 구하되, 평균 정가가 18,000원 이상인 분야만 '분야', '평균정가' 컬럼으로 조회하고, 
-- 평균정가가 높은 순서로 정렬하시오.
select category 분야, round(avg(price),0) 평균정가
from book
group by category
having avg(price)
order by 2 desc;

-- 문제 15  재고가 확보된 도서만 대상으로 한 분야별 평균 재고 분석
-- [난이도: 중급]  [학습 함수: WHERE, GROUP BY, HAVING, AVG]
-- 품절 임박(재고 5권 미만) 도서는 통계를 왜곡할 수 있어 제외하고, 안정적으로 재고가 있는 분야만 분석하려 합니다.
-- 요구사항 : 재고수량(stock)이 5권 이상인 도서만을 대상으로 분야별 평균 재고수량을 구하되, 
-- 평균 재고수량이 20권 이상인 분야만 '분야', '평균재고' 컬럼으로 조회하시오.
select category 분야, round(avg(stock),0) 평균재고
from book
where stock >=5
group by category
having avg(stock) >=20;

-- 문제 16  단독으로 존재하는 분야 찾기
-- [난이도: 중급]  [학습 함수: GROUP BY, HAVING, COUNT]
-- 도서가 1권밖에 없는 분야는 상품 다양성이 부족하므로 큐레이션 보강이 필요한지 검토하려 합니다.
-- 요구사항 : 분야(category)별 도서 수를 구하되, 도서가 정확히 1권뿐인 분야만 '분야', '도서수' 컬럼으로 조회하시오.
select category 분야, count(*) 도서수
from book
group by category
having count(*) =1;

-- 문제 17  [종합] 가격대별 도서 수와 평균 재고 통계
-- [난이도: 심화]  [학습 함수: CASE, GROUP BY, COUNT, AVG]
-- Day2에서 배운 CASE문과 오늘 배운 집계 함수를 결합해, 가격대별 판매 전략 수립을 위한 통계 리포트를 만들려 합니다.
-- 요구사항 : 정가(price)가 15,000원 미만이면 '저가', 25,000원 이하면 '중가', 그 외에는 
-- '고가'로 분류하고, 가격대별 도서 수와 평균 재고수량(반올림)을 '가격대', '도서수', '평균재고' 컬럼으로 조회하시오. 도서수가 많은 순서로 정렬하시오.
select case
		when price < 15000 then '저가'
		when price <= 25000 then '중가'
		else '고가' 
    end as 가격대,
    count(*) 도서수,
    round(avg(stock),0) 평균재고
from book
group by 1
order by 3 desc;

-- 문제 18  전체 주문 현황 요약
-- [난이도: 기초]  [학습 함수: COUNT, SUM]
-- 최근 book_order 테이블에 주문 데이터가 쌓이기 시작했습니다. 전체 주문 현황을 요약 보고하려 합니다.
-- 요구사항 : book_order 테이블의 전체 주문 건수와 총 주문 수량(qty의 합)을 각각 '전체주문건수', '총주문수량' 이라는 별명으로 함께 조회하시오.
select count(order_id) 전체주문건수, sum(qty) 총주문수량
from book_order;

-- 문제 19  재주문(반복 주문)이 발생한 도서 찾기
-- [난이도: 중급]  [학습 함수: GROUP BY, HAVING, COUNT, SUM]
-- 어떤 도서가 반복적으로 주문되는 "스테디셀러" 후보인지 확인하려 합니다.
-- 요구사항 : 도서코드(book_id)별로 주문건수와 총주문수량(qty 합계)을 구하되, 
-- 주문건수가 2건 이상인 도서만 '도서코드', '주문건수', '총주문수량' 컬럼으로 조회하고, 
-- 총주문수량이 많은 순서로 정렬하시오.
select book_id 도서코드, count(order_id) 주문건수, sum(qty) 총주문수량
from book_order
group by book_id
having count(order_id) >1
order by 3 desc;

-- 문제 20  [종합] 배송이 느린 우려 고객 찾기
-- [난이도: 심화]  [학습 함수: GROUP BY, HAVING, AVG, DATEDIFF]
-- 배송 만족도를 관리하기 위해, 평균적으로 배송이 오래 걸린 고객을 찾아 우선 관리 대상으로 선정하려 합니다.
-- 요구사항 : 고객명(customer_name)별로 주문건수와 [발송일-주문일]의 평균 소요일(반올림)을 구하되, 
-- 평균 소요일이 5일을 초과하는 고객만 '고객명', '주문건수', '평균배송소요일' 컬럼으로 조회하고, 
-- 평균배송소요일이 큰 순서로 정렬하시오.
select customer_name 고객병, count(order_id) 주문건수, round(avg(ship_date -order_date),0) 평균배송소요일
from book_order
group by customer_name
having avg(ship_date -order_date) >5
order by 3 desc;