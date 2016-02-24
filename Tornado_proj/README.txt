
一。 mysql：
建立一个数据库：
create database qiwsirtest character set utf8;
创建一张表：
create table users(id int(2) not null primary key auto_increment,username varchar(40),password text,email text)default charset=utf8;
插入一条数据
insert into users(username,password,email) values("qiwsir","123123","qiwsir@gmail.com");