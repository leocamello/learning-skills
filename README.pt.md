# learning-skills

**AI Agent Skills for Human Learning — Not Machine Learning**

*Skills de agentes de IA para a aprendizagem humana — não para treinar máquinas.*

**Deixa de usar a IA como muleta. Usa-a como ginásio para o pensamento.**

Reconhecer uma resposta não é saber chegar a ela. Estes seis ficheiros de instruções transformam a IA num tutor que te pede para recordar, explicar, aplicar e defender o que sabes. O raciocínio é teu. O agente propõe o próximo desafio útil.

[English](README.md) · [Demonstrações ao vivo](examples/Before-And-After-PT.md) · [Contribuir](CONTRIBUTING.md) · [Licença MIT](LICENSE)

| Com uma IA passiva | Com learning-skills |
| --- | --- |
| «Explica outra vez.» | Explicas por palavras tuas e descobres o elo em falta. |
| Copias uma solução completa. | Dás um passo no raciocínio e recebes uma pista ajustada. |
| Relês até tudo parecer familiar. | Recordas sem apontamentos e aplicas numa situação nova. |
| «O teu argumento está ótimo!» | Defendes a ideia perante um contraexemplo forte. |

## Escolhe o teu treino

| Skill | Usa quando… | O que vais fazer | Evidência de progresso |
| --- | --- | --- | --- |
| 🗺️ [Curriculum Architect](skills/01-curriculum-architect/SKILL.md) | «Quero aprender X. Por onde começo?» | Identificar pré-requisitos e construir uma sequência focada. | Concluir um pequeno projeto verificável em cada etapa. |
| 🧭 [Socratic Tutor](skills/02-socratic-tutor/SKILL.md) | «Estou bloqueado neste exercício.» | Responder a uma pergunta de cada vez, com pistas progressivas. | Resolver uma variante nova sem ajuda. |
| 🗣️ [Feynman Validator](skills/03-feynman-validator/SKILL.md) | «Acho que já percebi.» | Ensinar um principiante curioso, sem te esconderes atrás de jargão. | Explicar o mecanismo e um caso desconhecido. |
| 🧠 [Retention Engine](skills/04-retention-engine/SKILL.md) | «Testa-me sobre estes apontamentos.» | Recordar, aplicar e diagnosticar erros. | Passar uma prova de evocação variada e criar cartões atómicos. |
| 🌉 [Mental Model Bridge](skills/05-mental-model-bridge/SKILL.md) | «Preciso de perceber esta ideia nova.» | Relacioná-la com algo que dominas e identificar os limites da analogia. | Raciocinar sobre o conceito sem depender da comparação. |
| ⚔️ [Devil’s Advocate](skills/06-devils-advocate/SKILL.md) | «Põe o meu argumento ou projeto à prova.» | Defender pressupostos e corrigir afirmações frágeis. | Responder a um contraexemplo novo com evidência. |

Não sabes qual escolher? Usa o [Learner Orchestrator](agents/learner-orchestrator.md). Identifica a dificuldade imediata e ativa **uma skill de cada vez**. Podes fazer uma pausa, mudar de língua ou sair do modo de aprendizagem a qualquer momento.

## Começa em 30 segundos: qualquer chatbot

Não precisas de terminal, chave de API, integração paga ou conhecimentos de programação para colar as instruções numa conversa. Precisas de acesso a um chatbot; as opções para guardar assistentes dependem da tua conta.

1. Abre [Socratic Tutor](skills/02-socratic-tutor/SKILL.md), escolhe **Raw** e copia o texto do ficheiro.
2. Cola-o numa conversa nova no ChatGPT, Claude ou Gemini.
3. Acrescenta: **«Segue estas instruções nesta sessão de estudo. Quero perceber os JOINs em SQL. Faz a primeira pergunta em português.»**

A primeira resposta deve ter uma única pergunta de diagnóstico, sem resolver logo o problema. Se o modelo entregar a resposta, escreve: **«Volta à fase de diagnóstico da skill. Faz uma pergunta e espera.»** As instruções orientam o modelo; não constituem uma garantia técnica de cumprimento.

### Guarda o teu assistente de estudo

