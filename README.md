# TEIA
Trabalho para a disciplina de tópicos especiais em inteligência artificial

## Informações:

**Tema:** O uso de inteligência artificial para identificar e classificar pelo número
de relevância os assuntos tratados dentro um conjunto de áudios de um
dispositivo para uma perícia criminal </ br>
**Por: Breno Felix de Souza**  
  
## Relatório:
## Treinamento
Eu utilizei um modelo criado apartir de uma competição de espetograma e mais 5 modelos de Transfer Learning. Os modelos criados foram
: 
# desnet
 ![Banana](https://cdn.discordapp.com/attachments/451788828513140756/615511323702198285/unknown.png)
 ## 54.565mb

# xception
![Banana](https://cdn.discordapp.com/attachments/451788828513140756/615511388152135686/unknown.png)
## 87.429mb
# resnet
![Banana](https://cdn.discordapp.com/attachments/451788828513140756/615511448214568991/unknown.png)
## 98.177mb
# inception
![Banana](https://cdn.discordapp.com/attachments/451788828513140756/615511528396947466/unknown.png)
## 89.439mb
# vgg
![Banana](https://cdn.discordapp.com/attachments/451788828513140756/615512564549419018/unknown.png)
## 79.481mb

Apesar desses valores, ao realizar o teste, o inception teve grandes problemas ao garantir a classe definida, e deu mais de 50% de erro nos testes realizados.

# Execução

Para executar o algoritmo, é retirado dentro de um áudio diversos espetogramas .A cada 0,5 segundo, um segundo inteiro é realizado o esptograma e executado o modelo de treinamento para identificar a classe correspondente.

# Contexto: 
<p>Como gravações de áudio e vídeo vêm se tornando extremamente
popular em nosso dia a dia, consequentemente estão sendo muito
utilizadas como provas nas mais diversas circunstâncias (lembre-se que
muitas vezes é necessária autorização judicial para fazer determinadas
gravações).</p>
<p> Desta forma notamos a responsabilidade da função do perito que em
muitos casos passa semanas sobre pequenos trechos de inúmeros
áudios ou outros materiais, onde através da Perícia de Áudio é capaz
de criar provas concretas e seguras que podem levar um culpado à sua
condenação.</p>
<p>Os exames realizados em aparelho mobile deve ter um objetivo
especificado, assim o examinador precisa conhecer e ter uma prévia
dos dados que estão coletando. Caso contrário, o relatório (laudo) não
passará de uma simples extração das informações que estavam no
telefone celular para outro tipo de suporte.</p>
<p>Ao se deparar com essa premissa, um dispositivo de um usuário
comum atualmente pode possui diversos tipos de arquivos de áudios,
principalmente de conversas com outros indivíduos, e o trabalho para
analisar inúmeras conversas em um pequeno período de tempo muitas
vezes reduzido dependendo da investigação, é grande. O exame de
texto é simples e pode usar um software simples de busca para localizar
palavras chaves em sua análise, mas com o áudio fica muito mais difícil
de fazer pela complexidade de tipos de áudio, ambientes e ruídos que
pode haver no objeto de análise, portanto requer muito tempo
desperdiçado do perito.</p>
<p>O objetivo desse trabalho é facilitar a busca entre palavras chaves em
um número grande de áudios e classifica-los devido ao seu grau de
possibilidade do assunto para a análise manual do perito, ou seja,
ordenar os arquivos de áudio para a possibilidade de obter a informação
desejada.</p>
<p>O uso de Deep learning é crucial pelo cenário do uso grande de dados,
pois ele tem uma vantagem de potencialmente fornecer uma solução
para abordar a análise de dados e problemas de aprendizado
encontrados em volumes massivos de dados de entrada. Mais
especificamente, auxilia na extração automática de representações de
dados complexos de grandes volumes de dados não supervisionados.</p>

## Dados:  
[Dados utilizados](https://github.com/PascalBreno/Detector-de-palavras/blob/master/dados.md)

## Referência:
André Morum de lIma Simão (2011). Proposta de método para análise pericial em
smartphone com sistema operacional Android. Dissertação de mestrado em
engenharia elétrica. </br>
**Sobre:** Esse trabalho de conclusão de curso aborda a forma exposta para se obter
através da perícia as amostras de dados em uma investigação, tal como o trabalho
do perito na análise de dados de áudio individual.
Olivier Lézoray, Christophe Charrier, Hubert Cardot e Sébastien Lefèvre, EURASIP
Journal on Advances in Signal Processing20082008:927950 “Machine Learning in
Image Processing” </br>
URL: [https://doi.org/10.1155/2008/927950](https://doi.org/10.1155/2008/927950) </br>
**Sobre:** O tratamento de imagem pode ser utilizado de maneiras diferente,
dependendo da forma que for utilizado e principalmente pelo tempo que aquilo
precisa ser processado para gerar um resultado em escala. No artigo do jornal ele
explica sobre vários trabalhos criados e artigos científicos para o tratamento de
imagem em uma rede de aprendizado de máquina. </br>
A. H. Moore, M. Brookes and P. A. Naylor, "Roomprints for forensic audio applications,"
2013 IEEE Workshop on Applications of Signal Processing to Audio and Acoustics, New
Paltz, NY, 2013, pp. 1-4. </br>
URL:
[http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6701854&isnumber=6701802]([http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6701854&isnumber=6701802) </br>
**Sobre:** O deep Learning tem uma vantagem de potencialmente fornecer uma solução
para abordar a análise de dados e problemas de aprendizado encontrados em volumes
massivos de dados de entrada. Mais especificamente, auxilia na extração automática de
representações de dados complexos de grandes volumes de dados não supervisionados.
Hafiz Malik, Hasan Mahmood(2014). “Acoustic environment identification using
unsupervised learning”. Magazine: Security Informatics 2014 Published: 2
September 2014 </br>
URL: [https://doi.org/10.1186/s13388-014-0011-7](https://doi.org/10.1186/s13388-014-0011-7) </br>
**Sobre:** Uma implementação de IA para identificar certos ambientes através da
análise do áudio. O ponto principal é identificar e modularizar os pontos chaves do
áudio utilizando uma IA para identificar esses valores, para que assim você possa
fazer o processo de classificação. </br>
Hafiz MalikEmail e Hasan Mahmood, (2014). “Acoustic environment identification
using unsupervised learning”, Journal of big Data.
**Sobre:** Tipos de identificar áudios através de uma rede neural não supervisionada 
