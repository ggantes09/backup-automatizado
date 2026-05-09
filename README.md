# Backup Automatizado

Script Python para backup automatizado de pastas, com geração de logs e controle de arquivos antigos.

## O que faz

- Compacta a pasta de origem em `.zip` com data e hora no nome
- Salva o backup na pasta de destino configurada
- Registra cada execução em um arquivo de log
- Remove automaticamente backups antigos conforme o limite configurado

## Como usar

1. Clone o repositório
2. Edite o `config.py` com os caminhos da sua máquina
3. Execute o script:
python backup.py

## Automação

Para rodar automaticamente, configure o Agendador de Tarefas do Windows apontando para o `backup.py`.

## Tecnologias

- Python
- shutil
- os
- datetime