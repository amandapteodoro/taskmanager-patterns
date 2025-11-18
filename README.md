# TaskManager – Implementação de Padrões de Projeto

## 1. Descrição do Projeto

O TaskManager é uma aplicação simples em Python desenvolvida para demonstrar, de forma prática, a utilização de quatro padrões de projeto amplamente estudados: **Factory Method**, **Strategy**, **Observer** e **Singleton**.

A aplicação permite criar diferentes tipos de tarefas, armazená-las em um repositório único e executar cada tarefa conforme sua lógica específica. Durante a execução, eventos são registrados por um observador de logs.

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

## 3. Padrões de Projeto Implementados e Onde Encontrá-los

A seguir estão os quatro padrões implementados e a localização de suas classes no código.

### 3.1 Factory Method
**Responsável pela criação das tarefas conforme o tipo informado pelo usuário.**

- `src/tasks/task_factory.py`  
- Classes concretas das tarefas:  
  - `src/tasks/email_task.py`  
  - `src/tasks/report_task.py`  
  - `src/tasks/backup_task.py`

### 3.2 Strategy
**Define o comportamento de execução específico de cada tipo de tarefa.**

- Interface base:  
  - `src/strategy/execution_strategy.py`
- Estratégias concretas:  
  - `src/strategy/email_strategy.py`  
  - `src/strategy/report_strategy.py`  
  - `src/strategy/backup_strategy.py`
- Uso dentro das tarefas:  
  - `src/tasks/*.py`


### 3.3 Observer
**Permite registrar automaticamente um log sempre que uma tarefa é executada.**

- Interface: `src/observer/observer.py`  
- Observador concreto: `src/observer/logger_observer.py`  
- Notificação integrada à classe base de tarefa:  
  - `src/tasks/task.py`

### 3.4 Singleton
**Garante que todas as tarefas criadas sejam armazenadas em uma única instância global.**

- Implementação: `src/storage/storage_singleton.py`

## 4. Objetivo Educacional

Este projeto foi desenvolvido exclusivamente para fins acadêmicos, atendendo aos requisitos da atividade da disciplina **Padrões e Arquitetura de Software**, com foco em demonstrar o uso correto, organizado e contextualizado de cada padrão estudado.





