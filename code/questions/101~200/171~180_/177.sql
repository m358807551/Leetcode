# https://leetcode-cn.com/problems/nth-highest-salary

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
      set N = N -1;
  RETURN (
      select distinct salary
    from Employee
    order by salary desc
    limit N, 1
  );
END
