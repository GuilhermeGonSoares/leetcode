SELECT class FROM Courses c 
GROUP BY class 
HAVING COUNT(class) >=5;