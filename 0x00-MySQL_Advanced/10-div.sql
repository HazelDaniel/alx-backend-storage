-- A function that divides (and returns) the first by the second number
-- function SafeDiv takes 2 arguments: a, INT, b, INT
-- returns a / b or 0 if it's a zero division

DELIMITER //

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	RETURN (IF (b = 0, 0, a / b));
END //

DELIMITER ;
