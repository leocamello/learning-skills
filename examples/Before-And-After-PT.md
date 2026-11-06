# Da resposta pronta ao raciocínio próprio

Três demonstrações para uma apresentação numa universidade: desenvolvimento web fullstack, cibersegurança e estudo académico. O objetivo é tornar visível quem faz o trabalho intelectual.

**Os diálogos abaixo são guiões ilustrativos escritos para demonstração. Não são transcrições de testes realizados nem evidência de ganhos de aprendizagem.** As respostas reais variam com o modelo e com o participante. Não prometas uma fala exata numa demonstração ao vivo.

## Preparação: dois minutos antes de subir ao palco

1. Abre duas conversas novas no mesmo chatbot. Na primeira, usa apenas o pedido do cenário. Na segunda, cola a skill indicada e escreve: «Segue este protocolo nesta sessão. Conversa comigo em português.»
2. Mantém o mesmo problema nos dois lados. Usa os dados sintéticos deste ficheiro; não precisas de contas, serviços externos, dados de estudantes ou acesso a sistemas reais.
3. Mostra uma resposta passiva curta e, depois, a primeira pergunta da skill. Deixa um participante responder antes de continuar. Não mostres os turnos seguintes enquanto estiver a tentar.
4. Reserva três a quatro minutos por cenário. No ecrã, identifica as falas: **Estudante**, **IA sem skill**, **IA com skill**. A distinção é o comportamento observado, não a marca do chatbot.
5. Se houver falha de rede, lê o guião como uma simulação e identifica-o como tal. Se a IA revelar a resposta, assinala a falha e muda o exercício antes de avaliar a compreensão.

Pergunta de abertura para o público: **«Depois de ler uma boa explicação, como sabemos se conseguimos resolver um problema novo?»**

## Demonstração 1 — Fullstack: um JOIN que parece duplicar clientes

**Skill:** [Socratic Tutor](../skills/02-socratic-tutor/SKILL.md).  
**Resultado de aprendizagem:** explicar a multiplicidade numa relação um-para-muitos, agregar por cliente e preservar clientes sem encomendas.

### Material no ecrã

Uma aplicação mostra clientes e encomendas. A interface devia apresentar uma linha por cliente, com o número de encomendas.

`clientes`

| id | nome |
| --- | --- |
| 1 | Inês |
| 2 | Rui |

`encomendas`

| id | cliente_id | total |
| --- | --- | --- |
| 101 | 1 | 20 |
| 102 | 1 | 35 |
| 103 | 2 | 10 |

```sql
SELECT c.id, c.nome, e.id AS encomenda_id
FROM clientes AS c
JOIN encomendas AS e ON e.cliente_id = c.id;
```

**Pedido comum às duas conversas:** «Este JOIN devolve a Inês duas vezes. Como corrijo isto?»

### Antes e depois, lado a lado

| IA sem skill: resposta passiva ilustrativa | IA com skill: primeiro turno |
| --- | --- |
| «Usa GROUP BY para teres uma linha por cliente: `SELECT c.id, c.nome, COUNT(e.id) AS encomendas FROM clientes c JOIN encomendas e ON e.cliente_id = c.id GROUP BY c.id, c.nome;`. Aqui está a query corrigida.» | «Quantas linhas da tabela `encomendas` correspondem ao identificador da Inês?» |

A query da esquerda responde à necessidade de agregação para estes dados, mas não permite observar se o estudante compreendeu a cardinalidade. Na demonstração, evita sugerir que receber código é sempre errado; o problema é usá-lo como prova de aprendizagem.

### Continuação guiada — revelar um turno de cada vez

**Estudante:** «Duas.»

**IA com skill:** «Se cada correspondência formar uma linha no resultado, quantas linhas esperas para a Inês?»

**Estudante:** «Duas. Então não são linhas repetidas por engano: representam duas encomendas.»

**IA com skill:** «Essa explicação distingue as linhas pelas encomendas. Para a interface mostrar uma linha por cliente, que informação dessas encomendas precisas de resumir?»

