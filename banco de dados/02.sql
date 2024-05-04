CREATE DATABASE biblioteca;


CREATE TABLE autores (
    autor_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE editoras (
    editora_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE livros (
    livro_id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200),
    autor_id INT,
    editora_id INT,
    FOREIGN KEY (autor_id) REFERENCES autores(autor_id),
    FOREIGN KEY (editora_id) REFERENCES editoras(editora_id)
);

CREATE TABLE emprestimos (
    emprestimo_id INT AUTO_INCREMENT PRIMARY KEY,
    livro_id INT,
    data_emprestimo DATE,
    data_devolucao DATE,
    FOREIGN KEY (livro_id) REFERENCES livros(livro_id)
);



CREATE TRIGGER registrar_emprestimo AFTER INSERT ON emprestimos
FOR EACH ROW
BEGIN
    DECLARE livro_titulo VARCHAR(200);

    SELECT titulo INTO livro_titulo FROM livros WHERE livro_id = NEW.livro_id;
    
    INSERT INTO logs_emprestimos (livro_emprestado, data_emprestimo)
    VALUES (livro_titulo, NEW.data_emprestimo);
END;

