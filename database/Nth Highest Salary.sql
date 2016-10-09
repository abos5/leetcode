
-- 615 ms 61.2%
-- 613 ms 65.5%

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set @CT=(select count(distinct(salary)) as ct from Employee order by salary desc limit 0, N);
  RETURN (
        if (
            @CT >= N,
            (
                select min(salary) from (
                    select distinct(salary) as salary from Employee order by salary desc limit 0, N
                )t
            ),
            null
        )
  );
END