create database if not exists 현대학사 default charset utf8mb4 collate utf8mb4_general_ci;

-- 현대학사를 관리하는 직원을 등록하고 , 접속 권한을 부여하고 등록한 직원으로 접속하세요.
create user hak@localhost identified by '현대학사';
grant all privileges on 현대학사.* to 'hak'@'localhost';
commit;

create user hak2@localhost identified by 'mysql1234';
grant all privileges on 현대학사.* to 'hak2'@'localhost';
commit;

DROP USER IF EXISTS 'hak'@'localhost';
flush privileges;