-- MySQL
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE result INT;
    
    IF n <= 0 THEN
        RETURN NULL;
    END IF;

    SET result = NULL;

    SET n = N - 1;

    SELECT DISTINCT salary INTO result
    FROM employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET n;

    RETURN result;
END

-- PostgreSQL
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  IF n >= 1 THEN
    RETURN QUERY (
        select distinct e.salary
        from employee e
        order by e.salary desc
        offset N-1
        limit 1);
  END IF;
END;
$$ LANGUAGE plpgsql;