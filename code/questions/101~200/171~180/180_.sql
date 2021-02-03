# https://leetcode-cn.com/problems/consecutive-numbers

select Num as ConsecutiveNums from (
       select Num, count(*) as count from Logs
group by Num
having count > 2
                  )t
