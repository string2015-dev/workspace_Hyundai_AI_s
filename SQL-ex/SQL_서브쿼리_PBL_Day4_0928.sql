USE bookstore;
 
select * from book;
select * from book_order;
select * from customer;

-- ================================================
-- 문제 1  평균 정가보다 비싼 도서 찾기
-- [난이도: 기초]  [학습 포인트: 단일행 서브쿼리, WHERE]
-- 전체 도서의 평균 가격이 얼마인지는 알지만, "평균보다 비싼 책"이 구체적으로 어떤 책들인지는 한 번의 쿼리로 바로 알 수 없습니다.
-- 요구사항 : book 테이블에서 전체 평균 정가(price)보다 비싼 도서의 도서명, 정가를 정가가 높은 순으로 조회하시오.
select title 도서명, price 정가
from book
where book.price > (select avg(price) from book)
order by 정가 desc;
-- ================================================
-- 문제 2  가장 비싼 도서 찾기(서브쿼리 방식)
-- [난이도: 기초]  [학습 포인트: 단일행 서브쿼리, MAX]
-- "가장 비싼 책이 무엇인가?"라는 질문에 MAX() 하나만으로는 "가격"만 알 수 있고, 어떤 "책"인지는 알 수 없습니다.
-- 요구사항 : book 테이블에서 정가가 전체 최고가와 같은 도서의 도서명, 정가를 조회하시오.
select title 도서명, price 정가
from book
where book.price = (select max(price) from book);
-- ================================================
-- 문제 3  재고가 가장 적은 도서 찾기
-- [난이도: 기초]  [학습 포인트: 단일행 서브쿼리, MIN]
-- 품절 위험이 가장 큰 도서, 즉 재고가 가장 적은 책을 먼저 확인해 긴급 발주를 검토하려 합니다.
-- 요구사항 : book 테이블에서 재고수량(stock)이 전체 최솟값과 같은 도서의 도서명, 재고수량을 조회하시오.
select title 도서명, stock 재고수량
from book
where book.stock = (select min(stock) from book);
-- ================================================
-- 문제 4  특정 도서보다 비싼 도서 목록
-- [난이도: 초급]  [학습 포인트: 단일행 서브쿼리(특정 행 값)]
-- 베스트셀러인 "처음 배우는 MySQL"(BK001)보다 비싼 프리미엄 도서들만 따로 모아 진열하려 합니다.
-- 요구사항 : 도서코드(book_id)가 'BK001'인 도서의 정가보다 비싼 도서의 도서명, 정가를 정가가 높은 순으로 조회하시오.
select title 도서명, price 정가
from book
where book.price > (select price from book where book_id ='BK001')
order by 정가 desc;
-- ================================================
-- 문제 5  실제로 주문된 적 있는 도서 목록
-- [난이도: 초급]  [학습 포인트: 다중행 서브쿼리, IN]
-- 전체 도서 중에서 "실제로 한 번이라도 팔린 적 있는 책"만 골라 베스트 진열대 후보로 검토하려 합니다.
-- 요구사항 : book_order 테이블에 주문 기록이 있는 도서코드(book_id)에 해당하는 도서의 도서코드, 도서명을 도서코드 순으로 조회하시오.
select book_id 도서코드, title 도서명
from book
where book.book_id in(select distinct book_id from book_order)
order by book_id;
-- ================================================
-- 문제 6  한 번도 주문되지 않은 도서 목록(서브쿼리 방식)
-- [난이도: 초급]  [학습 포인트: 다중행 서브쿼리, NOT IN]
-- 앞서 JOIN(LEFT JOIN + IS NULL)으로 풀었던 문제를 이번에는 서브쿼리 방식으로 다시 풀어봅니다.
-- 요구사항 : book_order 테이블에 주문 기록이 없는 도서의 도서코드, 도서명을 도서코드 순으로 조회하시오.
select book_id 도서코드, title 도서명
from book
where book.book_id not in(select distinct book_id from book_order)
order by book_id;
-- ================================================
-- 문제 7  VIP 고객이 주문한 내역 조회
-- [난이도: 초급]  [학습 포인트: 다중행 서브쿼리, IN]
-- VIP 고객들만 골라 그들의 주문 내역을 별도로 관리하려 합니다.
-- 요구사항 : customer 테이블에서 등급(grade)이 'VIP'인 고객명을 서브쿼리로 구한 뒤, 그 고객들의 주문 내역(주문번호, 고객명, 수량)을 book_order에서 조회하시오.
select o.order_id 주문번호, o.customer_name 고객명, o.qty 수량
from book_order o
where o.customer_name in(select distinct customer_name from customer where grade = 'VIP');
-- ================================================
-- 문제 8  주문 이력이 전혀 없는 고객 찾기(서브쿼리 방식)
-- [난이도: 초급]  [학습 포인트: 다중행 서브쿼리, NOT IN]
-- 12번(LEFT JOIN) 문제와 동일한 목표를 서브쿼리로 다시 풀어, 두 방식의 결과가 똑같이 나오는지 검증합니다.
-- 요구사항 : book_order에 주문 기록이 없는 고객의 고객코드, 고객명을 customer 테이블에서 조회하시오.
select c.customer_id 고객코드, c.customer_name 고객명
from customer c
where c.customer_name not in(select distinct customer_name from book_order);
-- ================================================
-- 문제 9  배송이 지연된 주문의 도서 목록
-- [난이도: 중급]  [학습 포인트: 다중행 서브쿼리, IN, DATEDIFF]
-- 배송 지연이 자주 발생하는 도서가 물류 처리에 특별히 오래 걸리는 책인지 확인하려 합니다.
-- 요구사항 : book_order에서 [발송일-요청일]이 3일 이상인 주문의 도서코드를 서브쿼리로 구한 뒤, 해당 도서의 도서코드, 도서명을 book에서 조회하시오.
select b.book_id 도서코드, b.title 도서명
from book b
where b.book_id in(select book_id from book_order where datediff(ship_date,request_date) >= 3);
-- ================================================
-- 문제 10  스테디셀러 후보 도서 찾기(서브쿼리+GROUP BY)
-- [난이도: 중급]  [학습 포인트: 다중행 서브쿼리, IN, GROUP BY/HAVING]
-- 누적 주문수량이 많은 "스테디셀러 후보" 도서를 골라 재입고 우선순위를 정하려 합니다.
-- 요구사항 : book_order에서 도서코드별 총주문수량(qty 합계)이 5 이상인 도서코드를 서브쿼리로 구한 뒤, 해당 도서의 도서코드, 도서명을 book에서 도서코드 순으로 조회하시오.
SELECT b.book_id 도서코드, b.title 도서명
FROM book b
WHERE b.book_id IN(SELECT book_id FROM book_order GROUP BY book_id HAVING sum(qty) >=5);
-- ================================================
-- 문제 11  에세이 도서 중 한 권보다는 비싼 도서(ANY)
-- [난이도: 중급]  [학습 포인트: ANY(다중행 비교 연산자)]
-- "에세이 분야에도 나름 비싼 책이 있는데, 그 중 아무거나 하나보다만 비싸도 프리미엄 후보로 보고 싶다"는 다소 느슨한 조건을 적용하려 합니다.
-- 요구사항 : 정가가 에세이(category='에세이') 분야 도서 중 최소 하나보다는 비싼 도서의 도서명, 분야, 정가를 정가가 높은 순으로 조회하시오. (ANY 연산자 활용)
SELECT b.title 도서명, b.category 분야, b.price 정가
FROM book b
WHERE b.price > ANY (SELECT price FROM book WHERE category ='에세이')
ORDER BY 정가 desc;
-- ================================================
-- 문제 12  에세이 도서 전체보다 비싼 프리미엄 도서(ALL)
-- [난이도: 중급]  [학습 포인트: ALL(다중행 비교 연산자)]
-- 이번에는 "에세이 분야의 가장 비싼 책보다도 더 비싼, 진짜 프리미엄 도서"만 엄격하게 골라내려 합니다.
-- 요구사항 : 정가가 에세이 분야 도서 전체보다 비싼 도서의 도서명, 분야, 정가를 정가가 높은 순으로 조회하시오. (ALL 연산자 활용)
SELECT b.title 도서명, b.category 분야, b.price 정가
FROM book b
WHERE b.price > All (SELECT price FROM book WHERE category ='에세이')
ORDER BY 정가 desc;
-- ================================================
-- 문제 13  IT 분야보다 재고가 적은 위험 도서(ALL)
-- [난이도: 중급]  [학습 포인트: ALL(다중행 비교 연산자)]
-- IT 분야는 회전율이 빨라 재고를 넉넉히 유지하는 편인데, IT 분야의 어떤 책보다도 재고가 적은 "정말 위험한" 도서를 찾아 긴급 발주하려 합니다.
-- 요구사항 : 재고수량(stock)이 IT 분야 도서 전체보다 적은 도서의 도서명, 분야, 재고수량을 재고수량이 적은 순으로 조회하시오. (ALL 연산자 활용)
SELECT b.title 도서명, b.category 분야, b.stock 재고수량
FROM book b
WHERE b.stock < All (SELECT stock FROM book WHERE category ='IT')
ORDER BY 재고수량 asc;
-- ================================================
-- 문제 14  주문 이력이 있는 고객 찾기(EXISTS)
-- [난이도: 중급]  [학습 포인트: 상관 서브쿼리, EXISTS]
-- "이 고객이 주문을 한 적이 있는가?"라는 질문에 IN 대신 EXISTS로 답해보는 연습을 합니다.
-- 요구사항 : customer 테이블에서 book_order에 주문 기록이 존재하는 고객의 고객코드, 고객명을 EXISTS를 사용하여 조회하시오.
SELECT c.customer_id 고객코드, c.customer_name 고객명
FROM customer c
WHERE EXISTS(SELECT customer_name FROM book_order o WHERE o.customer_name = c.customer_name);
-- ================================================
-- 문제 15  주문 이력이 없는 고객 찾기(NOT EXISTS)
-- [난이도: 중급]  [학습 포인트: 상관 서브쿼리, NOT EXISTS]
-- 8번(NOT IN)에서 풀었던 것과 같은 목표를, 이번에는 실무에서 더 안전하다고 알려진 NOT EXISTS로 다시 풀어봅니다.
-- 요구사항 : customer 테이블에서 book_order에 주문 기록이 없는 고객의 고객코드, 고객명을 NOT EXISTS를 사용하여 조회하시오.
SELECT * FROM customer left join book_order on customer.customer_name = book_order.customer_name;

