# https://leetcode-cn.com/problems/second-highest-salary

select ifnull(
           (select distinct salary
from employee
order by salary desc
limit 1, 1), null
         ) as SecondHighestSalary

