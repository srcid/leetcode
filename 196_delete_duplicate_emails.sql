# Write your MySQL query statement below

delete q
from person p
    join person q on p.email like q.email
    and p.id < q.id;