DELIMITER //

CREATE PROCEDURE relatorio_compras_diario()
BEGIN
    DECLARE data_atual DATE;
    
    SET data_atual = CURDATE();
    
    SELECT DATE(data_compra) AS data, COUNT(*) AS quantidade
    FROM compras
    WHERE DATE(data_compra) = data_atual
    GROUP BY DATE(data_compra);
END;
//

DELIMITER ;
