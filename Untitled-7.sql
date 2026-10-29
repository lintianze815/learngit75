SELECT 
    l.Eno,
    e.Ename AS 企业名称,
    l.Bno,
    b.Bname AS 银行名称,
    l.Ldate,
    l.Amount,
    l.Term
FROM loant l
INNER JOIN legalentityt e 
    ON l.Eno = e.Eno
INNER JOIN bankt b 
    ON l.Bno = b.Bno;

