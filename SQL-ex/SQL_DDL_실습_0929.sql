use 현대학사;

-- 테이블 생성
# 처음 테이블을 생성할때는 컬럼 하나하나 입력해야한다.

-- 8-2
create table 학과 (학과번호 char(2), 학과명 varchar(20), 학과장명 varchar(2));
desc 학과;
insert into 학과 values('AA', '컴퓨터공학과', '배경민'),('BB', '소프트웨어학과', '김남준'),('CC', '디자인융합학과', '박선영');

alter table 학과 modify 학과장명 varchar(20);

select* from 학과;
commit;
-- -
-- 8-3
create table 학생 (학번 char(5), 이름 varchar(5), 나이 int, 연락처 int, 학과명 varchar(20));
desc 학생;

drop table 학생;
create table 학생 (학번 char(5), 이름 varchar(20), 생일 date, 연락처 varchar(20), 학과번호 char(2));
desc 학생;

insert into 학생 values('S0001', '이윤주', '2020-01-30', '01033334444', 'AA'),('S0001', '이승은','2021-02-23', NULL ,'AA'),('S0003','백재용', '2018-03-31', '01077778888', 'DD');
select * from 학생;
commit;

-- =======================================================================================
-- 예제 8-12
# 컬럼 레벨 
DROP TABLE 학과;

create table 학과 (학과번호 char(2) primary KEY, 학과명 varchar(20) not null, 학과장명 varchar(2));

#table 레벨 방법
create table 학과 (
학과번호 char(2), 
학과명 varchar(20) not null,
학과장명 varchar(2),
primary key(학과번호)
);
alter table 학과 change 학과장명 학과장명 varchar(20);
-- 예제 8-13
DROP TABLE 학생;
# 테이블 레벨
create table 학생 (
학번 char(5), 
이름 varchar(20) NOT NULL, 
생일 date NOT NULL, 
연락처 varchar(20), 
학과번호 char(2),
성별 CHAR(1),
등록일 DATE default(CURDATE()),
primary key(학번),
unique(연락처),
check(성별 IN ('남','여')),
FOREIGN KEY (학과번호) REFERENCES 학과(학과번호)
);
DESC 학생;
SELECT * FROM 학생;
COMMIT;

# 컬럼 레벨
create table 학생 (
학번 char(5) primary KEY, 
이름 varchar(20) NOT NULL, 
생일 date NOT NULL, 
연락처 varchar(20) unique, 
학과번호 char(2), foreign key (학과번호) REFERENCES 학과(학과번호),
성별 CHAR(1) check(성별 in('남','여')),
등록일 DATE default(CURDATE())
);
-- 예제 8-14
create table 과목
(
과목번호 char(5)
,과목명 varchar(20) not null
,학점 int not null check(학점 between 2 and 4)
,구분 varchar(20) check(구분 in('전공','교양','일반'))
,primary key(과목번호)
);
desc 과목;
-- 예제 8-15
create table 수강_1 (
수강년도 char(4) not null
,수강학기 varchar(20) not null check(수강학기 in('1학기','2학기','여름학기','겨울학기'))
,학번 char(5) not null
,과목번호 char(5) not null
,성적 int check (성적 between 0 and 4.5)
,primary key(수강년도, 수강학기, 학번, 과목번호)
,foreign key(학번) references 학생(학번)
,foreign key(과목번호) references 과목(과목번호)
);
alter table 수강_1 change 성적 성적 float check (성적 between 0 and 4.5);
desc 수강_1;

-- 예제 8-16
create table 수강_2
(
수강번호 int primary key auto_increment
,수강년도 char(4) not null
,수강학기 varchar(20) not null check(수강학기 in('1학기','2학기','여름학기','겨울학기'))
,학번 char(5) not null
,과목번호 char(5) not null
,성적 numeric(3,1) check (성적 between 0 and 4.5)
,foreign key(학번) references 학생(학번)
,foreign key(과목번호) references 과목(과목번호)
);
desc 수강_2;

commit;

/*예제8-17*/
INSERT INTO 학과
VALUES ('AA','컴퓨터공학과','배경민');

INSERT INTO 학과
VALUES ('AA','소프트웨어학과','김남준');

INSERT INTO 학과
VALUES ('CC','디자인융합학과','박선영');
/*오류 수정*/
INSERT INTO 학과
VALUES ('BB','소프트웨어학과','김남준');

/*예제8-18*/
INSERT INTO 학생(학번, 이름, 생일, 학과번호) 
VALUES ('S0001','이윤주','2020-01-30','AA');

INSERT INTO 학생(이름, 생일, 학과번호) 
VALUES ('이승은','2021-02-23','AA');   

INSERT INTO 학생(학번, 이름, 생일, 학과번호) 
VALUES ('S0003','백재용','2018-03-31','DD'); 


/*오류 수정*/
INSERT INTO 학생(학번, 이름, 생일, 학과번호)
VALUES ('S0002', '이승은','2020-01-30', 'AA');

INSERT INTO 학생(학번, 이름, 생일, 학과번호)
VALUES ('S0003','백재용','2018-03-31','CC');

select * from 학생;

/*예제8-19*/
INSERT INTO 과목(과목번호, 과목명, 구분)
VALUES ('C0001','데이터베이스실습', '전공');

