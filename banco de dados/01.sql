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

INSERT INTO autores (nome) VALUES ('Machado de Assis'), ('Clarice Lispector'), ('Carlos Drummond de Andrade');

INSERT INTO editoras (nome) VALUES ('Companhia das Letras'), ('Record'), ('L&PM Editores');

INSERT INTO livros (titulo, autor_id, editora_id) VALUES
('Dom Casmurro', 1, 1),
('A Hora da Estrela', 2, 2),
('A Rosa do Povo', 3, 3);

SELECT livros.titulo, autores.nome AS autor, editoras.nome AS editora
FROM livros
JOIN autores ON livros.autor_id = autores.autor_id
JOIN editoras ON livros.editora_id = editoras.editora_id;

