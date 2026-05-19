# Arduino com Sensor de Temperatura Analógico e Multímero -- Prototipação 
 
O objetivo deste trabalho é de testar o uso do Arduino para gerenciar um modelo de dispositivos interligados para simular a medição da temperatura do ambiente com um sensor analógico, de forma que, a  partir dos valores que forem sendo lidos pelo sensor, o Arduino possa decidir que decisões tomar, o que no caso, significa decidir quais os leds devem ser acesos ou apagados com as mudanças na temperatura medida. 


Observe ainda, que o uso do Arduino em projetos deste tipo não é simplesmente para se permitir a ligar dispositivos entre si, isto porque essa tarefa bem poderia ser feita sem o uso dele, mas precisamente para permitir inserir processamento e decisão neste modelo, de forma que com o Arduino, passamos a poder gerir a todo o sistema de forma integrada. 


Abaixo vemos um simples arranjo de três dispositivos que se ligam para o acendimento de um led sem precisar da participação do Arduino para isso:

![circuito-simples-pilha-resistor-led](/public/circuito-simples-pilha-resistor-led.png)

<br>


Contudo, quando trabalhamos dessa maneira, não possuímos uma forma prática para fazer o gerenciamento desse modelo, porque para alterarmos o funcionamento do sistema acima, somos obrigados a fazer tudo isso manualmente, como, por exemplo, quando queremos desligar o led e precisamos de cortar a ligação da bateria manualmente.


Do outro lado, quando a gestão é feita pelo Arduino, o projeto pode ser plenamente automatizado, inclusive com a utilização de uma versão da linguagem de programação C++, como poderá ser visto ao longo do projeto.


<br>

## Componentes Utilizados

Neste projeto são utilizados os seguintes componentes:
 - Arduino UNO
 - Placa Protoboard
 - 9 Leds
 - 9 Resistores
 - Sensor de temperatura TMP-36
 - Multímetro


Para esse arranjo de componentes, o Arduino é responsável pelo gerenciamento do sistema e pela distribuição de energia, enquanto que a placa Protoboard é utilizada para permitir a arrumação dos circuitos de forma facilitada e mais limpa.


Assim, caberá ao Arduino fazer o envio de corrente para carregar a placa Protoboard por meio do pino 5V, bem como receber de volta a polaridade de carga negativa da corrente para fechar o circuito através do pino GND. Ademais, também é utilizado o pino analógico A0 do Arduino para receber a leitura de um sensor de temperatura analógico, enquanto são usados os pinos digitais de 5 a 13 para gerenciar o envio de energia para o acendimento individual de cada um dos leds usados. 


Contudo, os leds não podem ser alimentados diretamente pela placa Protoboard, que recebe os 5 Volts do Arduino, de modo que são usados nove resistores para restringir a quantidade de corrente para 220 Ohm, evitando assim queimar os dispositivos.


Finalmente, também será usado um multímetro para nos permitir acompanhar a operação de conversão do valor analógico que é feito pelo sensor para a temperatura em graus Célsius, uma vez que segundo a documentação da plataforma Tinkercad, o pino central do sensor é capaz de mudar o seu valor de saída de acordo com as variações captadas no ambiente, trabalhando dentro da faixa de uma faixa de valores de 0 a 1023, de forma que caberá, então, a uma função de mapeamento usada no Arduino para fazer a conversão final daqueles valores para a faixa de -40º até 125º Celsius. 


Na figura abaixo temos um esquema geral explicativo da placa Arduino UNO:

![esquema-explicativo-do-Arduino-Uno](/public/esquema-explicativo-do-Arduino-Uno.jpeg)

<br>

## Funcionamento do Projeto

Como dito, então, o projeto funciona seguindo o gerenciamento do Arduino e a prototipagem da placa Protoboard, de forma que o Arduino envia sinal de corrente de 5V para alimentar o sistema, recebendo de volta no pino GND as cargas negativas para garantir o fechamento do circuito. Veja que nas imagens abaixo da próxima seção, os fios que conduzem carga positiva foram padronizados com a cor vermelha, enquanto os que têm carga negativa têm a cor preta.


Embora os leds e os resistores estejam posicionados na placa Protoboard para permitir uma melhor arrumação (e ela esteja recebendo corrente do Arduino), não será a placa a responsável por alimentar os leds com energia, pois como discutimos antes, queremos que seja o próprio Arduino o responsável por controlar de forma automatizada o acendimento e o apagamento dos leds de acordo com algoritmo definido nele.   

Do outro lado, o sensor de temperatura também está posicionado na Protoboard, sendo que dessa vez será a própria placa que o alimentará com energia, afinal, o sensor não precisa ser controlado diretamente pelo Arduino, mas apenas enviar ao Arduino as suas medições que, depois de recebidas, elas são tratadas por ele com um delay de um segundo, que também está definido na programação feita.


Assim, de posse da informação recebida pelo sensor, o Arduino usa a seguinte expressão para fazer a conversão do sinal enviado pelo sensor para o padrão da temperatura Celsius:

    - **val_celsius = map(((analogRead(A0) - 20) * 3.04), 0, 1023, -40, 125);** 


Vemos na expressão que o valor recebido pelo sensor é subtraído de vinte e multiplicado por 3,04. Já a segunda parte da expressão descreve de um lado a faixa de funcionamento do sensor (de 0 a 1023) e a faixa de capacidade de operação do mesmo, que vai de -40º até 125º Célsius. Ou seja, um sensor mais potente ou ainda um sensor voltado para operações mais específicas poderia ter uma outra capacidade de operação, de forma que, então, deveríamos relacionar a sua nova capacidade de operação correlacionando com o seu valor de funcionamento naquela função de mapeamento.


Na sequência, após o valor recebido do sensor ser convertido para um valor em Célsius, esse valor é usado no algoritmo do Arduino para decidir quais leds acenderão a cada momento.


Para ajudar a visualizar todo esse processo de conversão, utilizamos dois sistemas, como poderá ser visto mais adiante:

1. Método Serial.begin(9600) do Arduino
2. Multímetro


O primeiro permite que possamos jogar o valor recebido pelo pino A0 para um terminal de uso ou um “Monitor Serial”, tal qual a plataforma Tinkercad disponibiliza logo abaixo da caixa de texto de codificação:

![monitor-serial-da-plataforma-tinkercad](/public/monitor-serial-da-plataforma-tinkercad.png)

<br>





<br>

## Outros links:

 - [linkedin:] https://www.linkedin.com/in/marcus-vinicius-richa-183104199/
 - [Github:] https://github.com/ahoymarcus/
 - [My Old Web Portfolio:] https://redux-reactjs-personal-portfolio-webpage-version-2.netlify.app/


