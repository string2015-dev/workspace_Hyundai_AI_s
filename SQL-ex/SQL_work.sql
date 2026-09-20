use hyndai;
-- 09/15 2.5
select *
from 고객
limit 3;

-- 2.6 마일리지가 많은 상위 3명의 고객을 마일리지 많은 순서대로 가지고 와라.
select *
from 고객
order by 마일리지 desc
limit 3;

-- 2.7
select distinct 도시
from 고객;

-- section2 SQL 연산자

-- 2.8 두개의 숫자 23, 5로 산술 연산자. div, mod 사용
select
23 + 5 as '덧셉',
23 - 5 as '밸셈',
23*5 as '곱셈',
23/5 as '실수나누기',
23 div 5 as '몫',
23 mod 4 as '나머지 1',
23 % 5 as '나머지2';
-- 2.9
select
23>= 5,
23<=5,
23>5,
23< 23,
23 = 23,
23 != 23,
23 <> 23;

-- 2.10
select *
from 고객
where 담당자직위 != '대표 이사';

-- 2.11
select *
from 고객
where 도시 ='부산광역시' and 마일리지 < 1000;

-- 2.11
select 고객번호, 담당자명, 마일리지, 도시
from 고객
where 도시 ='부산광역시'
union
select 고객번호, 담당자명, 마일리지, 도시
from 고객
where 마일리지 < 1000
order by 1;

-- 2.13
select *
from 고객
where 지역 ='';

update 고객
set 지역 = null
where 지역 ='';

select *
from 고객
where 지역 is null;

-- 2.14
select 고객번호, 담당자명, 담당자직위
from 고객
where 담당자직위 ='염업 과장'
or 담당자직위 ='마케팅 과장';

select 고객번호, 담당자명, 담당자직위
from 고객
where 담당자직위 in('염업 과장','마케팅 과장');

-- 2.15
select 담당자명, 마일리지
from 고객
where 마일리지 between 100000 and 200000;

-- 2.16
select *
from 고객
where 도시 like '%광역시' 
and (고객번호 like '_C%' or 고객번호 like '__C%');

-- 점검문제 1
select *
from 고객
where 마일리지 between 15000 and 20000;

-- 점검문제2
select distinct 지역, 도시
from 고객
order by 1, 2;

-- 점검문제3
select *
from 고객
where 도시 in ('춘천시','광명시','과천시') and 담당자직위 like '%이사'
or 도시 in ('춘천시','광명시','과천시') and 담당자직위 like '%사원';

-- 점검문제4
select *
from 고객
where 도시 not regexp'광역시|특별시'
order by 마일리지 desc
limit 3;

-- 점검문제5
select *
from 고객
where 지역 is not null and 담당자직위 not like '%대표 이사%';

-- 문자형 함수 3.1
select char_length('hello')
, length('hello')
, char_length('안녕')
, length('안녕');

-- 