**Estudante:** «O número de encomendas por cliente.»

**IA com skill:** «Como escreverias a consulta para obter esse resumo?»

**Estudante:**

```sql
SELECT c.id, c.nome, COUNT(e.id) AS encomendas
FROM clientes AS c
JOIN encomendas AS e ON e.cliente_id = c.id
GROUP BY c.id, c.nome;
```

**IA com skill:** «A consulta agrupa por cliente e conta as encomendas dos clientes com correspondência. Vamos testar uma condição nova: acrescentámos a Ana, sem encomendas, e ela também tem de aparecer com o valor zero. Como adaptarias a consulta?»

### Verificação independente — manter a resolução oculta durante a tentativa

<details>
<summary>Notas de avaliação para quem apresenta</summary>

Uma solução válida usa `LEFT JOIN` e conta uma coluna não nula de encomenda, como `e.id`. Para a Ana, `COUNT(e.id)` devolve zero. `COUNT(*)` contaria a linha preservada pelo `LEFT JOIN` e daria um.

```sql
SELECT c.id, c.nome, COUNT(e.id) AS encomendas
FROM clientes AS c
LEFT JOIN encomendas AS e ON e.cliente_id = c.id
GROUP BY c.id, c.nome;
```

Numa segunda pergunta, pede ao estudante que explique por que escolheu a coluna usada em `COUNT`. Só assinala «demonstrado nesta sessão» se a consulta e a justificação forem autónomas. Se precisares de explicar `LEFT JOIN`, o caso da Ana passa a prática assistida; usa outro caso de verificação depois.

</details>

**Se o estudante bloquear:** começa por pedir uma previsão sobre as linhas que a consulta atual mantém. Se isso não bastar, usa duas pequenas tabelas diferentes para mostrar a diferença entre preservar linhas e exigir correspondências. Não reveles a query da Ana como «pista».

**Frase para o palco:** «A IA deixou de ser apenas quem corrige a query. Passou a tornar visível o raciocínio de quem a escreve.»

## Demonstração 2 — Cibersegurança: entrar na conta não dá acesso a tudo

**Skill:** [Feynman Validator](../skills/03-feynman-validator/SKILL.md).  
**Resultado de aprendizagem:** explicar a diferença entre autenticação e autorização, aplicando-a à leitura de um recurso concreto. O cenário é fictício e serve para raciocinar; não é um pedido para explorar um sistema.

### Contexto no ecrã

Num portal académico fictício, cada estudante consulta a sua pauta. O servidor recebe um pedido como `GET /pautas/42`. Há uma sessão iniciada, mas ainda não sabemos que verificações o servidor faz antes de devolver os dados.

**Pedido comum às duas conversas:** «Acho que percebo segurança: se o utilizador fez login, a aplicação pode devolver a pauta pedida. Valida a minha explicação.»

| IA sem skill: resposta passiva ilustrativa | IA com skill: primeiro turno |
| --- | --- |
| «Não basta o login. Autenticação verifica a identidade e autorização verifica permissões. Deves validar o acesso à pauta no servidor. Aqui está um middleware completo…» | «O que te permite concluir que a pessoa autenticada tem permissão para consultar a pauta 42?» |

A explicação da esquerda pode estar correta, mas o estudante ainda não produziu a distinção. O tutor procura o elo lógico em falta.

### Continuação guiada

**Estudante:** «O sistema sabe quem ela é.»

**IA com skill:** «Saber quem a pessoa é permite distinguir a pauta dela da pauta de outra pessoa?»

**Estudante:** «Precisamos de saber a quem pertence a pauta e se aquela pessoa a pode consultar.»

**IA com skill:** «Como explicarias agora a diferença entre verificar a identidade e verificar essa permissão?»

**Estudante:** «A autenticação confirma a identidade. A autorização decide se essa identidade pode fazer aquela ação sobre aquela pauta.»

**IA com skill:** «Explicaste duas verificações distintas. Se um docente puder consultar pautas de várias turmas, que regra terá de justificar o acesso a uma pauta concreta?»

