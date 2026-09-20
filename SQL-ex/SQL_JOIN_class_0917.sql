use hyundai;

-- 에제5.1
select 부서.부서번호 '부서명의_부서번호', 부서.부서명 '부서명',이름, 사원.부서번호 '사원의_부서번호'
from 부서
cross join 사원
where 이름 = '배재용';

-- 외례키 만들어서 연결하기 부서와 사원 연결
# 사원 -> 부서(한부서에 여러 사원 가능)
desc 사원;
select distinct 부서번호 from 부서;
select distinct 부서번호, 사원번호 from 사원;

update 사원 set 부서번호 = null where 사원번호 ='E10';
commit;
-- --------------------------------
ALTER table 사원
	add constraint FK_사원_부서
foreign key (부서번호) references 부서(부서번호);

-- 셀프조인 사원에서 사원 포린키 걸기
alter table 사원
	add constraint FK_사원_상사
foreign key (상사번호) references 사원(사원번호);
select distinct 상사번호, 사원번호 from 사원;

update 사원 set 상사번호 = null where trim(상사번호) ='';
commit;

-- 사원과 주문 연결
alter table 주문
	add constraint FK_주문_사원
foreign key (사원번호) references 사원(사원번호);
-- 고객과 주문
desc 고객;
alter table 주문
	add constraint FK_고객_주문
foreign key (고객번호) references 고객(고객번호);
-- 주문과 주문세부
alter table 주문세부
add constraint FK_주문세부_주문
foreign key (주문번호) references 주문(주문번호);
-- 제품과 주문세부
alter table 주문세부
add constraint FK_주문세부_제품
foreign key (제품번호) references 제품(제품번호);

commit;