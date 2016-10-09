# Write your MySQL query statement below
select max(e.Salary) as SecondHighestSalary from Employee e, (
  select max(Salary) as MaxSalary from Employee
) m
where e.Salary < m.MaxSalary

