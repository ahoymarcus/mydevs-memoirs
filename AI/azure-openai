# Azure OpenAI

De acordo com a documentação da [Microsoft](https:///en-us/azure/ai-services/openai/overview), a Azure OpenAI Service é uma API REST que funciona como interface para chamada dos modelos de linguagem para inteligência artificial da Microsoft e da OpenAI, incluindo GPT-3,5-Turbo, GPT-4o and GPT-4, etc.

Ademais, ainda segundo o site, todos esses modelos podem ser facilmente adaptados para o provimento de tarefas específicas, como, por exemplo, criação de conteúdo, sumarização, entendimento de imagem,busca semântica e tradução de linguagem natural, etc.


> "With Azure OpenAI, customers get the security capabilities of Microsoft Azure while running the same models as OpenAI. Azure OpenAI offers private networking, regional availability, and responsible AI content filtering."
> [What is Azure OpenAI Service - at learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)

Em termos de usabilidade, acrescenta a documentação, o uso da API é bastante flexível e pode ser acessada por um usuário simplismente com o uso de um terminal de prompt para fazer chamadas ao serviço:

Um exemplo apresentado pelo site:
> Prompt: """ count to 5 in a for loop """\
> Completion: for i in range(1, 6): print(i)


## Funcionamento da API OpenAI

O serviço da API OpenAI funciona por meio de tokens, que são o resultado do processo de análise e quebra dos textos inseridos como entrada num terminal de chamada da API em suas partes mais simples, incluindo aí a análise dos espaços em branco inseridos.

Note que o número de tokens gerado em cada acesso da API vai depender diretamente do modelo de IA escolhido na chamada, bem como os parâmetros definidos, incluindo questões relacionadas com a latência do processo e a magnitude de saída de dados.

Observe que também a análise de imagens resulta na análise e quebra em tokens, de forma que novamente o resuldado do processo vai depender dos modelos e configurações definidos, como já dito, bem como do nível de detalhamento das imagens e de suas dimensões.


### Recursos, Desenvolvimento e Engenharia de Prompt

Os recursos da API OpenAI são acessados por meio da plataforma da Azure tal qual qualquer outro produto da cloud da Microsoft, sendo que antes de sua operacionalização para serviços e tarefas, um recurso da Azure OpenAI precisa ser instanciado por meio do deploy de um modelo (esta tarefa inclui tanto a escolha do modelo de IA propriamente dito, quanto da configuração dos parâmetros para o serviço).

Note que, segundo a documentação da Microsoft, o serviço da API OpenAI é baseado em prompt tanto em termos da definição da interatividade do usuário, quanto da resposta/relacionamento por parte da IA do serviço em processo:

> "While these models are powerful, their behavior is also sensitive to the prompt. This makes prompt engineering an important skill to develop."
> [What is Azure OpenAI Service - at learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)


### Conceitos Gerais da Azure OpenAI

Em termos gerais, o trabalho com modelos de linguagens pré-treinadas de IA demanda pode demandar o uso de três técnicas cocorrentes:
1. Engenharia de Prompt
2. RAG (Retrieval Augmented Generation)
3. Fine-tunning

A definição da documentação para Engenharia de Prompt é;

> "Prompt engineering is a technique that is both art and science, which involves designing prompts for generative AI models. This process utilizes in-context learning (zero shot and few shot) and, with iteration, improves accuracy and relevancy in responses, optimizing the performance of the model."
> [What is Azure OpenAI Service - at learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)

Já como definição para RAG (Retrieval Augmented Generation) a documentação segue no sentido de dizer que se trata de um método de integração de dados externos no contexto de um modelo de Large Language Model.

Veja que também esse processo de RAG é feito pelo terminal e traria vantagens consideráveis ao se permitir adaptar o trabalho direto com dados não estruturados pelo processo, podendo ir até o limite de estender as próprias definições do modelo de linguagem sendo utilizado, como, por exemplo, quando ele se torna desatualizado em termos dos dados com os quais ele fora previamente treinado:

> "RAG is also advantageous when answering questions based on an organization’s private data or when the public data that the model was trained on might have become outdated."
> [What is Azure OpenAI Service - at learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)

Finalmente, Fine-tunning seria definido como o processo iterativo para adaptar uma Large Language Model em tarefas específicas de trabalho, dessa forma, melhorando a sua performance, reduzindo latência e provendo novas capacidades de usabilidade para a linguagem:

> "This approach is used when the model needs to learn and generalize over specific topics, particularly when these topics are generally small in scope."
> [What is Azure OpenAI Service - at learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)

Especificamente nas tarefas de fine-tunning, a API Azure OpenAIse utiliza de uma série de parâmetros para definir o controle para a saída dos dados do terminal para o modelo, e dessa forma permitir um ajuste adequado dele para cada tarefa específica desempenhada, em termos de randomização, diversidade e repetição das saídas de prompt:

1. Temperatura: valor default é de 1.0
2. Top_p: valor defaul é também de 1.0
3. Penalidades (Frequência e Presença)  

Primeiramente, por meio da Temperatura o engenheiro de prompt pode definir valores para a randomização dos resultados, de modo que de 0 a 1, os resultados poderiam ser ajustados em termos de uma saída mais determinística ou mais randomizada respectivamente.

Já com relação ao Top_p, o engenheiro de prompt pode configurar a randomização baseado na probabilidade acumulada dos tokens e assim favorecer ou não maior ou menor diversidade em relação ao resultado do prompt.

Por exemplo, um valor mais baixo de Top_p permite ao modelo focar nos tokens mais provávies, enquanto que valores mais altos permite ao modelo randomizar de forma mais livre a diversificação com relação ao resultado de saída.

Finalmente, por meio das Penalidades de frequência e de presença, o engenheiro de prompt tem a possibilidade de ajustar os parâmetros para inibir seja a repetição de palavras ou frases, seja a presença de palavras ou frases, respectivamente.

Assim, uma penalidade mais alta para a frequência, tente a levar o modelo a trabalhar e gerar novas tokens para palavras ou frases ou função de tokens já repetidos, enquanto que uma penalidade baixa de presença, por exemplo, vai tender a levar o modelo a gerar uma saída com um maior reuso de tokens resultando no reuso de palavras e frases já presentes no texto de saída.  


#### O que são Large Language Models (LLMs)

Os Modelos de Linguagem de Grande Escala, segundo a tradução feita pelo blog do site [blog.dsacademy.com.br](https://blog.dsacademy.com.br/o-que-sao-large-language-models-llms/), que são algoritmos para aprendizado de máquina e para deep learning capazes de entender e processar a linguagem natural.

Nesse sentido esses modelos funcionariam pela ingestão de grandes quantidades de dados para serem treinados em relação aos padrões e ao relacionamento das estruturas de um idioma, resultando na sua capacidade de realizar tarefas genéricas como:

- tradução de textos do idioma,
- análise de sentimentos,
- conversas de chatbot
- traduzir linguagem natural em códigos, etc.  

> "Os LLMs têm visto uma série de avanços significativos nos últimos anos. Por exemplo, o GPT-3 da OpenAI, lançado em 2020, tem 175 bilhões de parâmetros e ficou famoso ao gerar texto preciso a partir de entradas feitas no ChatGPT. Outras melhorias incluem avanços na compreensão de contexto de longo alcance, a capacidade de gerar respostas mais coerentes e relevantes e a capacidade de entender e responder a uma variedade maior de entradas de texto."
> [O Que São Large Language Models (LLMs)?](https://blog.dsacademy.com.br/o-que-sao-large-language-models-llms/)

Contudo, há também os cuidados necessários relacionados ao uso das LLMs, seja em termos de confiabilidade das tarefas, seja em termos de conformação em relação aos regulamentos e normas dos países e internacionais.

Primeiramente, cabe apontar o fato de que em função da forma esparça de treinamento com grandes quantidades de dados, os modelos podem ficar enviesados e "gerar informações falsas ou enganosas, pois não têm uma compreensão do mundo real", dependendo tão somente dos padrões aprendidos por meio de seu treinamento com os dados.

Em segundo lugar, o bom uso das LLMs exigem também o cuidado para evitar "refletir e perpetuar os preconceitos presentes nos dados de treinamento", de modo que possam assim se adequar plenamente às regras e boas práticas de uso de seus processos.

Finalmente, há ainda questões relacionadas aos cuidados com a manipulação de informações sensíveis, seja presentes nos dados treinados, seja em dados processados, bem como na defesa para com o seu uso para "fins mal-intencionados, como a criação de textos enganosos ou difamatórios". 

Ao final do artigo, o blog ainda explica que as LLMs poderiam ser entendidas como padrões específicos para a  modelagem de linguagem de IA que seria treinados a base de grande quantidade de dados, isto é, operando na casa de  milhões, bilhões, e até trilhões de dados, e estando por isso mesmo muitas vezes relacionados com processos de deep learning no trabalho de dados.



## Azure OpenAI API and Semantic Kernel

De acordo com a documentação da [Microsoft](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference), a API de chamada para a Azure OpenAI Service funcionaria a partir da interação de três camadas:
1. Control Plane: esta camada tem um contexto que se assemelha a todos os demais painéis de controles para serviços da Azure OpenAI, de modo que por meio dela seria possível realizar tarefas como criar recursos e instanciar modelos. 
2. Data Plane - authoring: já o contexto dessa camada da API estaria relacionado com tarefas como Fine-Tunning, File-Upload, Ingestion Jobs, Batch, etc.
3. Data Plane - inference: finalmente, nesta camada a API dispões capacidades para tarefas relacionadas com as Completions, Chat Completions, Embeddings, Speech/Whisper, Dall-e, Assistants, etc.


Assim, por meio dessas três camadas da especificação da API do Azure OpenAI todos os modelos, todos os recursos e todas as capacidades do serviço poderiam ser alcançados pelos desenvolvedores.


### Autenticação na API

Em termos de autenticação há dois métodos:
1. Autenticação pela API Key: neste caso a api-key é inserida na header da chamada.
2. Autenticação por meio do Microsoft ID: segundo a documentação este método é um pouco mais complexo e exige a formatação do ID da Microsoft para a construção do header das chamadas.


> "You can authenticate an API call using a Microsoft Entra token. Authentication tokens are included in a request as the Authorization header. The token provided must be preceded by Bearer, for example Bearer YOUR_AUTH_TOKEN."\
> [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)


### Exemplo de Interação com a API do Azure OpenAI

> [!TIP]
> Exemplo de uma URL de chamada para um recurso:
> POST https://{endpoint}/openai/deployments/{deployment-id}/completions?api-version=2024-10-21


E por meio da estrutura de um JSON é possível transmitir parâmetros para o prompt com o qual interagimos:

``` 
{
 "prompt": [
  "tell me a joke about mango"
 ],
 "max_tokens": 32,
 "temperature": 1.0,
 "n": 1
}
```

Acima podemos ver a passagem de um parámetro para o prompt, bem como parâmetros relacionados à estruturação da resposta por parte do modelo de IA.


Assim, por meio do parâmetro *max_tokes* o desenvolvedor pode especificar o número máximo de tokes gastos para um resposta, enquanto por meio da *temperature* ele define o percentual probabilístico ou determinístico das respostas, enquanto que em *n* é definido o número de _compleitions_ que o desenvolvedor espera receber na resposta.


As repostas às chamada também são recebidas por meio de JSON de forma que é possível ao desenvolvedor construir a sua saída para o usuário de acordo com a escolha dos campos recebidos pela estrutura de JSON. 


Outros parâmetros possíveis seriam:
- Top-p
- Presence/Frequence penalties, etc.


### Desenvolvimento e Linguagens

A API da Azure OpenAI possui bibliotecas especiais chamadas de Assistants (ou Assistentes) que visam para auxiliar na preparação das chamadas e na personalização dos modelos, e que podem ser usadas nas seguintes linguagens:
- Python
- Go
- Java
- JavaScript: ~~deprecated~~
- C#

Abaixo temos Um exemplo da criação de um Assistente com a linguagem Python:
```
from openai import AzureOpenAI
    
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-08-01-preview",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

assistant = client.beta.assistants.create(
  instructions="You are an AI assistant that can write code to help answer math questions",
  model="<REPLACE WITH MODEL DEPLOYMENT NAME>", # replace with model deployment name. 
  tools=[{"type": "code_interpreter"}]
)
```

### Introdução ao Semantic Kernel

A [documentação da Microsoft]() define o _Semantic Kernel_ como um kit de desenvolvimento leve e open-source destinado a facilitar a criação de _agents_ e para a integração aos modelos de IA a partir de códigos pelas linguagens *C#*, *Python* ou *Java*.

> "Microsoft and other Fortune 500 companies are already leveraging Semantic Kernel because it’s flexible, modular, and observable. Backed with security enhancing capabilities like telemetry support, and hooks and filters so you’ll feel confident you’re delivering responsible AI solutions at scale."\
> [Introduction to Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/)

![Imagem representativa do Semantic Kernel](/public/semantic-kernel-azure-openai.png)


Em termos práticos, o _semantic kernel_ funcionaria como um _middleware_ para facilitar o processo da construção de código modular e também para facilitar as tarefas de estender recursos, como, por exemplo, das especificações para o *365 Copilot**. 


Ademais, a documentação acrescenta também que por se tratar de uma funcionalidade amplamente integrada à API, o _semantic kernel_ ofereceria ao desenvolvedor uma extraordinária flexibilidade para alcançar "all of the services and plugins necessary to run both native code and AI services", além de capaz de ser usado por praticamente todos os componentes da SDK para trazer funcionalidades aos agentes criados:


> "This is extremely powerful, because it means you as a developer have a single place where you can configure, and most importantly monitor, your AI agents. Take for example, when you invoke a prompt from the kernel. When you do so, the kernel will...\
> 1. Select the best AI service to run the prompt.\
> 2. Build the prompt using the provided prompt template.\
> 3. Send the prompt to the AI service.\
> 4. Receive and parse the response.\
> 5. And finally return the response from the LLM to your application."\
> [Introduction to Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/)


A figura abaixo traz exemplos dos recursos e das capacidades que o _semantic kernel_ disponibiliza aos desenvolvedores:

![Imagem representando as capacidades de funções e de plugins do semantic kernel](/public/function-and-plugins-semantic-kernel.png) 


E abaixo temos uma lista dos serviços já disponibilizados pelo _semantic kernel_, ainda que nem todos os serviços estejam plenamente implantados em cada uma das linguagens de programação especificadas:
1. Chat Complition
2. Text Generation
3. Embedding Generation *(Experimental)*
4. Text-to-Image *(Experimental)*
5. Image-to-Text *(Experimental)*
6. Text-to-Audio *(Experimental)*
7. Audio-to-Text *(Experimental)*
8. Realtime *(Experimental)*



- Referências:
1. [What is Azure OpenAI Service - at learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)
2. [O Que São Large Language Models (LLMs)?](https://blog.dsacademy.com.br/o-que-sao-large-language-models-llms/)
3. [Azure Openai Model Parameters](https://www.restack.io/p/ai-model-answer-azure-openai-model-parameters-cat-ai)
4. [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
5. [Introduction to Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/)






