use hyundai;

desc 부서;
select * from 부서;
insert into 부서 values('A5','마케팅부');
insert into 부서(부서번호) values('A6'); -- 테이블 명을 적을 떄는 컬럼의 갯수를 맞춰야 한다.
commit;
-- 예제 7-2
desc 제품;
insert into 제품 values(91, '연어피클소스', null, 5000, 40);
select * from 제품;
commit;

-- 7-3
desc 제품;
insert into 제품(제품번호, 제품명, 단가, 재고) values(90,'연어핫소스', 4000,50);
select * from 제품 where 제품번호 =90;
commit;

-- 7-4
desc 사원;
insert into 사원(사원번호, 이름, 직위, 성별, 입사일)
values ('E20','김사과','수습사원','여',curdate()),('E21','박바나나', '수습사원', '여', curdate()),('E22', '정오렌지', '수습사원', '여', curdate());
select * from 사원;
commit;

-- update
update 테이블명
set 컬럼명1 =값1, 컬럼명2 =값2
where 조건;

-- 7-5
update 사원
set 이름 = '김레몬'
where 사원번호 ='E20';
select * from 사원;
commit;
-- 7-6
select * from 제품 where 제품번호 = 91;
update 제품 SET 포장단위 ='200 ml bottles' where 제품번호 =91;
commit;
-- 7-7
select * from 제품 where 제품번호 = 91;
update 제품
SET 단가 = 단가*1.1 , 재고 = 재고-10
where 제품번호 =91;
commit;

-- delete
-- 7-8
delete from 제품 where 제품번호 = 91;
select * from 제품 where 제품번호 = 91;
rollback;

select @@autocommit;
set autocommit = 0;

-- 7-9
select * from 사원 order by 입사일 desc;

delete from 사원
order by 입사일 desc
limit 3;
commit;
-- 7-10
INSERT INTO 제품(제품번호, 제품명, 단가, 재고) values(91, '연어핫소스', 단가=6000, 재고=50)
ON DUPLICATE KEY UPDATE
제품명 ='연어핫소스', 단가 =6000, 재고 =50;
select * from 제품 where 제품번호 =91;
commit;
-- =========================================================================
create table 고객주문요약 (
	고객번호 char(5) primary key,
    고객회사명 varchar(50),
    주문건수 int,
    최종주문일 date);
    
desc 고객주문요약;

insert into 고객주문요약
select 고객.고객번호, 고객.고객회사명, count(*),max(주문일)
from 고객, 주문
where 고객.고객번호 = 주문.고객번호
group by 고객.고객번호, 고객회사명;

select * from 고객주문요약;
commit;

-- 7-12
update 제품
set 단가 =(
select * from 
(select avg(단가)
from 제품
where 제품명 like '%소스%') as t)
where 제품번호 =91;

select * from 제품 where 제품번호=91;

-- 7-13
update 고객, (select distinct 고객번호
from 주문) as 주문고객
set 마일리지 =마일리지*1.1
where 고객.고객번호 in (주문고객.고객번호);
select * from 고객 where 고객번호 = 'ACDDR';
commit;

-- 7-14
UPDATE 고객
inner join 마일리지등급
on 마일리지 between 하한마일리지 and 상한마일리지
SET 마일리지 =마일리지+1000
where 등급명 ='S';
-- 위는 반영 아래는 확인
SELECT *
FROM 고객
inner join 마일리지등급
on 마일리지 between 하한마일리지 and 상한마일리지
where 등급명 ='S';

ROLLBACK;
COMMIT;

-- DELETE SELECT
DELETE FROM 주문
WHERE 주문번호 NOT IN
(select distinct 주문번호
from 주문세부);

SELECT * FROM 주문 WHERE 주문번호 ='H1077';
SELECT * FROM 주문세부 WHERE 주문번호 ='H1077';

COMMIT;

-- delect JOIN
-- 두 테이블에서 일치하는 것을 삭제 할 수 있다.
SELECT *
FROM 주문
WHERE 주문번호 = 'H0248';

SELECT *
FROM 주문세부
WHERE 주문번호 = 'H0248';

/*ANSI SQL*/
DELETE 주문
      ,주문세부
FROM 주문
INNER JOIN 주문세부
ON 주문.주문번호 = 주문세부.주문번호
WHERE 주문.주문번호 = 'H0248';

/*Non-ANSI SQL*/
DELETE 주문
      ,주문세부
FROM 주문
    ,주문세부
WHERE 주문.주문번호 = 주문세부.주문번호
AND 주문.주문번호 = 'H0248';

-- 7-17
SELECT 고객.*
FROM 고객
LEFT OUTER JOIN 주문
ON 고객.고객번호 = 주문.고객번호
WHERE 주문.고객번호 IS NULL;

DELETE 고객
FROM 고객
LEFT JOIN 주문
ON 고객.고객번호 = 주문.고객번호
WHERE 주문.고객번호 IS NULL;

SELECT *
FROM 고객
WHERE 고객번호 IN ('BQQZA', 'RISPA', 'SSAFI', 'TTRAN');


-- =========================================================
# 점검문제

-- 1번
desc 제품;

insert into 제품 values(95, '망고베리 아이스크림', '400g', 800, 30);
select* from 제품 where 제품번호 =95;
commit;
-- 2번
insert into 제품(제품번호, 제품명,단가) values(96, '눈꽃빙수맛 아이스크림',2000);
select* from 제품 where 제품번호 =96;
commit;

-- 3번
update 제품
set 재고 =30
where 제품번호 =96;
select* from 제품 where 제품번호 =96;
commit;

-- 4번
delete 부서
from 사원 
right join 부서 on 사원.부서번호 = 부서.부서번호
where 사원.부서번호 is null;

select * from 부서;
commit;
-- 세람님
delete from 부서
where 부서번호 not in (select distinct 부서번호 from 사원);

desc 부서;
insert into 부서 values ('A4', '홍보부'),('A5', '마케팅부');

select * from 부서;
commit;

-- 4번 문제 풀이
# 사원이 한 명도 존재하지 않는 부서를 부서 테이블에서 삭제하시오.
delete 부서
from 사원
right join 부서 on 사원.부서번호 = 부서.부서번호
where 사원.사원번호 is null;

select * from 부서;
commit;