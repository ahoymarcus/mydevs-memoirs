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

![esquema-explicativo-do-Arduino-Uno](/public/esquema-explicativo-do-Arduino-Uno.png)

<br>

## Funcionamento do Projeto








<br>

## Outros links:

 - [linkedin:] https://www.linkedin.com/in/marcus-vinicius-richa-183104199/
 - [Github:] https://github.com/ahoymarcus/
 - [My Old Web Portfolio:] https://redux-reactjs-personal-portfolio-webpage-version-2.netlify.app/


