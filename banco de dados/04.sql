CREATE FUNCTION contar_clientes_cadastrados(data_consulta DATE)
RETURNS INT
BEGIN
    DECLARE total_clientes INT;
    
    SELECT COUNT(*) INTO total_clientes
    FROM clientes
    WHERE DATE(data_cadastro) = data_consulta;
    
    RETURN total_clientes;
END;