**Estudante:** «Não chega saber que é docente. A política tem de dizer quais as turmas a que tem acesso, e o servidor tem de verificar se aquela pauta está abrangida.»

### Verificação independente

Muda o contexto para uma biblioteca digital. Primeiro, pede uma explicação curta da diferença entre identidade e permissão, sem consultar a conversa anterior. Depois, num novo turno:

> «Uma investigadora iniciou sessão, mas o documento que pediu pertence a uma coleção restrita a outro grupo. O que deve determinar a decisão de acesso?»

<details>
<summary>Notas de avaliação para quem apresenta</summary>

Espera uma resposta que relacione a identidade autenticada, a ação de leitura, o documento ou coleção e a política aplicável. A sessão iniciada, por si só, não prova a autorização. Aceita diferentes políticas legítimas; avalia se o estudante explicita a regra em vez de inventar permissões.

Não exijas termos técnicos específicos se a explicação do mecanismo for correta. Não transformes «o docente pertence à turma» numa regra universal para todos os sistemas. Se deres a distinção durante esta verificação, marca-a como assistida e usa um novo cenário posteriormente.

</details>

**Se o estudante bloquear:** usa um caso simples de uma pessoa identificada que só tem autorização para consultar uma das duas listas fictícias. Pergunta pela diferença relevante. Evita fornecer uma implementação pronta que esconda a decisão conceptual.

**Frase para o palco:** «Dizer duas palavras certas não chega. O estudante tem de mostrar que sabe tomar uma decisão com elas.»

## Demonstração 3 — Estudo académico: apontamentos familiares não são memória utilizável

**Skill:** [Retention Engine](../skills/04-retention-engine/SKILL.md).  
**Resultado de aprendizagem:** distinguir associação de causalidade e reconhecer uma explicação alternativa num estudo observacional.

### Apontamentos sintéticos para colar

```text
Uma correlação descreve uma associação entre variáveis; isoladamente, não estabelece causalidade.
Uma variável de confundimento pode contribuir para a associação observada.
Um estudo observacional, sem uma estratégia adicional de identificação causal, não permite atribuir automaticamente a diferença observada à intervenção.
A atribuição aleatória pode reduzir diferenças sistemáticas entre grupos, mas não torna qualquer estudo imune a problemas de execução ou medição.
```

**Pedido comum às duas conversas:** «Tenho teste de metodologia. Ajuda-me a estudar estes apontamentos.»

| IA sem skill: resposta passiva ilustrativa | IA com skill: primeiro turno |
| --- | --- |
| «Aqui tens um resumo: correlação não implica causalidade, confundimento cria associações e aleatorização ajuda. Memoriza estas definições e lê estes dez cartões com as respostas.» | «Sem consultar os apontamentos, o que podes concluir se duas variáveis estiverem correlacionadas?» |

### Continuação guiada

**Estudante:** «Que variam em conjunto, mas não sei se uma causa a outra.»

**IA com skill:** «Essa resposta separa associação de causalidade. Num estudo observacional, os estudantes que foram a sessões de apoio tiveram melhores notas. Que explicação alternativa à eficácia das sessões considerarias?»

**Estudante:** «Talvez os estudantes mais motivados fossem às sessões e também estudassem mais fora delas.»

**IA com skill:** «A motivação pode contribuir para a frequência das sessões e para o estudo autónomo. Noutro estudo, os investigadores distribuem participantes aleatoriamente por dois grupos. Que problema procura essa distribuição reduzir?»

**Estudante:** «Diferenças sistemáticas entre os grupos antes da intervenção.»

**IA com skill:** «Agora analisa esta conclusão: “Todos os estudantes escolheram se queriam usar a nova aplicação; os utilizadores tiveram melhores resultados, logo a aplicação causou a melhoria.” Qual é a falha decisiva nesse raciocínio?»

**Estudante:** «Os grupos podem já diferir em motivação ou preparação. A diferença de resultados não isola o efeito da aplicação.»

### Verificação independente: três itens em turnos separados

Não apresentes os três de uma vez. Não mostres as respostas ou os cartões antes de fechar a verificação.