SELECT c.customer_id 고객코드, c.customer_name 고객명
FROM customer c
WHERE NOT EXISTS(SELECT customer_name FROM book_order o WHERE o.customer_name = c.customer_name);
-- ================================================
-- 문제 16  주문된 적 있는 도서 찾기(EXISTS, book 기준)
-- [난이도: 중급]  [학습 포인트: 상관 서브쿼리, EXISTS]
-- 5번(IN)에서 풀었던 문제를 이번에는 EXISTS로 다시 풀며, book_id 기준 상관 서브쿼리를 연습합니다.
-- 요구사항 : book 테이블에서 book_order에 주문 기록이 존재하는 도서의 도서코드, 도서명을 EXISTS를 사용하여 도서코드 순으로 조회하시오.
SELECT b.book_id 도서코드, b.title 도서명
FROM book b
WHERE EXISTS(SELECT o.book_id FROM book_order o WHERE o.book_id = b.book_id)
ORDER BY 도서코드 ASC;
-- ================================================
-- 문제 17  주문된 적 없는 도서 찾기(NOT EXISTS, book 기준)
-- [난이도: 중급]  [학습 포인트: 상관 서브쿼리, NOT EXISTS]
-- 6번(NOT IN)에서 풀었던 문제를 NOT EXISTS로 다시 풀어, 세 가지 방법(LEFT JOIN, NOT IN, NOT EXISTS)의 결과가 모두 같은지 최종 확인합니다.
-- 요구사항 : book 테이블에서 book_order에 주문 기록이 전혀 없는 도서의 도서코드, 도서명을 NOT EXISTS를 사용하여 도서코드 순으로 조회하시오.
SELECT b.book_id 도서코드, b.title 도서명
FROM book b
WHERE NOT EXISTS(SELECT o.book_id FROM book_order o WHERE o.book_id = b.book_id)
ORDER BY 도서코드 ASC;
-- ================================================
-- 문제 18  같은 분야 평균보다 비싼 도서(상관 서브쿼리)
-- [난이도: 심화]  [학습 포인트: 상관 서브쿼리, AVG]
-- "전체 평균"이 아니라 "자기가 속한 분야 안에서" 평균보다 비싼, 즉 "분야별 프리미엄 도서"를 찾으려 합니다.
-- 요구사항 : book 테이블에서 각 도서의 정가가 자신이 속한 분야(category)의 평균 정가보다 비싼 도서의 도서명, 분야, 정가를 분야, 정가 내림차순으로 조회하시오.
SELECT 
    b.title AS 도서명, 
    b.category AS 분야, 
    b.price AS 정가
