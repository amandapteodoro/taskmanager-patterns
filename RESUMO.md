# Resumo Técnico – Estudo e Aplicação de Padrões de Projeto

Este documento apresenta um estudo técnico sobre os padrões de projeto utilizados na construção da aplicação **TaskManager**, detalhando suas bases teóricas, variações, justificativas e a forma como foram aplicados na prática. O objetivo é demonstrar não apenas a compreensão conceitual dos padrões, mas também como eles solucionam problemas reais de organização, extensibilidade e desacoplamento dentro do sistema.

---

# 0. Introdução da Aplicação

O **TaskManager** é um sistema simples de gerenciamento de tarefas que permite ao usuário criar diferentes ações — como enviar e-mails, gerar relatórios ou executar backups —, armazená-las em um repositório global e executá-las de forma centralizada. Para manter o código modular e sustentável, o sistema aplica quatro padrões de projeto que trabalham em conjunto:

- **Factory Method:** Escolhe automaticamente qual tipo de tarefa deve ser criada, delegando às subclasses o processo de instanciação.
- **Strategy:** Define o comportamento específico de execução de cada tarefa, mantendo o algoritmo isolado da classe principal.
- **Observer:** Notifica automaticamente observadores sempre que uma tarefa é executada, registrando logs e permitindo reações independentes.
- **Singleton:** Mantém uma única instância global responsável por armazenar todas as tarefas criadas.

O fluxo geral do TaskManager segue uma cadeia lógica clara:

1. O usuário escolhe o tipo de tarefa.  
2. O **Factory Method** aciona o *creator* correto, que retorna a classe concreta da tarefa.  
3. A tarefa criada recebe internamente sua **Strategy** de execução.  
4. A tarefa é registrada na estrutura única controlada pelo **Singleton**.  
5. Ao ser executada, a estratégia define o comportamento da tarefa.  
6. Após a execução, a tarefa dispara notificações via **Observer**, permitindo o registro automático de logs.

Essa combinação garante organização, baixo acoplamento, facilidade de extensão e permite adicionar novos tipos de tarefas ou comportamentos sem alterar o código existente.

---

# 1. Estudo Teórico dos Padrões de Projeto

Os padrões utilizados pertencem às categorias **criacionais** e **comportamentais**, conforme documentado pelo Refactoring.Guru — que serviu de base conceitual para o desenvolvimento deste trabalho.

Padrões estudados e aplicados:

- **Factory Method** (Criacional)  
- **Strategy** (Comportamental)  
- **Observer** (Comportamental)  
- **Singleton** (Criacional)  

---

# 2. Descrição dos Padrões Estudados

## 2.1 Factory Method

**Propósito:**  
Fornecer uma interface abstrata para criar objetos, permitindo que subclasses decidam qual classe concreta deve ser instanciada.

**Estrutura:**  
- Um *Creator* abstrato que define o método de fábrica.  
- Subclasses concretas que sobrescrevem o factory method para retornar produtos específicos.  

**Uso ideal:**  
- Quando o sistema não deve depender de classes concretas.  
- Quando a criação de novos produtos precisa ser estendida sem modificar o código principal.  
- Quando se deseja eliminar blocos extensos de condicionais para instanciar objetos.

---

## 2.2 Strategy

**Propósito:**  
Encapsular algoritmos intercambiáveis e permitir que o objeto principal delegue comportamentos específicos a classes separadas.

**Estrutura:**  
- Uma interface base para a estratégia.  
- Implementações concretas que encapsulam diferentes algoritmos.  
- A classe principal delega o comportamento à estratégia definida.

**Uso ideal:**  
- Quando um objeto precisa executar diferentes lógicas dependendo do contexto.  
- Quando se deseja manter regras de negócio bem organizadas e independentes.  
- Quando condicionais repetitivas devem ser eliminadas.

---

## 2.3 Observer

**Propósito:**  
Criar uma dependência um-para-muitos entre objetos, de modo que mudanças no sujeito (Subject) gerem notificações automáticas para todos os observadores.

**Estrutura:**  
- Um objeto observado (Subject) com lista de observadores.  
- Observadores que implementam uma interface comum.  
- Notificação automática disparada após um evento relevante.

**Uso ideal:**  
- Quando múltiplas partes do sistema precisam agir após um evento.  
- Quando se deseja evitar chamadas diretas e dependências rígidas entre objetos.

---

## 2.4 Singleton

**Propósito:**  
Garantir que apenas uma instância de uma classe exista e fornecer um ponto global de acesso a ela.

**Estrutura:**  
- Construtor controlado.  
- Instância única armazenada e reutilizada.  

**Uso ideal:**  
- Quando existe um recurso central compartilhado.  
- Quando múltiplas instâncias causariam inconsistências (como listas de tarefas, caches ou configurações).

---

# 3. Iterações e Variações dos Padrões

## 3.1 Factory Method
Variações comuns:
- Fábricas abstratas para grupos de produtos.  
- Registro dinâmico de criadores.  
- Seleção baseada em metadados externos.

No TaskManager, adotou-se a versão clássica: cada criador concreto instancia um tipo específico de tarefa, garantindo clareza e fácil expansão.

---

## 3.2 Strategy
Variações:
- Estratégias encadeadas.  
- Seleção dinâmica em tempo de execução.  
- Composição de múltiplas estratégias.

Aqui, cada tarefa já recebe sua estratégia no momento da criação — simples e didático.

