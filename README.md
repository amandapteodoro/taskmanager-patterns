# TaskManager – Implementação de Padrões de Projeto

## 1. Descrição do Projeto

O **TaskManager** é uma aplicação em Python desenvolvida com foco didático para demonstrar, de forma prática e organizada, a aplicação de quatro padrões de projeto amplamente utilizados: **Factory Method**, **Strategy**, **Observer** e **Singleton**.

O programa permite criar diferentes tipos de tarefas, armazená-las em uma única estrutura global e executá-las conforme o comportamento específico de cada tipo. Além disso, toda vez que uma tarefa é executada, um observador registra automaticamente o evento, simulando um mecanismo simples de auditoria.

---

## 2. Como Executar o Projeto

### Requisitos
- Python 3.10 ou superior

### Execução
1. Abra o terminal na pasta raiz do projeto.
2. Execute: python -m src.main
3. Utilize o menu exibido no terminal para:
- Criar tarefas  
- Executar todas as tarefas  
- Listar tarefas registradas  

---

## 3. Padrões de Projeto Implementados e onde estão localizados no programa

### 3.1 Factory Method
Responsável pela criação das tarefas conforme o tipo informado pelo usuário, evitando que o código principal conheça diretamente as classes concretas.
A implementação segue o formato clássico: um Creator abstrato define o método de fábrica, enquanto Creators concretos criam os objetos específicos.

**Localização:**
- **Creator abstrato:**
  - `src/tasks/task_factory.py`
  
- **Creators concretos:**  
  - `src/tasks/creators/email_task_creator.py`
  - `src/tasks/creators/report_task_creator.py`
  - `src/tasks/creators/backup_task_creator.py`

- **Produtos (tarefas criadas)**:
  - `src/tasks/email_task.py`
  - `src/tasks/report_task.py`
  - `src/tasks/backup_task.py`

### 3.2 Strategy
O padrão Strategy define o comportamento de execução de cada tarefa. Cada tipo de tarefa possui sua própria estratégia, permitindo alterar o algoritmo de execução sem modificar o restante da classe.

- Interface:  
  - `src/strategy/execution_strategy.py`
  
- Estratégias concretas:  
  - `src/strategy/email_strategy.py`  
  - `src/strategy/report_strategy.py`  
  - `src/strategy/backup_strategy.py`
  
- Uso dentro das tarefas:  
  - `src/tasks/*.py`
  - `src/tasks/task*.py`


### 3.3 Observer
Permite registrar automaticamente um log sempre que uma tarefa é executada, por meio de um observador de logs.

- Interface: `src/observer/observer.py`  
- Observador concreto: `src/observer/logger_observer.py`  
- Notificação integrada à classe base de tarefa:  
  - `src/tasks/task.py` (métodos attach() e notify())

### 3.4 Singleton
Garante que todas as tarefas criadas sejam armazenadas em uma única instância global.

- Implementação: `src/storage/storage_singleton.py`

---

## 4. Objetivo Geral

Este projeto foi desenvolvido exclusivamente para fins acadêmicos, atendendo aos requisitos da atividade da disciplina **Padrões e Arquitetura de Software**. O objetivo principal é demonstrar, de forma clara e contextualizada, como diferentes padrões de projeto podem ser aplicados em conjunto dentro de uma aplicação Python real, ainda que simplificada, promovendo modularidade, flexibilidade e facilidade de manutenção.





