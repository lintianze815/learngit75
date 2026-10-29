creat database stu_course9
go 
use stu_course
CEATE TABLE Student
(
    Sno CHAR(9)PRIMARY KEY,
    Ssex CHAR(20)UNIQE,
    Sage SMALLINT,
    Sdep CHAR(20)
)



CREATE TABLE Course
(
    Cno CHAR(4)PRIMARY KEY,
    Cname CHAR(20),
    Cpno CHAR(4),
    Ccredit SMALLINT, 
    FOREIGN KEY(Cpno)REFERENCES Course(Cno)
);

CREATE TABLE SC
(
    Sno CHAR(9),
    Cno CHAR(4),
    Grade SAMLLINT,
    PRIMARY KEY(Sno,Cno),
    
)