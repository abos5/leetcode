

-- 1018 ms normal solve
select e.Name as Employee from Employee e inner join Employee m
on e.ManagerId = m.Id
where e.Salary > m.Salary


-- 1276 ms sub join
select e.Name as Employee from Employee e where
ManagerId is not null and
Salary > (select Salary from Employee m where m.Id=e.ManagerId)


-- 1069 ms move where to on
select e.Name as Employee from Employee e inner join Employee m
on e.ManagerId = m.Id
and e.Salary > m.Salary

-- 983 ms left join beats inner join
select e.Name as Employee from Employee e left join Employee m
on e.ManagerId = m.Id
where e.Salary > m.Salary

-- 1020 ms no direct join
select e.Name as Employee from Employee e, Employee m
where e.ManagerId = m.Id and e.Salary > m.Salary


-- 1066 ms no direct join and reverse conditions
select e1.Name as Employee
from Employee e1, Employee e2
where e1.Salary > e2.Salary and e1.ManagerId = e2.Id;