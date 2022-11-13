SELECT customer_number FROM (SELECT  customer_number ,COUNT(*) as pedido FROM orders
GROUP BY customer_number) o WHERE o.pedido IN (SELECT MAX(pedido) FROM 
(SELECT  customer_number , COUNT(*) as pedido FROM orders o 
GROUP BY customer_number) X)