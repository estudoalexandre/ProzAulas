let titulo = document.createElement("h1");
titulo.textContent = "Produto em Destaque";
titulo.id = "titulo";
document.body.appendChild(titulo);
document.body.style.textAlign = "center"

let produto = document.createElement("div");
produto.classList.add("produto");

let nome = document.createElement("h2");
nome.textContent = "Smartphone S20";
produto.appendChild(nome);

let descricao = document.createElement("p");
descricao.textContent = "Este smartphone possui uma câmera de alta resolução e bateria de longa duração.";
produto.appendChild(descricao);

let preco = document.createElement("p");
preco.textContent = "Preço: R$ 999,99";
produto.appendChild(preco);

let imagem = document.createElement("img");
imagem.src = "https://i.zst.com.br/thumbs/12/37/3a/-794835717.jpg"; 
imagem.alt = "Smartphone S20";
produto.appendChild(imagem);
imagem.style.width = "400px"

document.body.appendChild(produto);