FROM book b
WHERE b.price > (
    SELECT AVG(sub.price) 
    FROM book sub 
    WHERE sub.category = b.category
)
ORDER BY 정가 DESC,분야 DESC;
-- ================================================
-- 문제 19  분야별 최저 재고 도서 찾기(상관 서브쿼리)
-- [난이도: 심화]  [학습 포인트: 상관 서브쿼리, MIN]
-- 분야마다 "그 분야 안에서 가장 재고가 부족한 책"이 무엇인지 한 번에 뽑아 분야별 담당자에게 전달하려 합니다.
-- 요구사항 : book 테이블에서 각 도서의 재고수량이 자신이 속한 분야의 최소 재고수량과 같은 도서의 도서명, 분야, 재고수량을 분야 순으로 조회하시오.
SELECT b.title 도서명, b.category 분야, b.stock 재고수량
FROM book b
WHERE b.stock = (SELECT MIN(stock) FROM book sub WHERE sub.category = b.category)
ORDER BY 분야 ASC;
-- ================================================
-- 문제 20  전체 평균가 대비 각 도서의 가격 차이
-- [난이도: 중급]  [학습 포인트: SELECT절 스칼라 서브쿼리]
-- 각 도서가 전체 평균보다 얼마나 비싸거나 싼지, 그 "차액"을 도서 목록과 나란히 보여주는 리포트를 만들려 합니다.
-- 요구사항 : book 테이블의 모든 도서에 대해 도서명, 정가와 함께 전체평균가, 그리고 (정가-전체평균가)인 평균과의차이를 함께 조회하고, 차이가 큰 순서로 정렬하시오.
SELECT b.title 도서명, b.price 정가, (SELECT AVG(price) FROM book) 전체평균가, b.price-(SELECT AVG(price) FROM book) as '평균과차이'
FROM book b
ORDER BY 평균과차이 DESC;
-- ================================================
-- 문제 21  도서별 총주문수량을 함께 보여주기
-- [난이도: 중급]  [학습 포인트: SELECT절 상관 스칼라 서브쿼리, IFNULL]
-- 전체 도서 목록 옆에, 각 도서가 지금까지 몇 권이나 주문되었는지 "요약 수치"를 나란히 붙여서 보여주고 싶습니다.
-- 요구사항 : book 테이블의 모든 도서에 대해 도서명과 함께, 해당 도서의 book_order상 총주문수량(qty 합계, 주문이 없으면 0)을 조회하고, 총주문수량이 많은 순서로 정렬하시오.
SELECT b.title 도서명, ifnull((SELECT sum(o.qty) FROM book_order o WHERE o.book_id =b.book_id),0)as '총주문수량'
FROM book b
ORDER BY 총주문수량 DESC;
SELECT qty FROM book_order;
-- ================================================
-- 문제 22  고객별 총결제금액을 고객 목록에 함께 표시
-- [난이도: 심화]  [학습 포인트: SELECT절 상관 스칼라 서브쿼리(JOIN 포함)]
-- 전체 고객 명단(휴면 고객 포함)에 각자의 누적 결제금액을 나란히 붙여, 등급별 관리 대상을 한눈에 파악하려 합니다.
-- 요구사항 : customer 테이블의 모든 고객에 대해 고객명, 등급과 함께 해당 고객의 총결제금액(수량×정가×(1-할인율/100)의 합, 주문이 없으면 0, 반올림)을 조회하고, 총결제금액이 큰 순서로 정렬하시오.
SELECT c.customer_name 고객명, c.grade 등급, ifnull((SELECT round(sum(b.price*(1-b.discount_rate/100)*o.qty)) FROM book b join book_order o on b.book_id = o.book_id WHERE o.customer_name = c.customer_name),0) AS '총결제금액'
FROM customer c
ORDER BY 총결제금액 DESC;
-- ================================================
-- 문제 23  평균가가 높은 분야만 골라 도서 확인
-- [난이도: 중급]  [학습 포인트: FROM절 인라인뷰]
-- Day3에서 구했던 "분야별 평균가" 집계 결과 중, 평균가가 특히 높은 분야만 추려서 다시 살펴보려 합니다.
-- 요구사항 : 분야별 평균 정가(반올림)를 구한 결과를 서브쿼리로 만들고, 그 중 평균가가 18,000원 이상인 분야만 분야, 평균가로 조회하시오.
SELECT *
FROM (SELECT category 분야, round(avg(price)) 평균가격 FROM book GROUP BY category) AS 평균정가
WHERE 평균정가.평균가격 >= 18000;
-- ================================================
-- 문제 24  많이 팔린 도서 목록(인라인 뷰)
-- [난이도: 중급]  [학습 포인트: FROM절 인라인뷰]
-- 23번과 같은 방식으로, 이번에는 "많이 팔린 도서"를 인라인 뷰로 뽑아보는 연습입니다.
-- 요구사항 : 도서코드별 총주문수량을 구한 결과를 서브쿼리로 만들고, 그 중 총주문수량이 5 이상인 도서코드만 도서코드, 총주문수량으로 많은 순서로 조회하시오.
SELECT *
FROM (SELECT book_id 도서코드, ROUND(SUM(qty)) 총주문수량 FROM book_order GROUP BY book_id) AS sub
WHERE sub.총주문수량 >= 5
ORDER BY sub.총주문수량 desc;
-- ================================================
-- 문제 25  많이 팔린 도서의 이름 확인(인라인 뷰+JOIN)
-- [난이도: 심화]  [학습 포인트: FROM절 인라인뷰 + JOIN]
-- 24번 결과에는 도서코드만 있어 실제로 어떤 책인지 알기 어렵습니다. 도서명을 붙여서 담당자에게 전달할 최종본을 만들려 합니다.
-- 요구사항 : 도서코드별 총주문수량을 구한 서브쿼리 결과를 book과 조인하여, 도서명과 총주문수량을 총주문수량이 많은 순서로 조회하시오.
SELECT b.title 도서명, sub.총주문수량
FROM book b,
	(SELECT book_id 도서코드, ROUND(SUM(qty)) 총주문수량 FROM book_order GROUP BY book_id) AS sub
