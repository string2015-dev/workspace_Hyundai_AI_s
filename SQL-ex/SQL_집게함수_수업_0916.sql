select count(*), count(고객번호), count(도시), count(지역)
from 고객;

select count(지역) from 고객;
select count(*) from 고객;
select 도시 from 고객;

-- 예제 4-5
desc 고객;
select count(담당자직위) from 고객;
select 담당자직위
	,도시
	,count(*) as 고객수
    ,avg(마일리지)
from 고객
group by 담당자직위, 도시
order by 1,2;

-- 예제 4-6
select 도시, count(*) 고객수, avg(마일리지) 평균마일리지
from 고객
group by 도시
having count(*) >=10;

-- 4-7
-- 문제를 쪼개서 어떻게 작성할 것인지 논리구조를 세우는게 중요하다.
SELECT 도시, SUM(마일리지)
FROM 고객
WHERE 고객번호 LIKE 'T%'
group by 1
having sum(마일리지) >1000;

-- 심화문제1
select ifnull(도시,'총계') 도시
	,count(*) 고객수
    ,avg(마일리지) 평균마일리지
from 고객
where 지역 is null
group by 도시
with rollup;

-- 예제 4-9
select 담당자직위 from 고객;

select 담당자직위, 도시
	,count(*) 고객수
from 고객
where 담당자직위 like '%마케팅%'
group by 담당자직위, 도시
with rollup;

-- 에제4-10
select 지역
	,count(*) 고객수
    ,grouping(지역) 구분
from 고객
where 담당자직위 = '대표 이사'
group by 지역
with rollup;

-- 예제4-11

-- 점검 문제 ============
-- ====================
-- 문제1 고객테이블의 컬럼에는 몇 개의 도시가 들어있을까요? 도시 수와 중복 값을 제외한 도시수?
SELECT 
    COUNT(도시), COUNT(DISTINCT (도시))
FROM
    고객;
    
-- 문제2 주문 테이블에서 주문년도별로 주문걸수를 조회하시오.
desc 주문;

select year(주문일) 주문연도, count(주문일) 주문건수
from 주문
group by 주문연도;

-- 문제3 결과화면을 참고 주문 테이블에서(주문년고, 분기) 별 주문건수, 주문년도별 주문건수, 천제 주문건수 조회
select year(주문일) 주문연도
,quarter(주문일) 분기
, count(주문번호) 주문건수
from 주문
group by 1,2
with rollup;

-- 문제 4 주문 테이블에서 요청일보다 발송이 늦어진 주문내역이 월별로 몇 건씩인지 요약해 조회]
-- 주문월 순서대로 정렬하시오.
desc 주문;
select month(주문일) 주문월
	,count(주문번호) 주문건수
from 주문
where 발송일 - 요청일 >0
group by 1
order by 1;

-- 문제5 제품 테이블에서 '아이스크림' 제품들에 대하여 제품명별로 제고합을 보이시오.
desc 제품;
select * from 제품;

select 제품명,sum(재고) 재고량
from 제품
where 제품명 like '%아이스크림%'
group by 제품명;

-- 문제6 고객 테이블에서 마일리지가 50000점 이상인 고객 vip 나머지 일반고객
-- 고객 구분별로 고객 수와 평균마일리지.
desc 고객;
select case
		when 마일리지 >= 50000 then 'VIP_고객'
        else '일반고객'
		end as 고객구분
        ,count(고객번호) as 고객수
        ,avg(마일리지) as 평균마일리지
from 고객
group by 고객구분;