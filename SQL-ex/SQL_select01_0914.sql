use hyundai;

select * from 고객 order by 고객회사명 desc;
-- 2.2
select
	고객번호, 담당자명, 고객회사명, 마일리지 as 포인트,
    마일리지*1.1 as '10% 인상된 마일리지'
from
고객;

-- 2.3
select 고객번호, 담당자명, 마일리지
from 고객
where 마일리지 >= 100000;

-- 2.4
select 고객번호, 담당자명, 도시, 마일리지
from 고객
where 도시 = '서울특별시'
order by 마일리지 desc;