| Plataforma | Configuração |
| --- | --- |
| **Instruções Personalizadas do ChatGPT** | Em Definições → Personalização, adiciona a instrução curta abaixo. Cola a skill completa em cada conversa de estudo. As Instruções Personalizadas servem de entrada, não de arquivo dos seis ficheiros. [Guia oficial](https://learn.chatgpt.com/docs/personalize). |
| **GPTs personalizados do ChatGPT** | Se a tua conta permitir criar GPTs, cola o corpo de uma skill em **Instructions / Instruções**. Se exceder o limite do editor, adiciona o ficheiro completo a **Knowledge / Conhecimento** e usa a instrução de ativação abaixo. Testa numa conversa de pré-visualização. [Descrição oficial](https://developers.openai.com/api/docs/actions/introduction). |
| **Claude Projects** | Cria um projeto de estudo, adiciona a skill aos ficheiros do projeto e coloca a instrução de ativação nas instruções do projeto. Abre uma conversa nova dentro dele. [Guia oficial](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects). |
| **Gemini Gems** | No Gemini para a Web, abre Gems → New Gem. Cola o corpo de uma skill nas instruções e guarda. Se preferires anexar um ficheiro, acrescenta a instrução de ativação. A Google anuncia a migração dos Gems de contas pessoais para skills a partir de novembro de 2026; segue as opções disponíveis na tua conta ou usa o método de colar numa conversa. [Guia oficial](https://support.google.com/gemini/answer/15146780?hl=en). |

Instrução curta para as Instruções Personalizadas:

```text
Quando eu pedir explicitamente para estudar ou praticar, segue o ficheiro learning-skills que eu fornecer. Faz uma pergunta de cada vez, espera pela minha tentativa e usa pistas progressivas sem revelar a solução do exercício. Responde na minha língua. Verifica a compreensão com uma tarefa nova, sem pistas. Se a skill não estiver disponível, pede-me que a cole. Respeita os meus pedidos de pausa ou de saída.
```

Instrução de ativação para um ficheiro anexado:

```text
Nesta sessão de estudo, lê o SKILL.md do Socratic Tutor que anexei e segue o protocolo completo. Se não conseguires aceder ao ficheiro, diz-me e pede-me que o cole; não afirmes que o carregaste. Começa com uma pergunta de diagnóstico na minha língua.
```

Para teres encaminhamento automático, coloca o corpo do [orquestrador](agents/learner-orchestrator.md) nas instruções do assistente e anexa as seis skills. Dá às cópias os nomes `curriculum-architect.md`, `socratic-tutor.md`, `feynman-validator.md`, `retention-engine.md`, `mental-model-bridge.md` e `devils-advocate.md`, evitando seis anexos chamados `SKILL.md`. O orquestrador reconhece estes nomes. A recuperação dos ficheiros não é garantida: verifica a primeira resposta e cola a skill escolhida se necessário.

## Começa em 30 segundos: terminal e IDE

**O caminho mais rápido:** descarrega o repositório em **Code → Download ZIP**, extrai-o e abre-o no editor. Na conversa com o agente, anexa `skills/02-socratic-tutor/SKILL.md` e escreve:

```text
Lê este SKILL.md e usa socratic-tutor para me ajudar a compreender um JOIN que está a falhar. Faz uma pergunta e espera pela minha resposta. Não alteres ficheiros nem executes a solução por mim.
```

Este método também funciona se o cliente não reconhecer skills automaticamente.

Para descoberta nativa no projeto, copia as seis pastas para o diretório de skills do teu cliente. Na raiz do repositório extraído, executa o seguinte em **Bash, Terminal do macOS, Linux, WSL ou Git Bash**. A instalação fica no projeto atual, não é global:

```bash
# Claude Code; escolhe outro destino na tabela se necessário.
destination=.claude/skills
mkdir -p "$destination"
for source in skills/[0-9][0-9]-*; do
  name="${source##*/}"
  name="${name#??-}"
  if [ -e "$destination/$name" ]; then
    printf 'Já existe; ignorado: %s\n' "$destination/$name"
  else
    cp -R "$source" "$destination/$name"
  fi
done
```

| Cliente | Valor de `destination` | Como começar |
| --- | --- | --- |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills` | `/socratic-tutor Ajuda-me a compreender JOINs em SQL` |
| [Cursor](https://cursor.com/docs/skills) | `.cursor/skills` | Seleciona `socratic-tutor` no menu `/` ou pede explicitamente para o usar. |
| [GitHub Copilot](https://docs.github.com/en/copilot/concepts/customizations/agent-skills) | `.github/skills` | Pede ao agente do Copilot que use `socratic-tutor`; o suporte depende do cliente e da versão. |
| **Windsurf** | `.windsurf/skills` ([mapeamento mantido pelo instalador](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)) | Pede ao Cascade que use `socratic-tutor`; se a descoberta não estiver disponível, anexa o ficheiro explicitamente. |

As pastas numeradas mantêm o catálogo ordenado. Os nomes das pastas instaladas coincidem com o campo `name` do cabeçalho YAML. Incluímos o campo de projeto `cognitive_principle`; um cliente com validação estrita pode rejeitá-lo. Nesse caso, move-o para o corpo Markdown **na cópia instalada** ou usa o método de anexar o ficheiro. Não precisas de um ambiente de execução específico. Para remover uma skill copiada, apaga a respetiva pasta de instalação; a origem mantém-se.

## Experimenta uma sessão útil

```text
Usa curriculum-architect. Tenho quatro semanas, três horas por semana e conhecimentos básicos de HTML. Quero construir um pequeno site acessível. Avalia o meu ponto de partida antes de fazeres o plano.
```

```text
Usa feynman-validator. Vou explicar a diferença entre autenticação e autorização. Questiona os termos que eu não explicar. Conversa comigo em português.
```

```text
Usa retention-engine com os apontamentos que anexei. Tenho 15 minutos. Testa a minha memória antes de mostrares respostas e, no final, exporta cartões Frente/Verso para as lacunas encontradas.
```

```text
Usa devils-advocate. A minha tese é que todas as aulas universitárias expositivas deviam ser substituídas por vídeos gravados. Ajuda-me a testar os pressupostos sem escreveres o trabalho por mim.
```

Uma sessão típica segue **tentativa → feedback específico → nova tentativa → aplicação autónoma**. Planos e cartões são instrumentos, não provas de aprendizagem. «Demonstrado nesta sessão» significa ter resolvido uma tarefa nova sem ajuda; a retenção duradoura exige nova verificação noutro dia.

Os ficheiros de instruções estão em inglês para facilitar a manutenção. **Todas as skills têm de conversar na língua do estudante**, incluindo português, inglês e espanhol. Não é preciso traduzir o ficheiro. A mesma abordagem serve uma unidade curricular em Lisboa, uma disciplina em São Paulo ou um grupo de estudo em Maputo; o vocabulário adapta-se ao estudante.

## O compromisso do projeto

- **Tentativa antes da resposta:** uma pergunta ou tarefa de cada vez, sem disfarçar a solução numa pergunta sugestiva.
- **Apoio antes da frustração:** passos mais pequenos, três níveis de pistas e exemplos resolvidos de um problema diferente quando necessário. Podes fazer uma pausa ou sair.
- **Evidência antes do elogio:** explicação ou aplicação autónoma, sem confundir confiança, rapidez ou concordância com compreensão.
- **Texto portátil:** Markdown que podes inspecionar, sem servidor próprio, telemetria ou API obrigatória. O fornecedor do chatbot continua a tratar o que lhe envias.

Os protocolos recorrem à prática de evocação, à autoexplicação, ao apoio gradual e à transferência por analogia. As formulações, os limiares e os intervalos de revisão são opções de desenho, não uma intervenção validada experimental ou clinicamente. A ideia «80/20» é uma heurística de priorização, não uma lei quantitativa da aprendizagem. Consulta a [base científica e os critérios para contribuir](CONTRIBUTING.md#evidence-and-claims).

## Faz parte

Docentes: adaptem uma skill a um resultado de aprendizagem e experimentem uma sessão curta e anónima em aula. Estudantes: criem um fork para a vossa disciplina, partilhem um exemplo antes/depois anonimizado e indiquem onde a IA revelou a resposta ou vos deixou bloqueados. Para contribuir, sigam o [guia de Pull Requests e a lista de verificação pedagógica](CONTRIBUTING.md).

**Se uma skill te ajudou a resolver algo sem IA, dá uma estrela ao repositório e partilha esse momento.** Traz um exemplo reproduzível, não uma promessa de melhores notas.

Inspirado na abordagem modular e imediatamente útil de [agent-skills, de Addy Osmani](https://github.com/addyosmani/agent-skills), e de [skills, de Matt Pocock](https://github.com/mattpocock/skills). Projeto independente, sem afiliação nem aprovação implícita dos autores.

[Licença MIT](LICENSE). Podes criar um fork, adaptar, traduzir e usar nas tuas aulas.
