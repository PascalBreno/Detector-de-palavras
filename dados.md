## Dados utilizados na realização do trabalho:  
Para a realização do trabalho, resolvi fazer uma pesquisa simples sobre gírias para um tipo de droga em especifica para dar introdução ao banco de dados.
A fonte da pesquisa foi no site EducBrasil sobre gírias no mundo das drogas.

* Acochar - apertar o cigarro de maconha
* Bhang - maconha'
* Marijuana - maconha
* Manga-rosa - maconha de boa qualidade
 
Coletei audios de mais de 10 voluntários para a realização da base de dados.

Para a base de dados ser completa e se adaptar para o projeto, eu extrai os audios no formato ogg (Formato usado para áudios em Aplicativos de Mensagens). Para transformar a base de dado sem espectograma realizei o algoritmo main.py, onde ele irá identificar a pasta onde deve procurar os audios, converter um por um dos audios para a palavra descrita e armazenar em sua pasta especifica de treinamento para treinar a Rede.

O algoritmo utliza as bibliotecas:
* numpy <Trabahar com Array>
* pydub <b>Manipulação de áudio </b>
* librosa <b>Carregar os arquivos WAV e pegar suas frequências </b>
* os <b> Listar os diretórios de uma pasta em um Array </b>

<p>Atualmente estou com mais de 400 audios, mas irei adicionar mais a rede com o tempo</p>
<p>Ao finalizar a conversão do espectograma, e depois de fazer o treinamento, eu adiciono uma tag no nome para o programa identificar que a imagem já foi treinada podendo adicionar constantemente novas entradas de dados sem alterar o que já foi feito</p>
