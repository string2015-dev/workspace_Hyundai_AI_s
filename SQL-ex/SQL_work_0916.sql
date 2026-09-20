-- bookorder 파일 준비
use bookstore;
create table book_order(
order_id varchar(10) primary key,
book_id varchar(10),
customer_name varchar(30),
qty int,
order_date date,
request_date date,
ship_date date,
foreign key (book_id) references book(book_id)
);

-- 문제1
select title 도서명 ,rpad(left(title,6),6,'.') 미리보기
from book;

-- 문제2
select concat_ws('-',left(book_id,2),right(book_id,4)) 도서신규코드
from book_order;

-- 문제3
select concat(left(author,1),repeat('*',char_length(author)-1)) 저자_마스킹
from book;

-- 문제 4
select title 도서명, price 정가
, round(price*(100-discount_rate)/100,1) 할인가
, truncate(price*(100-discount_rate)/100,-2)
from book;