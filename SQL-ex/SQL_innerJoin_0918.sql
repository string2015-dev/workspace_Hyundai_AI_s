USE bookstore;
 
CREATE TABLE customer (
  customer_id   VARCHAR(10) PRIMARY KEY,
  customer_name VARCHAR(50),
  grade         VARCHAR(10),   -- 'VIP' 또는 '일반'
  join_date     DATE
);
 
-- customer.csv (12명, 전체 컬럼)를 Table Data Import Wizard로 가져오세요.
-- 또는 아래처럼 INSERT문으로 직접 입력해도 됩니다.
INSERT INTO customer VALUES
('C01','김도윤','VIP','2024-01-15'),
('C02','이수민','일반','2024-03-22'),
('C03','박지훈','VIP','2023-11-05'),
('C04','최유진','일반','2024-05-10'),
('C05','정하늘','일반','2024-02-18'),
('C06','한소연','VIP','2023-09-30'),
('C07','오세훈','일반','2024-06-01'),
('C08','강민재','일반','2024-04-14'),
('C09','윤아름','VIP','2024-07-20'),
('C10','서준호','일반','2024-08-02'),
('C11','이하늘','일반','2024-08-15'),
('C12','정민준','VIP','2024-08-20');
commit;
-- 커밋으로 확인한 것 필요하다!
-- 신규 주문 데이터 추가
INSERT INTO book_order VALUES
('O017','BK005','김도윤',1,'2025-08-20','2025-08-24','2025-08-23'),
('O018','BK013','이수민',2,'2025-08-20','2025-08-24','2025-08-25'),
('O019','BK020','박지훈',1,'2025-08-21','2025-08-25','2025-08-30'),
('O020','BK002','최유진',2,'2025-08-21','2025-08-25','2025-08-26'),
('O021','BK017','정하늘',1,'2025-08-22','2025-08-26','2025-08-26'),
('O022','BK016','한소연',3,'2025-08-22','2025-08-26','2025-08-31'),
('O024','BK006','강민재',2,'2025-08-23','2025-08-27','2025-08-28'),
('O026','BK013','서준호',1,'2025-08-24','2025-08-28','2025-08-31');
select * from customer;
select * from book_order;
select count(*) from book_order;

-- ====================================================================
-- 문제 1  주문-도서 기본 연결(INNER JOIN)
-- [난이도: 기초]  [학습 포인트: INNER JOIN, ON]
-- 북마루 서점에 book_order(주문) 테이블이 계속 쌓이고 있습니다.
-- 그런데 주문 테이블에는 도서명이 없고 book_id만 있어서, 주문 내역만 봐서는 어떤 책이 팔렸는지 알 수 없습니다.
-- 요구사항 : book_order 테이블과 book 테이블을 book_id 기준으로 연결하여 
-- 주문번호(order_id), 고객명(customer_name), 도서명(title), 수량(qty)을 조회하시오. 
-- 컬럼 별명은 '주문번호','고객명','도서명','수량'으로 하시오.
desc book;
desc book_order;

