# Write your MySQL query statement below

select e1.name as Employee
from employee e1
where e1.salary > (
    select e2.salary from employee e2 where e2.id = e1.managerId
);

select e.name as Employee
from employee e
    left join employee m on e.managerId = m.id
where
    e.salary > m.salary;