WHERE b.book_id = sub.도서코드
ORDER BY sub.총주문수량 desc;
-- ================================================
-- 문제 26  [종합] 평균가 높은 분야의 도서만 모아보기
-- [난이도: 심화]  [학습 포인트: IN + GROUP BY/HAVING + 스칼라 서브쿼리]
-- 23번에서 찾은 "평균가 18,000원 이상인 분야"를 이번에는 "전체 평균보다 비싼 분야"라는 상대적 기준으로 바꾸고, 그 분야에 속한 개별 도서들까지 모두 보여주는 종합 리포트를 만들려 합니다.
-- 요구사항 : 분야별 평균 정가가 전체 평균 정가 이상인 분야에 속한 도서들의 도서명, 분야, 정가를 분야, 정가 내림차순으로 조회하시오.
SELECT b.title 도서명, b.category 분야, b.price 정가
FROM book b, (SELECT category 분야, round(avg(price)) 평균가격 FROM book GROUP BY category) AS 평균정가
WHERE b.category = 평균정가.분야 and 평균정가.평균가격>= (SELECT AVG(price) FROM book)
ORDER BY 정가 DESC;
-- --------------------------------------------------------------------------
SELECT b.title 도서명, b.category 분야, b.price 정가
FROM book b
WHERE b.category in(SELECT category FROM book GROUP BY category HAVING AVG(price) >= (SELECT AVG(price) FROM book))
ORDER BY 정가 DESC;

