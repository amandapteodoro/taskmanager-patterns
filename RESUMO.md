# Resumo Técnico – Estudo e Aplicação de Padrões de Projeto

Este documento apresenta um estudo aprofundado e uma análise detalhada dos padrões de projeto utilizados no desenvolvimento da aplicação TaskManager.  
O objetivo é demonstrar domínio teórico dos padrões, suas variações, comparações e justificar tecnicamente a aplicação de cada padrão no contexto da atividade.

# 0. Introdução da Aplicação
O sistema TaskManager simula um gerenciador simples de tarefas, no qual o usuário pode criar diferentes tipos de ações (como enviar e-mails, gerar relatórios ou executar backups), armazená-las em um repositório e executá-las de forma centralizada. Para garantir uma arquitetura organizada, flexível e extensível, o sistema aplica quatro padrões de projeto complementares: o Factory Method, que decide qual classe concreta de tarefa criar conforme o tipo informado; o Strategy, que define o comportamento específico de execução de cada tarefa; o Observer, que captura e registra eventos sempre que uma tarefa é executada; e o Singleton, que garante que todas as tarefas sejam armazenadas em uma única estrutura compartilhada durante a execução do programa.

O fluxo do sistema ocorre sempre na mesma sequência lógica: o usuário escolhe um tipo de tarefa -> o Factory Method cria a instância correta -> a tarefa recebe sua estratégia de execução via Strategy -> a tarefa é armazenada em um repositório único controlado pelo Singleton -> quando executada, a lógica específica definida pela estratégia é aplicada -> após a execução, a tarefa notifica automaticamente os observadores cadastrados por meio do Observer, registrando logs e permitindo novas integrações. Essa combinação de padrões organiza o sistema em camadas independentes, reduz o acoplamento e torna fácil adicionar novos tipos de tarefas ou comportamentos sem alterar o código existente.

# 1. Estudo Teórico dos Padrões de Projeto

Os padrões implementados pertencem às categorias **criacionais** e **comportamentais**, amplamente documentados pela plataforma Refactoring.Guru, utilizada como base conceitual.

Os padrões estudados e aplicados foram:

- **Factory Method** (Criacional)  
- **Strategy** (Comportamental)  
- **Observer** (Comportamental)  
- **Singleton** (Criacional)  

# 2. Descrição dos Padrões Estudados

## 2.1 Factory Method

**Propósito:**  
Fornecer uma interface comum para criação de objetos, delegando às subclasses a decisão sobre qual classe concreta deve ser instanciada.

**Estrutura básica:**  
- Uma classe criadora define o método fábrica (factory method).  
- As subclasses sobrescrevem esse método para retornar diferentes produtos concretos.  

**Quando utilizá-lo:**  
- Quando o código não deve depender de classes concretas.  
- Quando é necessário permitir extensibilidade para criação de novos objetos.  
- Quando deseja-se evitar condicionais espalhadas pelo sistema.

## 2.2 Strategy

**Propósito:**  
Encapsular algoritmos ou comportamentos intercambiáveis dentro de classes separadas, permitindo substituição em tempo de execução.

**Estrutura básica:**  
- Uma interface de estratégia define o comportamento.  
- Múltiplas implementações concretas encapsulam algoritmos alternativos.  
- O objeto principal delega o comportamento para a estratégia escolhida.

**Quando utilizá-lo:**  
- Quando um objeto precisa executar comportamentos distintos dependendo do contexto.  
- Quando regras de negócio variam entre objetos semelhantes.  
- Quando se deseja evitar condicionais extensas e repetitivas.

## 2.3 Observer

**Propósito:**  
Criar uma relação de dependência um-para-muitos, de forma que uma mudança no objeto observado notifique automaticamente todos os observadores cadastrados.

**Estrutura básica:**  
- Um sujeito (Subject) mantém uma lista de observadores.  
- Observadores implementam uma interface comum para receber notificações.  
- Quando ocorre um evento, o sujeito dispara atualizações.

**Quando utilizá-lo:**  
- Quando diversas partes do sistema precisam reagir a eventos específicos.  
- Quando se deseja desacoplar produtor e consumidores de eventos.

## 2.4 Singleton

**Propósito:**  
Garantir que apenas uma instância de uma classe exista durante toda a execução do programa, e que haja um ponto global de acesso a ela.

**Estrutura básica:**  
- Construtor privado ou controlado.  
- Método estático que retorna sempre a mesma instância.  

**Quando utilizá-lo:**  
- Quando há recursos compartilhados (configurações, cache, armazenamento).  
- Quando duplicação de instâncias causaria inconsistência.

# 3. Iterações e Variações dos Padrões

