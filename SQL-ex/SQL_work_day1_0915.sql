create database if not exists bookstore;
use bookstore;

create table book(
book_id varchar(10) primary key,
title varchar(100) not null,
category varchar(20),
author varchar(30),
price int,
stock int,
discount_rate int,
pub_date date,
publisher varchar(30)
);
-- 실습1번
select *
from book ;

-- 실습2번
select title 도서명,author 저자명,price 판매가
from book;

-- 실습3번
select title 도서명,author 저자명,discount_rate 할인율,round(price*(100-discount_rate)/100,0) 할인가
from book;

-- 실습4번
select title 도서명, author 저자, price 정가
from book
where price >= 20000
order by price desc;

-- 실습 5번
select *
from book
where category = "it";

-- 실습 6번
select title 출판사, publisher 출판사
from book
where publisher != '비즈니스북스';

-- 실습 7번
select title 도서명, stock 재고수량
from book
where stock < 10
order by stock ;

-- 실습 8번
select title 도서명, price 정가
from book
where category = '에세이'
order by 2 desc;

-- 실습 9번
select distinct category 분야
from book
order by category;

-- 실습 10번
select title 도서명, author 저자, round(price*(100-discount_rate)/100,0) 추천가
from book
where stock >= 5 and price*(100-discount_rate)/100 <= 15000
order by 3 ;