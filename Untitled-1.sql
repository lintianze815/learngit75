create database stu_course default
character set utf8mb4;
use stu_course;
create table student
(Sno char(9) primary key,
Sname char (8) not null,
Ssex char (1),
Sage tinyint,
Sdept varchar (20)
);
create table Course
(Cno char(5) primary key,
Cname varchar(40) not null,
Ccredit smallint,
Cpno char (5),
foreign key(Cpno)references Course(Cno)
);
create table SC
(Sno char(9),
Cno char(4),
Grade smallint,
primary key(Sno,Cno),
foreign key(Sno)references student(Sno),
foreign key(Cno)references Course(Cno)
);
alter table student add S_entrance date;
use stu_course;
alter table student modify Sage int;
use stu_course;
alter table Course add unique(Cname);
use stu_course;
create index Stusname on Student(Sname);
use stu_course;
create unique index Stusno on Student(Sno);
create unique index Coucno on Course(Cno);
create unique index SCno on SC(Sno asc,Cno desc);
use stu_course;
drop index Stusname on Student;
use stu_course;
insert into Course(Cno, Cname) values(1, '数据库');
insert into Course(Cno, Cname) values(2, '数学');
insert into Course(Cno, Cname) values(3, '信息系统');
insert into Course(Cno, Cname) values(4, '操作系统');
insert into Course(Cno, Cname) values(5, '数据结构');
insert into Course(Cno, Cname) values(6, '数据处理');
insert into Course(Cno, Cname) values(7, 'PASCAL语言');
update Course set Cpno = 5, Ccredit = 4 where Cno = 1;
update Course set Ccredit = 2 where Cno = 2;
update Course set Cpno = 1, Ccredit = 4 where Cno = 3;
update Course set Cpno = 6, Ccredit = 3 where Cno = 4;
update Course set Cpno = 7, Ccredit = 4 where Cno = 5;
update Course set Ccredit = 2 where Cno = 6;
update Course set Cpno = 6, Ccredit = 4 where Cno = 7;
set sql_safe_updates=0;
select *from Course;