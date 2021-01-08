# https://leetcode-cn.com/problems/combine-two-tables

select FirstName, LastName, City, State
from Person p
left join Address a
on p.PersonId = a.PersonId
