

select Email from Person group by Email having count(1) > 1;


select Email from Person group by Email having count(Id) > 1;