-- ================================================
-- 문제 27  [종합] 배송 지연을 경험한 고객 찾기
-- [난이도: 심화]  [학습 포인트: 상관 서브쿼리, EXISTS, DATEDIFF]
-- 배송 지연을 한 번이라도 겪은 고객에게는 사과 쿠폰을 발송해 고객 이탈을 방지하려 합니다.
-- 요구사항 : customer 테이블에서, 3일 이상 배송이 지연된 주문을 한 번이라도 한 적 있는 고객의 고객코드, 고객명을 EXISTS를 사용하여 조회하시오.
SELECT c.customer_id 고객코드, c.customer_name 고객명
FROM customer c
WHERE EXISTS(SELECT customer_name FROM book_order WHERE c.customer_name= book_order.customer_name AND datediff(ship_date,request_date) >= 3);
-- ================================================
-- 문제 28  [종합] 분야별 최고가 도서 한눈에 보기
-- [난이도: 심화]  [학습 포인트: 행 값 서브쿼리(Row Subquery)]
-- 각 분야를 대표하는 "분야별 최고가 도서"들만 모아 프리미엄 큐레이션 코너를 구성하려 합니다.
-- 요구사항 : 분야(category)별 최고 정가를 구한 뒤, (분야, 정가) 조합이 그 목록에 해당하는 도서의 도서명, 분야, 정가를 정가가 높은 순서로 조회하시오.
SELECT category, max(price) FROM book GROUP BY category;
SELECT b.title 도서명, b.category 분야, b.price 정가
FROM book b, (SELECT category, max(price) 최고가 FROM book GROUP BY category) AS max값
WHERE b.price = max값.최고가
ORDER BY 정가 DESC;
-- ================================================
-- 문제 29  [종합] 고객별 최근 주문일 확인
-- [난이도: 중급]  [학습 포인트: SELECT절 상관 스칼라 서브쿼리, MAX]
-- 오랫동안 주문이 없는 "이탈 위험 고객"을 파악하기 위해, 전체 고객의 가장 최근 주문일을 한눈에 정리하려 합니다.
-- 요구사항 : customer 테이블의 모든 고객에 대해 고객명과 함께 book_order상 최근주문일(order_date의 최댓값, 주문이 없으면 NULL)을 조회하고, 최근주문일이 최신인 순서로 정렬하시오.
SELECT max(order_date) FROM book_order GROUP BY customer_name;

