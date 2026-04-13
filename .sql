CREATE TABLE `Productos` (
    producto_id = INT PRIMARY KEY, 
    producto_nombre = VARCHAR(50), 
    producto_precio = DECIMAL(10,2), 
    producto_stock = INT
);

ALTER TABLE `Productos`
   ADD category VARCHAR(100);

ALTER TABLE `Productos`
MODIFY name VARCHAR(255);

INSERT INTO Productos (producto_id, producto_nombre, producto_precio, producto_stock, category)
VALUES 
(1, 'PS5', 499.99, 87, 'Consolas'),
(2, 'Xbox Series X', 499.99, 80, 'Consolas'),
(3, 'Nintendo Switch 2', 499.99, 96, 'Consolas'),
(4, 'Trionda', 55.00, 74, 'Deporte'),
(5, 'Camiseta del FC Barcelona', 25.00, 58, 'Deporte'),

UPDATE Customers 
SET country = 'Venezuela'
WHERE customer_id = 4 OR firtname = 'Edgar';

DELETE FROM Shippings
WHERE status = 'Delivered' AND shipping_id > 200;

SELECT * FROM Customers
WHERE age > 30
AND country NOT IN ('Mexico', 'Colombia');

SELECT name, price, stock
FROM Productos
ORDER BY stock DESC, price ASC;

SELECT SUM(amount) AS total_sales
FROM Orders;
WHERE amount >= 2;

SELECT MAX(age) AS edad_maxima, MIN(age) AS edad_minima
FROM Customers;

SELECT COUNT(*) AS total_pedidos
FROM Orders;
WHERE Customer_id IN (1, 3, 5);