INSERT INTO 과목(과목번호, 과목명, 구분, 학점)
VALUES ('C0002','데이터베이스 설계와 구축', '전공', 5); -- 학점에 들어간 check 값 넘어감.

INSERT INTO 과목(과목번호, 과목명, 구분, 학점)
VALUES ('C0003','데이터 분석', '전공', 3);

/*오류 수정*/
INSERT INTO 과목(과목번호, 과목명, 구분, 학점)
VALUES ('C0001','데이터베이스실습', '전공', 3);

INSERT INTO 과목(과목번호, 과목명, 구분, 학점)
VALUES ('C0002','데이터베이스 설계와 구축', '전공', 3);
# =====================================================================================
/*예제8-20*/
INSERT INTO 수강_1(수강년도, 수강학기, 학번, 과목번호, 성적)
VALUES('2023','1학기','S0001','C0001',4.3);

INSERT INTO 수강_1(수강년도, 수강학기, 학번, 과목번호, 성적)
VALUES('2023','1학기','S0001','C0001',4.5); -- primary key는 uniqu 해야하는데 겹침

INSERT INTO 수강_1(수강년도, 수강학기, 학번, 과목번호, 성적)
VALUES('2023','1학기','S0001','C0002',4.6); -- 성적이 check 값 벗어남.

INSERT INTO 수강_1(수강년도, 수강학기, 학번, 과목번호, 성적)
VALUES('2023','1학기','S0002','C0009',4.3); -- 과목 번호가 일치 하지 않음/ 즉 없음.

/*오류 수정*/
INSERT INTO 수강_1(수강년도, 수강학기, 학번, 과목번호, 성적)
VALUES('2023','1학기','S0001','C0002',4.4);

INSERT INTO 수강_1(수강년도, 수강학기, 학번, 과목번호, 성적)
VALUES('2023','1학기','S0002','C0002',4.3);

select * from 과목;
#==========================================================================
/*예제8-21*/
INSERT INTO 수강_2(수강년도, 수강학기, 학번, 과목번호, 성적)
VALUES('2023','1학기','S0001','C0001',4.3);

INSERT INTO 수강_2(수강년도, 수강학기, 학번, 과목번호, 성적)
VALUES('2023','1학기','S0001','C0001',4.5);
#==========================================================================
/*예제8-22*/
alter table 학생 add  constraint check(학번 like 'S%');
#==========================================================================
/*예제8-23*/
SELECT *
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE CONSTRAINT_SCHEMA = '현대학사'
AND TABLE_NAME = '학생';
#==========================================================================
/*예제8-24*/
alter table 학생 drop index 연락처;
desc 학생;

#=========================================================================
/*예제8-25*/
ALTER TABLE 학생 DROP check 학생_chk_1;

ALTER TABLE 학생 DROP check 학생_chk_2;

ALTER TABLE 학생 ADD CHECK (학번 LIKE 'S%');
#=========================================================================
/*예제8-26*/
CREATE TABLE 학생_2
    (
       학번 CHAR(5),
       이름 VARCHAR(20) NOT NULL,
       생일 DATE NOT NULL,
       연락처 VARCHAR(20),
       학과번호 CHAR(2),
       성별 CHAR(1),
       등록일 DATE DEFAULT(CURDATE()),
       PRIMARY KEY(학번),
       CONSTRAINT UK_학생2_연락처 UNIQUE(연락처),
       CONSTRAINT CK_학생2_성별 CHECK(성별 IN ('남','여')),
       CONSTRAINT FK_학생2_학과번호 FOREIGN KEY (학과번호) REFERENCES 학과(학과번호)
    );

SELECT *
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE CONSTRAINT_SCHEMA = '현대학사'
AND TABLE_NAME = '학생_2';
#=========================================================================
/*예제8-27*/
CREATE TABLE 과목평가
    (
	   평가번호 INT PRIMARY KEY AUTO_INCREMENT
      ,학번 CHAR(5) NOT NULL
      ,과목번호 CHAR(5) NOT NULL
      ,평점 INT CHECK(평점 BETWEEN 0 AND 5)
      ,과목평가 VARCHAR(500)
      ,평가일시 DATETIME DEFAULT CURRENT_TIMESTAMP
      ,FOREIGN KEY (학번) REFERENCES 학생(학번)
      ,FOREIGN KEY (과목번호) REFERENCES 과목(과목번호) ON DELETE CASCADE
    );
#=========================================================================
/*예제8-28*/
INSERT INTO 과목평가(학번, 과목번호, 평점, 과목평가)
VALUES('S0001','C0001',5,'SQL학습에 도움이 되었습니다.')
,('S0001','C0003',5,'SQL 활용을 배워서 좋았습니다.')
,('S0002','C0003',5,'데이터 분석에 관심이 생겼습니다.')
,('S0003','C0003',5,'머신러닝과 시각화 부분이 유용했습니다.');

select * from 과목평가;
#=========================================================================
/*예제8-29*/
DELETE FROM 과목 WHERE 과목번호 = 'C0003';

SELECT * FROM 과목;
SELECT * FROM 과목평가;
#=========================================================================
/*예제8-30*/
DELETE FROM 과목 WHERE 과목번호 = 'C0001'; -- 참조 무결성에 위배 되기 때문에 지울 수 없다.

select version();