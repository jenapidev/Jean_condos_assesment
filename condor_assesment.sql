CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    amount DECIMAL(10, 2),
    date DATE
);

CREATE TABLE invoice_items (
    id SERIAL PRIMARY KEY,
    auto_transfer INT NOT NULL,
    amount DECIMAL(10, 2),
    description VARCHAR(255),
    FOREIGN KEY (auto_transfer) REFERENCES invoices(id)
);

INSERT INTO invoices ("amount", "date")
values (100, '2020-12-24'),
       (200, '2020-12-12'),
       (300, '2020-11-20');
       
       
INSERT INTO invoice_items (id, amount, auto_transfer, description)
values (100, 50, 1, 'carnes'),
       (101, 25, 1, 'cereales'),
       (102, 25, 1, 'sal'),
       (103, 150, 2, 'bebidas'),
       (104, 50, 2, 'carnes'),
       (105, 10, 3, 'cereales'),
       (106, 100, 3, 'carnes'),
       (107, 100, 3, 'café'),
       (108, 90, 3, 'frutas');
       

CREATE VIEW invoices_view AS
SELECT 
    inv.id AS invoice_id,
    inv.amount AS total_amount,
    SUM(CASE WHEN items.description = 'carnes' THEN items.amount ELSE 0 END) AS carnes,
    SUM(CASE WHEN items.description = 'cereales' THEN items.amount ELSE 0 END) AS cereales,
    SUM(CASE WHEN items.description NOT IN ('carnes', 'cereales') THEN items.amount ELSE 0 END) AS others
FROM 
    invoices inv
JOIN 
    invoice_items items ON inv.id = items.auto_transfer
GROUP BY 
    inv.id, inv.amount;
    
SELECT *
FROM invoices_view ORDER BY invoice_id ASC;