# Write your MySQL query statement below

-- the requirement to have a null row if the select was empty made the outer select necessary
select ifnull(
        (
            select distinct
                salary
            from employee
            order by salary desc
            limit 1
            offset
                1
        ), null
    ) as SecondHighestSalary;

-- This one was the fastest, despite what I've though.
select max(salary) as SecondHighestSalary
from employee
where
    salary < (
        select max(salary)
        from employee
    );