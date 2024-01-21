# Modelo3DBuilderFramework

Este é um framework básico em Django para a construção de modelos 3D com um padrão de projeto Builder. O framework segue uma arquitetura MVC (Model-View-Controller) simples, com um foco especial na construção de orteses 3D.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `modelo3dbuilder/`: Contém os módulos principais do framework.
  - `controllers/`: Controladores responsáveis pela lógica de apresentação.
  - `services/`: Serviços e interfaces relacionados à construção de modelos 3D.
  - `repositories/`: Módulos para interação com o banco de dados.
  - `models.py`: Definição dos modelos de dados.
  - Outros arquivos padrões do Django (views, migrations, etc.).

- `Modelo3DBuilderFramework/`: Configuração do projeto Django.
- `venv/`: Ambiente virtual Python (ignorado pelo Git).
- `.gitignore`: Arquivo para especificar quais arquivos/diretórios devem ser ignorados pelo Git.
- `manage.py`: Script de gerenciamento do Django.