---

## 3.3 Observer
Variações:
- Notificação assíncrona.  
- Observadores remotos.  
- Filtragem de eventos.

A aplicação usa a versão síncrona tradicional, onde o log é impresso no console assim que a tarefa é executada.

---

## 3.4 Singleton
Variações:
- Singleton preguiçoso (lazy).  
- Singleton thread-safe.  
- Injeção de dependência com container.

No TaskManager, utiliza-se uma forma simples, adequada ao propósito acadêmico.

---


# 4. Comparação Geral Entre os Padrões

Embora atuem em áreas diferentes da arquitetura, os quatro padrões utilizados se complementam e contribuem para um sistema mais organizado e extensível.

- **Factory Method** resolve o problema de criação de objetos, permitindo que novos tipos de tarefas sejam adicionados sem alterar o fluxo principal da aplicação.  
- **Strategy** atua sobre o comportamento, garantindo que cada tarefa execute sua lógica própria de forma isolada e intercambiável.  
- **Observer** trata da reação a eventos, permitindo que o sistema acompanhe execuções sem acoplar tarefas a rotinas de monitoramento.  
- **Singleton** centraliza o armazenamento das tarefas, garantindo consistência e acesso global.

No conjunto, esses padrões demonstram como soluções arquiteturais diferentes podem trabalhar juntas:

- Um padrão controla **como os objetos são criados** (Factory Method).  
- Outro controla **como eles se comportam** (Strategy).  
- Outro controla **como eles se comunicam** (Observer).  
- E outro controla **como são armazenados** (Singleton).

O uso conjunto dos padrões reforça a importância de separar responsabilidades, reduzir acoplamento e promover extensibilidade, princípios essenciais de arquitetura de software.

---

# 5. Justificativas Detalhadas por Padrão

## 5.1 Factory Method

### Por que foi escolhido
Para evitar condicionais no `main.py` e permitir criar novos tipos de tarefas sem alterar o fluxo da aplicação.

### Problema resolvido
Remove dependências diretas de classes concretas e evita código rígido.

### Benefícios trazidos
- Extensibilidade  
- Centralização da lógica de criação  
- Desacoplamento do fluxo principal  

### Como seria sem o padrão
O `main.py` teria vários `if/elif` instanciando diretamente as classes `EmailTask`, `ReportTask`, etc., tornando o código inflexível.

### Uso no código
- Creator abstrato:  
  `src/tasks/creators/task_creator.py`
- Creators concretos:  
  `src/tasks/creators/email_task_creator.py`  
  `src/tasks/creators/report_task_creator.py`  
  `src/tasks/creators/backup_task_creator.py`
- Invocação no fluxo:  
  `main.py` usando `get_creator()` para decidir qual Creator instanciar.

---

## 5.2 Strategy

### Por que foi escolhido
Cada tipo de tarefa possui uma lógica de execução completamente distinta.

### Problema resolvido
Evita que a classe `Task` tenha que conhecer todos os comportamentos possíveis.

### Benefícios trazidos
- Modularidade  
- Maior legibilidade  
- Fácil adição de novos comportamentos  

### Como seria sem o padrão
A classe `Task` teria condicionais como:  
“se tipo == email: executa email…”, violando princípios de manutenção.

### Uso no código
- Interface da estratégia:  
  `src/strategy/execution_strategy.py`
- Implementações concretas:  
  `src/strategy/email_strategy.py`  
  `src/strategy/report_strategy.py`  
  `src/strategy/backup_strategy.py`
- Uso dentro das tarefas:  
  `src/tasks/task.py` delegando `self.strategy.run()`.

---

## 5.3 Observer

### Por que foi escolhido
O sistema precisa registrar logs e permitir reações automáticas após a execução de tarefas.

### Problema resolvido
Permite adicionar novas formas de resposta a eventos sem alterar o código das tarefas.

### Benefícios trazidos
- Desacoplamento entre execução e monitoramento  
- Possibilidade de múltiplos observadores  
- Centralização lógica das notificações  

### Como seria sem o padrão
Cada tarefa teria código manual de logging ou notificações, tornando difícil adicionar novas reações.

### Uso no código
- Interface do observador:  
  `src/observer/observer.py`
- Observador concreto:  
  `src/observer/logger_observer.py`
- Implementação no Subject:  
  `src/tasks/task.py` (métodos `attach()` e `notify()`)

---

## 5.4 Singleton

### Por que foi escolhido
O sistema depende de um repositório único de tarefas compartilhado do início ao fim da execução.

### Problema resolvido
Evita múltiplas listas de tarefas desconexas ou inconsistentes.

### Benefícios trazidos
- Consistência dos dados  
- Facilidade de acesso global  
- Simplicidade arquitetural  

### Como seria sem o padrão
Cada parte do sistema teria de gerenciar sua própria lista ou repassar listas manualmente.

### Uso no código
- Implementação do Singleton:  
  `src/storage/storage_singleton.py`
- Usado no fluxo principal:  
  `storage = StorageSingleton()` retorna sempre a mesma instância.

---

# 6. Conclusão

A aplicação do conjunto de padrões no TaskManager demonstra como diferentes abordagens de criação, comportamento, comunicação e armazenamento podem cooperar de forma harmônica.  
O sistema resultante é modular, de fácil manutenção e pronto para ser expandido, fornecendo uma base sólida para compreender como padrões clássicos podem ser integrados na prática para resolver problemas recorrentes.