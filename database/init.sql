create database test_db;

create user my_user identified by '123456';
grant all privileges on test_db.* to my_user;

use test_db;

create table user_key (
  id int not null auto_increment,
  s_id varchar(50),
  account varchar(50) not null,
  hash_key varchar(500) not null,
  hash_salt varchar(20) not null,
  primary key (id, account)
);

create table todo (
  id int not null auto_increment,
  user_id int not null,
  title varchar(20),
  content varchar(200),
  primary key (id, user_id)
);