1. **Compreensão:** «Qual é a diferença entre observar uma associação e identificar um efeito causal?»
2. **Aplicação:** «Quem escolheu um curso opcional de escrita obteve melhores avaliações de trabalhos. Como interpretarias esse resultado sem ultrapassar a evidência disponível?»
3. **Análise de falha:** «Um relatório diz que a aleatorização garante que nenhum participante abandona o estudo. Qual é o erro desta afirmação?»

<details>
<summary>Notas de avaliação para quem apresenta</summary>

No primeiro item, procura a distinção entre covariação observada e atribuição do efeito à causa. No segundo, espera reconhecimento da seleção voluntária e de possíveis diferenças prévias; a eficácia do curso pode ser uma hipótese, mas não está demonstrada por essa comparação isolada. No terceiro, a atribuição aleatória não impede abandonos: perdas posteriores podem afetar a interpretação dos resultados.

É uma prova curta no âmbito trabalhado, não uma avaliação completa de metodologia científica. Usa um novo item se houver pistas, consulta dos apontamentos ou uma correção durante o teste. Regista separadamente o que foi e o que não foi demonstrado.

</details>

### Cartões exportados depois de encerrar o teste

As chaves `Front` e `Back` mantêm-se para facilitar a portabilidade; o conteúdo acompanha a língua do estudante. Numa sessão real, seleciona cartões de acordo com as lacunas observadas. Estes são exemplos do formato, não o resultado medido de uma sessão.

| Front | Back |
| --- | --- |
| O que descreve uma correlação entre duas variáveis? | Uma associação entre os seus valores. |
| Que conclusão não é justificada apenas por uma correlação? | Que uma das variáveis causa a outra. |
| Como pode a motivação confundir a relação entre sessões de apoio e notas? | Pode influenciar tanto a participação nas sessões como o desempenho. |
| O que procura reduzir a atribuição aleatória a grupos? | Diferenças sistemáticas entre grupos antes da intervenção. |
| Que problema posterior à atribuição pode afetar um estudo mesmo com grupos aleatorizados? | O abandono de participantes durante o estudo. |

**Plano de revisão a propor:** voltar a tentar recordar no dia seguinte, passados alguns dias e aproximadamente uma semana depois, ajustando os intervalos ao desempenho. Explica que se trata de um ponto de partida; nenhuma notificação foi agendada.

**Frase para o palco:** «A leitura dizia-me que isto era familiar. A pergunta mostrou-me o que conseguia realmente recuperar e aplicar.»

## Demonstrações rápidas das outras três skills

| Skill | Pedido para a demonstração | Primeira ação esperada |
| --- | --- | --- |
| [Curriculum Architect](../skills/01-curriculum-architect/SKILL.md) | «Quero aprender a construir um site para a associação em quatro semanas.» | Pedir um resultado concreto ou a restrição mais importante que falta, antes de produzir o plano. |
| [Mental Model Bridge](../skills/05-mental-model-bridge/SKILL.md) | «Conheço cozinha e quero perceber filas num servidor.» | Verificar o mecanismo conhecido; construir a relação e explicar onde a analogia falha antes da aplicação. |
| [Devil’s Advocate](../skills/06-devils-advocate/SKILL.md) | «Todas as aulas expositivas deviam passar a vídeos. Desafia a minha tese.» | Formular uma objeção forte e pedir uma defesa ou revisão, sem escrever o ensaio. |

Se houver apenas cinco minutos, apresenta um cenário completo em vez de seis arranques sem tentativa do estudante.

## Encerrar a apresentação

Pede ao público que escolha um conceito e experimente uma sessão curta: uma tentativa, uma correção específica e um problema novo sem ajuda. O critério de sucesso é o desempenho observável, não a quantidade de texto produzida pela IA.

Convida a partilhar um exemplo anonimizado no repositório, identificando se é uma simulação ou uma interação real, o modelo utilizado e qualquer falha. O próximo passo é simples: [escolher uma skill e começar](../README.pt.md#começa-em-30-segundos-qualquer-chatbot).
