# Write your MySQL query statement below
#select salary from Employees where employee_id % 2 = 0 or name like 'M%';

select employee_id,
case when employee_id % 2 <> 0 and name not like 'M%' then salary
else 0
end
as bonus
from Employees
order by employee_id;