SELECT c.customer_name 고객명, 고객최근주문.최근주문일
FROM customer c
left join (SELECT max(order_date) 최근주문일, customer_name FROM book_order GROUP BY customer_name) AS 고객최근주문 ON c.customer_name = 고객최근주문.customer_name
ORDER BY 최근주문일 DESC;
-- ================================================
-- 문제 30  [종합] 평균 이상으로 결제한 우수 고객 찾기
-- [난이도: 심화]  [학습 포인트: FROM절 인라인뷰(이중), 스칼라 서브쿼리]
-- 전체 고객의 "평균적인 결제금액"보다 더 많이 결제한 고객만 선별하여 특별 감사 이벤트 대상자로 지정하려 합니다.
-- 요구사항 : 고객별 총결제금액을 구한 뒤, 그 값이 전체 고객의 평균 총결제금액보다 큰 고객의 고객명, 총결제금액을 총결제금액이 큰 순서로 조회하시오.

# => 고객별 총결제 금액
select round(sum(o.qty*b.price)) 총결제금액
from book_order o,
	(select book_id, price from book) as b
 where b.book_id = o.book_id
 group by o.customer_name;
 # => 전체 고객의 평균 총결제금액은 고객별 총 결제금액을 인라인 뷰로 받아서 avg해버리자!
