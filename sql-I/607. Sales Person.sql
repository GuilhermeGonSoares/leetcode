SELECT name FROM SalesPerson sp 
WHERE name NOT IN (SELECT sp.name FROM Orders o 
INNER JOIN Company c on o.com_id = c.com_id 
RIGHT JOIN SalesPerson sp ON o.sales_id = sp.sales_id 
WHERE c.name = 'RED')