select book_order.order_id 주문번호, book_order.customer_name 고객명, book.title 도서명, book_order.qty 수량
from book
inner join book_order
on book.book_id = book_order.book_id;
-- ===================================================================
-- 문제 2  주문별 도서 정가 확인
-- [난이도: 기초]  [학습 포인트: INNER JOIN]
-- 주문 데이터에 정가 정보가 없어, 각 주문이 정가 기준으로 얼마짜리 거래였는지 알 수 없습니다.
-- 요구사항 : book_order와 book을 조인하여 
-- 주문번호, 고객명, 도서명, 정가(price)를 '주문번호','고객명','도서명','정가'로 조회하시오.
select book_order.order_id 주문번호, book_order.customer_name 고객명, book.title 도서명, book.price 정가
from book
inner join book_order
on book.book_id = book_order.book_id;
-- ===================================================================
-- 문제 3  IT 분야 도서 주문만 조회
-- [난이도: 기초]  [학습 포인트: INNER JOIN, WHERE]
-- IT 도서 프로모션 효과를 분석하기 위해 IT 분야 도서의 주문 내역만 따로 뽑아야 합니다.
-- 요구사항 : book_order와 book을 조인한 뒤, 분야(category)가 'IT'인 주문만 주문번호, 고객명, 도서명, 분야를 조회하시오.
select o.order_id 주문번호, o.customer_name 고객명, b.title 도서명, b.category 분야
from book b
inner join book_order o
on b.book_id = o.book_id
where b.category ='IT';
-- ===================================================================
-- 문제 4  주문별 결제금액 계산
-- [난이도: 초급]  [학습 포인트: INNER JOIN, 산술연산자]
-- 주문 테이블의 qty(수량)와 book 테이블의 price(정가)·discount_rate(할인율)를 결합해야 실제 결제금액을 계산할 수 있습니다.
-- 요구사항 : book_order와 book을 조인하여 주문번호, 도서명, 수량과 함께 
-- '수량×정가×(1-할인율/100)'으로 계산한 결제금액을 반올림하여 '결제금액'으로 조회하시오.
select o.order_id 주문번호, b.title 도서명, o.qty 수량, round(o.qty*b.price*(1-b.discount_rate/100)) 결제금액
from book_order o
inner join book b
on o.book_id = b.book_id;
-- ===================================================================
-- 문제 5  결제금액이 높은 주문 순위
-- [난이도: 초급]  [학습 포인트: INNER JOIN, ORDER BY]
-- 가장 매출 기여도가 큰 "고액 주문"부터 정렬해서 VIP 응대 우선순위를 정하려 합니다.
-- 요구사항 : 4번 문제 결과에 결제금액이 높은 순서로 정렬을 추가하여 조회하시오.
select o.order_id 주문번호, b.title 도서명, o.qty 수량, round(o.qty*b.price*(1-b.discount_rate/100),0) 결제금액
from book_order o
inner join book b
on o.book_id = b.book_id
order by 4 desc;
-- ====================================================================
-- 문제 6  고객 등급 정보와 주문 연결
-- [난이도: 초급]  [학습 포인트: INNER JOIN(다른 컬럼 기준)]
-- 이번 시간에 새로 추가된 customer 테이블에는 고객 등급(VIP/일반) 정보가 있습니다. 주문 내역에 고객 등급을 함께 표시하고 싶습니다.
-- 요구사항 : book_order와 customer를 고객명(customer_name) 기준으로 조인하여 주문번호, 고객명, 등급(grade), 수량을 조회하시오
desc customer;

