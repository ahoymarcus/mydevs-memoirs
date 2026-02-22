# Avaliação e Métricas

> [!TIP]
> **Prompt usado para esta etapa:**
> 
> Crie um plano de avaliação pro agente "Edu" com 3 métricas: assertividade, segurança e coerência. Inclua 4 cenários de teste e um formulário simples de feedback. Preencha o template abaixo.
>
> [cole ou anexe o template `04-metricas.md` pra contexto]


## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** [ ] - Valor baseado no `transacoes.csv`
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Pergunta sobre produto
- **Pergunta:** "Investimentos em ações seria adequado para as minhas metas?"
- **Resposta esperada:** Produto incompatível com o perfil do cliente - Valor baseado nos docs (`perfil_investidor.json` & `produtos_financeiros.json`)
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Comportamento incompatível com o perfil do agente de edução de finanças - Valor baseado nas Regras e Edge Cases de configuração do agente
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente deve informar que só trata de finanças - Valor baseado nas Regras e Edge Cases de configuração do agente
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 5: Informação inexistente
- **Pergunta:** "Quanto rende o produto BBDC3 na Bovespa?"
- **Resposta esperada:** Agente precisa admitir não ter essa informação - Valor baseado nas Regras e Edge Cases de configuração do agente
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Formulário de Feedback (Sugestão)

Use com os participantes do teste:

| Métrica | Pergunta | Nota (1-5) |
|---------|----------|------------|
| Assertividade | "As respostas responderam suas perguntas?" | ___ |
| Segurança | "As informações pareceram confiáveis?" | ___ |
| Coerência | "A linguagem foi clara e fácil de entender?" | ___ |

**Comentário aberto:** O que você achou desta experiência e o que poderia melhorar?

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Liste aqui]

**O que pode melhorar:**
- [Liste aqui]

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