## 3.1 Factory Method
Variações incluem:
- Fábricas abstratas para grupos de objetos relacionados.  
- Instanciação dinâmica via dicionários ou registradores.
- Fábricas parametrizadas por configuração externa.

No projeto, optou-se pela forma mais tradicional, baseada em seleção por tipo, garantindo clareza para fins didáticos.

## 3.2 Strategy
Possui variações como:
- Estratégias compostas.  
- Estratégias selecionadas dinamicamente por contexto.  
- Cadeias de estratégias (Chain of Responsibility combinada com Strategy).

No projeto, utiliza-se a variação "Strategy fixa por tipo", onde cada tarefa recebe sua estratégia ao ser criada.

## 3.3 Observer
Variações comuns:
- Notificação assíncrona.  
- Observadores remotos (event sourcing).  
- Observadores configuráveis em tempo de execução.

O projeto utiliza a forma clássica síncrona, onde cada evento aciona imediatamente os observadores registrados.

## 3.4 Singleton
Variações incluem:
- Singleton preguiçoso (lazy).  
- Singleton thread-safe.  
- Singleton com injeção de dependência (via contêiner).

Aqui, utiliza-se a versão simples, adequada a um ambiente de execução sequencial.

# 4. Comparações Entre os Padrões Utilizados

### Factory Method vs Strategy  
- Ambos promovem extensibilidade.  
- Factory cria objetos; Strategy define comportamentos.  
- Juntos, permitem criar objetos já configurados com comportamentos específicos.

### Observer vs Strategy  
- Strategy encapsula “como executar”.  
- Observer encapsula “como reagir ao que foi executado”.  
- Um complementa o outro, pois o Observer não interfere na lógica principal.

### Singleton vs os demais  
- Singleton não define comportamentos, mas garante um ponto de acesso central.  
- Trabalha como suporte arquitetural para os padrões comportamentais.

---

# 5. Justificativas Detalhadas por Padrão

## 5.1 Factory Method

### Por que o padrão foi escolhido
O projeto exige criação de diferentes tipos de tarefas sem alterar o código principal sempre que um novo tipo for adicionado.

### Qual problema ele resolve
Evita condicionais espalhadas pelo código e elimina dependências diretas de classes concretas dentro do fluxo principal.

### Benefícios trazidos
- Extensibilidade facilitada.  
- Redução de acoplamento.  
- Centralização da lógica de criação.

### Como o código seria diferente sem o padrão
O `main.py` precisaria conter vários `if/elif` instanciando diretamente as classes concretas, tornando o código rígido e difícil de manter.

---

## 5.2 Strategy

### Por que o padrão foi escolhido
Cada tipo de tarefa possui uma lógica distinta de execução.

### Qual problema ele resolve
Evita que a classe base de tarefa tenha que conhecer todos os comportamentos possíveis, prevenindo código inchado e pouco flexível.

### Benefícios trazidos
- Organização modular das regras de negócio.  
- Possibilidade de adicionar novos comportamentos sem alterar tarefas existentes.  
- Remoção completa de condicionais desnecessários.

### Como o código seria diferente sem o padrão
Haveria condicionais dentro da classe `Task` verificando o tipo da tarefa, violando o princípio aberto/fechado e resultando em baixa manutenibilidade.

---

## 5.3 Observer

### Por que o padrão foi escolhido
O sistema precisa registrar logs automáticos sempre que uma tarefa é executada.

### Qual problema ele resolve
Permite adicionar novas formas de reação a eventos sem alterar o código da tarefa.

### Benefícios trazidos
- Total desacoplamento entre execução e monitoramento.  
- Possibilidade de múltiplos observadores.  
- Aumento da rastreabilidade.

### Como o código seria diferente sem o padrão
A classe `Task` teria que chamar diretamente uma função de log, criando dependência rígida e impossibilitando múltiplas reações ao mesmo evento.

---

## 5.4 Singleton

### Por que o padrão foi escolhido
Era necessário manter uma lista única e global de tarefas acessível ao longo da execução.

### Qual problema ele resolve
Garante que o armazenamento das tarefas não seja duplicado ou perdido em diferentes instâncias da aplicação.

### Benefícios trazidos
- Consistência dos dados.  
- Facilidade de acesso ao repositório global.  
- Simplicidade da arquitetura.

### Como o código seria diferente sem o padrão
Cada parte da aplicação precisaria carregar sua própria lista de tarefas ou repassar listas via parâmetros, causando duplicação e desorganização.

---

# 6. Conclusão

O estudo e aplicação dos padrões demonstraram sua importância na construção de sistemas modulares, coesos e sustentáveis.  
O conjunto dos padrões utilizados oferece clareza arquitetural e demonstra, na prática, como soluções consagradas da Engenharia de Software resolvem problemas recorrentes de forma elegante e estruturada.