select o.order_id 주문번호, o.customer_name 고객명, c.grade 등급, o.qty 수량
from book_order o
inner join customer c
on o.customer_name= c.customer_name;
-- =====================================================================
-- 문제 7  VIP 고객의 주문만 조회
-- [난이도: 초급]  [학습 포인트: INNER JOIN, WHERE]
-- VIP 고객 전용 사은품 발송을 위해 VIP 등급 고객의 주문만 추려야 합니다.
-- 요구사항 : 6번 결과에서 등급(grade)이 'VIP'인 주문만 조회하시오.
select o.order_id 주문번호, o.customer_name 고객명, c.grade 등급, o.qty 수량
from book_order o
inner join customer c
on o.customer_name= c.customer_name
where c.grade = 'VIP';
-- =====================================================================
-- 문제 8  3개 테이블 연결 - 고객·주문·도서 통합 조회
-- [난이도: 초급]  [학습 포인트: 다중 테이블 JOIN]
-- "누가, 어떤 등급이고, 어떤 책을, 어떤 분야에서" 샀는지 한 화면에서 보고 싶습니다. 정보가 book, book_order, customer 세 테이블에 흩어져 있습니다.
-- 요구사항 : book_order, book, customer 세 테이블을 모두 연결하여 고객명, 등급, 도서명, 분야, 수량을 조회하시오.
select o.customer_name 고객명, c.grade 등급, b.title 도서명, b.category 분야, o.qty 수량
from book_order o
inner join book b
on b.book_id = o.book_id
inner join customer c
on c.customer_name =o.customer_name;
-- =====================================================================
-- 문제 9  VIP 고객의 IT 도서 구매 내역
-- [난이도: 중급]  [학습 포인트: 다중 테이블 JOIN, WHERE(AND)]
-- VIP 고객 중 IT 도서를 구매한 사람들을 대상으로 신간 IT서적 안내 메일을 발송하려 합니다.
-- 요구사항 : 8번 결과에서 등급이 'VIP'이고 분야가 'IT'인 주문만 고객명, 도서명, 분야를 조회하시오.
select o.customer_name 고객명, c.grade 등급, b.title 도서명, b.category 분야, o.qty 수량
from book_order o
inner join book b
on b.book_id = o.book_id
inner join customer c
on c.customer_name =o.customer_name
where c.grade ='VIP' and b.category ='IT';
-- =====================================================================
-- 문제 10  고객별 결제금액 높은 순 종합 조회
-- [난이도: 중급]  [학습 포인트: 다중 테이블 JOIN, 산술연산, ORDER BY]
-- 3개 테이블 정보를 모두 활용해 "누가 얼마짜리 주문을 했는지"를 결제금액이 큰 순서로 정리한 리포트를 만들어야 합니다.
-- 요구사항 : book_order, book, customer를 조인하여 
-- 고객명, 도서명, 결제금액(수량×정가×(1-할인율/100), 반올림)을 결제금액이 큰 순서로 조회하시오.
select o.customer_name 고객명, b.title 도서명, round(o.qty*b.price*(1-b.discount_rate/100)) as 결제금액
from book_order o
inner join book b
on b.book_id = o.book_id
inner join customer c
on c.customer_name =o.customer_name
order by 3 desc;
-- ===================================================================
-- 문제 11  한 번도 주문되지 않은 도서 찾기
-- [난이도: 초급]  [학습 포인트: LEFT JOIN, IS NULL]
-- 재고 관리팀에서 "지금까지 단 한 번도 팔리지 않은 도서" 목록을 요청했습니다. 
-- 그런데 INNER JOIN으로는 "주문이 있는" 도서만 보이므로 이 문제를 풀 수 없습니다.
-- 요구사항 : book 테이블을 기준으로 book_order와 LEFT JOIN 하여, 주문 기록이 전혀 없는 도서의 도서코드(book_id)와 도서명을 조회하시오.
select b.book_id 도서코드, title 도서명
from book b
left outer join book_order o
on b.book_id = o.book_id
where order_Id is null;
-- ===================================================================
-- 문제 12  한 번도 주문하지 않은 고객 찾기
-- [난이도: 초급]  [학습 포인트: LEFT JOIN, IS NULL]
-- 가입만 하고 아직 주문 이력이 없는 "휴면 회원"에게 첫 구매 쿠폰을 보내려 합니다.
-- 요구사항 : customer 테이블을 기준으로 book_order와 LEFT JOIN 하여, 주문 이력이 없는 고객의 고객코드(customer_id)와 고객명을 조회하시오.
select c.customer_id 고객코드, c.customer_name 고객명
from customer c
left join book_order o
on c.customer_name = o.customer_name
where o.order_id is null;
-- =====================================================================
-- 문제 13  도서별 주문건수(0건 포함) 집계
-- [난이도: 중급]  [학습 포인트: LEFT JOIN, GROUP BY, COUNT]
-- 전체 도서의 판매 현황을 파악하되, 한 번도 안 팔린 도서도 "0건"으로 표시되어야 어떤 책이 안 팔리는지 알 수 있습니다.
-- 요구사항 : book을 기준으로 book_order와 LEFT JOIN하여 도서명별 주문건수를 구하시오. 주문건수가 적은 순서로 정렬하시오.
select b.title 도서명, ifnull( sum(o.qty),0) 주문건수
from book b
left join book_order o
on b.book_id = o.book_id
group by b.title
order by 2 asc;
-- ======================================================================
-- 문제 14  재고만 쌓여있는 미판매 도서 찾기
-- [난이도: 중급]  [학습 포인트: LEFT JOIN, GROUP BY, HAVING]
-- 13번에서 만든 집계표를 활용해, 이번에는 정확히 "0건"인 도서만 뽑아 재고 처분 대상 목록을 만들려 합니다.
-- 요구사항 : book을 기준으로 book_order와 LEFT JOIN하여 
-- 도서별 총주문수량(qty 합계, 없으면 0)을 구하되, 총주문수량이 0인 도서만 도서명과 총주문수량을 조회하시오.
select b.title 도서명, ifnull( sum(o.qty),0) 총주문수량
from book b
left join book_order o
on b.book_id = o.book_id
group by b.title
having ifnull( sum(o.qty),0) = 0;
-- ======================================================================
-- 문제 15  분야별 총 판매 수량
-- [난이도: 중급]  [학습 포인트: JOIN, GROUP BY, SUM]
-- 어느 분야가 가장 많이 팔리는지 분야별 판매 트렌드를 파악하려 합니다.
-- 요구사항 : book과 book_order를 조인하여 분야(category)별 총주문수량(qty 합계)을 구하고, 총주문수량이 많은 순서로 조회하시오.
select b.category 분야, ifnull( sum(o.qty),0) 총주문수량
from book b
left join book_order o
on b.book_id = o.book_id
group by b.category
order by 2 desc;
-- ======================================================================
-- 문제 16  주력 판매 분야 선정(HAVING)
-- [난이도: 중급]  [학습 포인트: JOIN, GROUP BY, HAVING, SUM]
-- 전체 분야 중 특별히 "잘 팔리는 주력 분야"만 골라 다음 시즌 마케팅 예산을 집중하려 합니다.
-- 요구사항 : 15번 결과에서 총주문수량이 5 이상인 분야만 조회하시오.
select b.category 분야, ifnull( sum(o.qty),0) 총주문수량
from book b
left join book_order o
on b.book_id = o.book_id
group by b.category
having ifnull( sum(o.qty),0) >= 5;
-- ======================================================================
-- 문제 17  고객별 총 결제금액 집계
-- [난이도: 중급]  [학습 포인트: 다중 JOIN, GROUP BY, SUM]
-- 우수 고객을 선정하기 위해 고객별로 지금까지 결제한 총액을 계산해야 합니다.
-- 요구사항 : book_order, book, customer를 조인하여 고객별 총결제금액(수량×정가×(1-할인율/100)의 합계, 반올림)을 구하고 금액이 큰 순서로 조회하시오.
select c.customer_name 고객, round(sum(o.qty*b.price*(1-b.discount_rate/100)),0) 총결제금액
from book_order o
inner join book b
on o.book_id = b.book_id
inner join customer c
on o.customer_name = c.customer_name
group by c.customer_name
order by 2 desc;
-- ======================================================================
-- 문제 18  우수 고객(고액 결제) 선정
-- [난이도: 중급]  [학습 포인트: 다중 JOIN, GROUP BY, HAVING]
-- 17번 집계 결과 중 누적 결제금액이 일정 기준을 넘는 고객만 VIP 승급 대상자로 선정하려 합니다.
-- 요구사항 : 17번 결과에서 총결제금액이 50,000원 이상인 고객만 조회하시오.
select c.customer_name 고객, round(sum(o.qty*b.price*(1-b.discount_rate/100)),0) 총결제금액
from book_order o
inner join book b
on o.book_id = b.book_id
inner join customer c
on o.customer_name = c.customer_name
group by c.customer_name
having round(sum(o.qty*b.price*(1-b.discount_rate/100)),0) >= 50000
order by 2 desc;
-- ======================================================================
-- 문제 19  출판사별 판매 실적
-- [난이도: 중급]  [학습 포인트: JOIN, GROUP BY, SUM]
-- 출판사와의 재계약 협상을 앞두고, 어떤 출판사의 책이 잘 팔렸는지 실적 자료가 필요합니다.
-- 요구사항 : book과 book_order를 조인하여 출판사(publisher)별 총판매수량(qty 합계)을 구하고 많이 팔린 순서로 조회하시오.
select publisher 출판사, sum(qty) 총판매수량
from book b
join book_order o
on b.book_id = o.book_id
group by b.publisher
order by 2 desc;
-- ======================================================================
-- 문제 20  등급별 구매력 비교
-- [난이도: 중급]  [학습 포인트: JOIN, GROUP BY, COUNT, SUM]
-- VIP 등급 제도가 실제로 매출에 도움이 되는지, VIP와 일반 고객의 구매 규모를 비교 분석하려 합니다.
-- 요구사항 : book_order와 customer를 조인하여 등급(grade)별 총주문건수와 총주문수량을 조회하시오.
select c.grade 등급, count(*)총주문건수, sum(qty)총주문수량
from book_order o
inner join customer c
on o.customer_name = c.customer_name
group by c.grade;
-- ======================================================================
-- 문제 21  요일별 주문 패턴 분석
-- [난이도: 심화]  [학습 포인트: CASE, 날짜 함수, GROUP BY]
-- 어느 요일에 주문이 몰리는지 파악해 배송 인력 배치 계획에 반영하려 합니다.
-- 요구사항 : book_order의 주문일(order_date)의 요일을 '월요일'~'일요일'로 변환하여 요일별 주문건수를 구하고, 건수가 많은 순서로 조회하시오.
select * from book_order;

