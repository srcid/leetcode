select email as Email
from person p
group by
    email
having
    count(1) > 1;

select distinct
    p.email as Email
from person p
    join person q on p.email like q.email
    and p.id <> q.id;