select round(avg(고객별총결제금액)) 전체_고객_평균_총결제금액
from book_order o,
	(select o.customer_name, sum(b.price*o.qty) 고객별총결제금액
		from book_order o
		join book b
		on b.book_id = o.book_id
		group by o.customer_name) as totalpay
 where totalpay.customer_name = o.customer_name;
-- ------------------------------------------------------------------
# 3ck 시도.
select o.customer_name 고객명, round(sum(b.price*o.qty*(1-b.discount_rate/100))) 총결제금액
from book_order o
inner join book b on o.book_id = b.book_id
group by o.customer_name
having sum(b.price*o.qty*(1-b.discount_rate/100)) > (select round(avg(고객별총결제금액)) 전체_고객_평균_총결제금액
														from book_order o,
															(select o.customer_name, sum(b.price*o.qty*(1-b.discount_rate/100)) 고객별총결제금액
																from book_order o
																join book b
																on b.book_id = o.book_id
																group by o.customer_name) as totalpay
														 where totalpay.customer_name = o.customer_name)
 order by 총결제금액 desc;

# 2차 시도 안됨... 거의 다 왔는데...!
select customer_name 고객명, sum(price*qty) 총결제금액
from book_order
join book on book_order.book_id = book.book_id
WHERE o.customer_name = book_order.customer_name and (select round(sum(o.qty*b.price)) 총결제금액
		from book_order o,
			(select book_id, price from book) as b
		 where b.book_id = o.book_id
		 group by o.customer_name) 
         > all (select round(avg(고객별총결제금액)) 전체_고객_평균_총결제금액
				from book_order o,
					(select o.customer_name, sum(b.price*o.qty) 고객별총결제금액
						from book_order o
						join book b
						on b.book_id = o.book_id
						group by o.customer_name) as totalpay
				 where totalpay.customer_name = o.customer_name)
group by book_order.customer_name;

 
 -- # 1차 시도 답이 안나옴... 왤까!
 select o.customer_name, sum(b.price*o.qty) 총결제금액
 from book_order o
 join book b
 on b.book_id = o.book_id
 group by o.customer_name
 having avg(b.price*o.qty) > (select avg(book.price*orde.qty) from book_order orde join book on book.book_id = orde.book_id);
 -- --------------------------------------
select round(avg(고객별총결제금액)) 전체_고객_평균_총결제금액
														from book_order o,
															(select o.customer_name, sum(b.price*o.qty*(1-b.discount_rate/100)) 고객별총결제금액
																from book_order o
																join book b
																on b.book_id = o.book_id
																group by o.customer_name) as totalpay
														 where totalpay.customer_name = o.customer_name;
 -- -------------------------------------------
