# Criando Um Sistema de Reconhecimento Facial do Zero - Desafio 5
 
Olá, este é o meu repositório para o quinto desafio do bootcamp "BairesDev - Machine Learning Training" da Dio.me! 

<br>

## Entendendo o Problema

Neste laboratório do prof. Diego Renan, o objetivo é criar um sistema de detecção e de classificação de imagem utilizando o framework **TensorFlow**, em conjunto com as bibiliotecas Python necessárias para se alcançar o resultado pretendido:

1. Criar um modelo de detecção treinada para detectar faces.
2. Utilizar uma rede de classificação para classificar a face detectada.


Finalmente, tendo apresentado acima os requisitos definidos pelo professor para o desafio/laboratório, e considerando que este quinto desafio do curso, "BairesDev - Machine Learning Training", se insere dentro do sexto módulo das disciplinas, "Frameworks de Deep Learning", o qual tem justamente aquele framework **TensorFlow** como elemento central, decidimos, então, começar a entender esse problema bucando conhecer um pouco mais sobre esta ferramenta e como ela se integração com as demais bibliotecas, recursos e funcionalidades do ecossoistema Python para se alcançar os resultados almejados neste trabalho.


<br>

## O Framework _TensorFlow_

O primeiro ponto a ser notado é que, enquanto algumas referências parecem tratar o **TensorFlow** como sendo mais uma biblioteca para machine learning, outras parecem tratá-lo de um modo mais abrangente como sendo uma ferramente, enquanto que no site de sua mantenedora [Tensorflow.org](https://www.tensorflow.org/?hl=pt-br) ele chega mesmo a ser tratado como sendo uma "plataforma completa" de machine learning.


De qualquer forma, a plataforma do [tensorflow.org](www.tensorflow.org) apresenta um Notebook Colab para um teste rápido dessa experiêcia com o uso do TensorFlow que basicamente roda o seguinte código:

```
import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
  loss='sparse_categorical_crossentropy',
  metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
``` 


Acima, mesmo nesse pequeno exemplo de entrada para o recurso, realmente vemos o que parece ser uma presença marcante do TensorFlow através de vários do que poderíamos chamar de **"Ciclo de Vida do machine learning"**:

1. O TensorFlow é chamado (ou ativado) como qualquer outra biblioteca Python através de um import padrão.
2. Que o TensorFlow realiza uma função de "alto nível" para acessar um conjunto de dados do **MNIST** utilizando-se de uma outro funcionalidade Python, a **Keras** (biblioteca de alto nível desenvolvida sobre Theano e TensorFlow - [databricks.com/br/glossary/keras-model](www.databricks.com/br/glossary/keras-model):   
    2.1. No glossário de Databricks.com, **Keras** é tratado como uma API para a criação de camadas e de arquiteturas de Deep Learning e Redes Neurais, de modo que parece ficar claro que em meio aquela simples chamada de alto nível feita pelo TensorFlow para o banco de dados **MNIST**, ele estaria gerenciando conexões tanto com a API do Keras, quanto com o banco de dados do **MNIST**.
3. Depois, novamente acionando a API do Keras, o TensorFlow faz uma chamada para a construção do que parece ser um "modelo sequencial" de machine learning.
4. Mas a gestão do TensorFlow não parece ter acabado, porque através do controle exercido por sobre a variável **model** o TensorFlow também realizaria o treinamento do modelo.
5. Para na sequência, ainda com o controle da variável **model** avaliar o modelo criado, calculando a sua acurácia.


Assim, parece mesmo que atrevés dessa pequena experiência introdutória apresentada no tutorial do site do TensorFlow, "[TensorFlow 2 início rápido para iniciantes](https://www.tensorflow.org/tutorials/quickstart/beginner?hl=pt-br)", com o treino de um pequeno modelo de classificação de imagens, que este recurso chamado de TensorFlow parece cumprir tudo aquilo que dele era esperado ao começo da experiência, isto é:

1. Que ele integraria toda a aplicação Python como a mesma naturalidade e a mesma flexibilidade de qualquer outra biblioteca da linguagem.
2. Que uma vez acionado ele desencadearia a chamada de diferentes recursos relacionados à operação de machine learning (acesso aos dados, construção do modelo, treinamento do modelo e avaliação do modelo), como é esperado de ferramentas digitais em geral, e neste caso específico, de uma ferramenta de machine learning.
3. Que ele também realizaria operações ou agiria como uma espécie de "recurso de gestão e controle" para outros recursos ainda, tal qual fora feito ao se utilizar de chamadas à API Keras de Deep Learning para gerenciar as etapas de acesso aos dados do MNIST e para a construação do modelo de detecção de imagens, tal qual se poderia esperar de uma **Plataforma de Desenvolvimento Completa** para machine learning.


<br>

## Contruindo um Modelo de Detecção e Classificação Facial

Primeiramente, considerando o objeto do desafio em questão, bem como de tudo o que foi apresentado pelo prof. Renan ao longo do curso, um modelo de **Detecção e Classificação Facial** remonta a uma operação bastante especializada, uma vez que tal modelo precisa primeiramente detectar os objetos presentes em uma imagem, marcar todos em relação às suas posições ou atributos que os individualizam, para ao final ainda fazer a sua predição para a classificação de cada um desses objetos encontrados e marcados.

![imagem de uma rede-de-detecção-de-imagens](./public/rede-de-detecção-de-imagens.png)


<br>

A imagem acima foi tirada do material do curso do prof. Renan, e mostra justamente o ciclo de trabalhos necessários que precisam ser feitos sobre uma imagem em uma operação de **detecção e classificação** de imagens ou faces, em que primeiramente é preciso serem detectados e marcardos todos os objetos encontrados dentro de uma imagem com as chamadas linhas de **bounding boxes**, para só ser possível proceder à classificação de cada objeto detectado na imagem:

![Imagem para o desafio-5 de reconhecimento-faces big-bang-theory](./public/desafio-5-reconhecimento-faces-big-bang-theory.png)


> [!IMPORTANT]
> Por meio da Figura 1 é possível visualizar o resultado esperado para o modelo proposto, devendo detectar e reconhecer mais de uma face ao mesmo tempo:     
> 1. Utilizar uma rede de detecção treinada para detectar faces.   
> 2. Utilizar uma rede de classificação para classificar a face detectada.   


<br>

Observando, então, a complexidade relacionada às aplicações de machine learning para a **detecção e classificação de faces**, bem como os requisitos definidos para este desafio em particular, fora decidido trabalhar o problemde acordo da estrutura a seguir:

- Simplificar o projeto, dividindo-o em dois módulos mais simples, o que também poderia permitir gerenciar e tratar da otimização de cada um deles separadamente:

1. A utilização de um modelo inicial para a detecção de imagens, isto é, faces: o modelo **MTCNN**.
2. A utilização de um modelo básico para a classificação final das imagens. 







![Tela da aba Dashboard com a visualização final do relatório de um dashboard Xbox](/public/desafio-3_aba-Dashboard-do-dashboard-Xbox_excel.png)



<br>

## Outros links:

 - [linkedin:] https://www.linkedin.com/in/marcus-vinicius-richa-183104199/
 - [Github:] https://github.com/ahoymarcus/
 - [My Old Web Portfolio:] https://redux-reactjs-personal-portfolio-webpage-version-2.netlify.app/