SELECT 
    CASE 
        WHEN DATE_FORMAT(order_date, '%w') = '0' THEN '일요일'
        WHEN DATE_FORMAT(order_date, '%w') = '1' THEN '월요일'
        WHEN DATE_FORMAT(order_date, '%w') = '2' THEN '화요일'
        WHEN DATE_FORMAT(order_date, '%w') = '3' THEN '수요일'
        WHEN DATE_FORMAT(order_date, '%w') = '4' THEN '목요일'
        WHEN DATE_FORMAT(order_date, '%w') = '5' THEN '금요일'
        WHEN DATE_FORMAT(order_date, '%w') = '6' THEN '토요일'
    END AS 주문요일,
    SUM(qty) AS 주문건수
FROM book_order
GROUP BY 1
ORDER BY 주문건수 DESC;
-- ======================================================================
-- 문제 22  가격대별 주문 선호도 분석
-- [난이도: 심화]  [학습 포인트: JOIN, CASE, GROUP BY]
-- 고객들이 저가/중가/고가 도서 중 어떤 가격대를 더 많이 주문하는지 분석해 가격 전략에 참고하려 합니다.
-- 요구사항 : book_order와 book을 조인하여 정가 기준으로 15,000원 미만은 '저가', 25,000원 이하는 '중가', 그 외는 '고가'로 분류하고, 가격대별 주문건수를 많은 순서로 조회하시오.
select
	case
		when b.price <15000 then '저가'
        when b.price <=25000 then '중가'
        else '고가'
	end as 가격대,
    sum(o.qty) 주문건수
