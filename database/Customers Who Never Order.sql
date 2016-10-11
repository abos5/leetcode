Customers Orders


-- leet code errors, should groupped
select Name as Customers
from Customers c left  join Orders o
on c.id = o.CustomerId
where o.CustomerId is null
group by o.CustomerId


-- 532ms remove group by to meet leetcode anwsers
select Name as Customers
from Customers c left  join Orders o
on c.id = o.CustomerId
where o.CustomerId is null
group by o.CustomerId