from book_order o
inner join book b
on o.book_id = b.book_id
group by 1
order by sum(o.qty) desc;
-- ======================================================================
-- 문제 23  등급별 평균 결제금액 비교
-- [난이도: 중급]  [학습 포인트: 다중 JOIN, GROUP BY, AVG]
-- VIP 고객 한 명당 평균적으로 얼마씩 결제하는지, 일반 고객과 비교해 등급제의 효과를 검증하려 합니다.
-- 요구사항 : book_order, book, customer를 조인하여 등급별 평균 결제금액(반올림)을 조회하시오.
select c.grade 등급, round(avg(o.qty*b.price*(1-b.discount_rate/100)),0) 평균결제금액
from book_order o
inner join book b
on o.book_id = b.book_id
inner join customer c
on o.customer_name = c.customer_name
group by c.grade
order by 2 desc;
-- ======================================================================
-- 문제 24  배송 지연 주문 상세 확인
-- [난이도: 중급]  [학습 포인트: 다중 JOIN, DATEDIFF, WHERE]
-- 고객 불만이 접수된 배송 지연 건들을 구체적으로 확인해 원인을 파악하려 합니다.
-- 요구사항 : book_order, book, customer를 조인하여 [발송일-요청일]이 3일 이상인 주문의 고객명, 도서명, 지연일수를 지연일수가 큰 순서로 조회하시오.
select c.customer_name 고객명, b.title 도서명, ship_date -request_date 지연일수
from book_order o
inner join book b
on o.book_id = b.book_id
inner join customer c
on o.customer_name = c.customer_name
where datediff(ship_date,request_date) >= 3
order by 3 desc;
-- ======================================================================
-- 문제 25  재고 소진이 필요한 미판매 도서(자산가치 포함)
-- [난이도: 중급]  [학습 포인트: LEFT JOIN, GROUP BY, HAVING]
-- 25번 문제는 11번(미판매 도서 찾기)을 한 단계 확장해, 재고수량까지 함께 보여줘 처분 우선순위를 정하려는 것입니다.
-- 요구사항 : book을 기준으로 book_order와 LEFT JOIN하여 총판매수량이 0인 도서의 도서명, 재고수량, 총판매수량을 재고수량이 많은 순서로 조회하시오.
select title 도서명, b.stock 재고수량, ifnull(o.qty,0) 총판매수량
from book b
left outer join book_order o
on b.book_id = o.book_id
where order_Id is null
order by 2 desc;
-- ======================================================================
-- 문제 26  고객별 구매 분야 다양성 분석
-- [난이도: 심화]  [학습 포인트: 다중 JOIN, GROUP BY, COUNT(DISTINCT)]
-- 한 분야만 편식하듯 구매하는 고객과, 여러 분야를 골고루 구매하는 고객을 구분해 추천 전략을 다르게 적용하려 합니다.
-- 요구사항 : book_order, book, customer를 조인하여 고객별로 서로 다른 구매 분야의 개수(구매분야수)를 구하고, 많은 순서로 조회하시오.
select c.customer_name 고객명, count(distinct(category)) 구매분야수
from book_order o
inner join book b
on o.book_id = b.book_id
inner join customer c
on o.customer_name = c.customer_name
group by c.customer_name
order by 2 desc;
-- ======================================================================
-- 문제 27  다분야 구매 고객(취향이 폭넓은 고객) 선별
-- [난이도: 심화]  [학습 포인트: 다중 JOIN, GROUP BY, HAVING, COUNT(DISTINCT)]
-- 26번 결과 중 특히 2개 분야 이상 구매한 "취향이 폭넓은 고객"만 뽑아 여러 분야 신간을 동시에 추천하려 합니다.
-- 요구사항 : 26번 결과에서 구매분야수가 2 이상인 고객만 조회하시오.
select c.customer_name 고객명, count(distinct(category)) 구매분야수
from book_order o
inner join book b
on o.book_id = b.book_id
inner join customer c
on o.customer_name = c.customer_name
group by c.customer_name
having count(distinct(category)) >=2
order by 2 desc;
-- ======================================================================
-- 문제 28  [종합] 고객별 주문 요약 리포트
-- [난이도: 심화]  [학습 포인트: 다중 JOIN, GROUP BY, COUNT, SUM, AVG]
-- 경영진 보고를 위해 고객별 핵심 지표(주문건수·총결제액·평균결제액)를 한 번에 모은 종합 리포트가 필요합니다.
-- 요구사항 : book_order, book, customer를 조인하여 고객별로 등급, 총주문건수, 총결제금액, 평균결제금액(모두 반올림)을 구하고 총결제금액이 큰 순서로 조회하시오.
select c.customer_name 고객명, c.grade 등급, sum(o.qty) 총주문건수, sum(o.qty*b.price) 총결제금액, round(avg(o.qty*b.price)) 평균결제금액
from book_order o
inner join book b
on o.book_id = b.book_id
inner join customer c
on o.customer_name = c.customer_name
group by c.customer_name, c.grade
order by 4 desc;
-- ======================================================================
-- 문제 29  [종합] 미판매 재고 자산 총액 산출
-- [난이도: 심화]  [학습 포인트: LEFT JOIN, SUM, WHERE]
-- 재무팀에서 "지금까지 한 번도 안 팔린 책들이 창고에 자산으로 얼마나 묶여있는지" 단일 금액으로 보고해 달라고 요청했습니다.
-- 요구사항 : book을 기준으로 book_order와 LEFT JOIN하여, 주문 기록이 없는 도서들의 '정가×재고수량' 합계를 '미판매재고자산' 이라는 별명으로 조회하시오.
select sum(b.price*b.stock) 미판매재고자산
from book b
left join book_order o
on b.book_id = o.book_id
where o.order_id is null;
-- ======================================================================
-- 문제 30  [종합] 등급×분야 교차 매출 분석
-- [난이도: 심화]  [학습 포인트: 다중 JOIN, GROUP BY(2개 컬럼)]
-- "VIP 고객은 어떤 분야를 특히 많이 사는지" 등급과 분야를 교차 분석해 정교한 타겟 마케팅 전략을 세우려 합니다.
-- 요구사항 : book_order, book, customer를 조인하여 등급과 분야 조합별 총결제금액(반올림)을 구하고, 등급 순 · 등급 내 결제금액 큰 순으로 조회하시오.
select c.grade 등급, b.category 분야, sum(o.qty*b.price) 총결제금액
from book_order o
inner join book b
on o.book_id = b.book_id
inner join customer c
on o.customer_name = c.customer_name
group by c.grade, b.category
order by 1 asc, 3 desc;