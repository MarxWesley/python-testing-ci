# 🧪 Projeto de Testes Unitários em Python com Pytest + CI/CD

Este projeto é um exemplo de aplicação Python com:

* Testes unitários usando **pytest**
* Relatório de cobertura com **pytest-cov**
* Pipeline CI/CD com **GitHub Actions**
* Estrutura organizada em `app/` e `tests/`

---

## 📁 Estrutura do Projeto

```
.
├── app/
│   ├── __init__.py
│   ├── calculadora.py
│   ├── calcular_idade.py
│   └── functions.py
├── tests/
│   ├── test_calculadora.py
│   ├── test_calcular.py
│   └── test_functions.py
├── .gitignore
├── pytest.ini
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── pipeline.yml
```

---

## 🚀 Funcionalidades

* Cálculo de idade baseado no ano de nascimento
* Contagem de caracteres de uma string
* Testes automatizados
* Geração de relatório de cobertura de código
* Integração contínua (CI) com GitHub Actions

---

## 🐍 Requisitos

* Python 3.11 ou superior
* pip instalado

---

## 📦 Instalação do Projeto

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

Crie um ambiente virtual (recomendado):

```bash
python -m venv venv
```

Ative o ambiente virtual:

### Windows:

```bash
venv\Scripts\activate
```

### Linux/Mac:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🧪 Como rodar os testes

Para executar os testes unitários:

```bash
pytest
```

Rodar testes com cobertura de código:

```bash
pytest --cov=app --cov-report=xml --cov-report=html
```

---

## 📊 Relatório de Cobertura

Após rodar os testes com cobertura, serão gerados:

* `coverage.xml` → usado em pipelines CI/CD
* Pasta `htmlcov/` → relatório visual em HTML

Para visualizar o relatório no navegador:

```bash
htmlcov/index.html
```

Ou abra manualmente o arquivo:

```
htmlcov/index.html
```

---

## ⚙️ CI/CD (GitHub Actions)

O projeto possui uma pipeline configurada que:

1. Faz checkout do código
2. Configura o Python 3.11
3. Instala as dependências
4. Executa os testes com pytest
5. Gera relatório de cobertura
6. Publica o artefato de cobertura

A pipeline é executada automaticamente quando:

* Há push nas branches `main` ou `qa`
* Um Pull Request é aberto para `main`

---

## 🔒 Qualidade do Código

A pipeline falhará automaticamente se:

* Algum teste unitário falhar
* Houver erro na execução do pytest
* Dependências não forem instaladas corretamente

Isso garante que apenas código estável seja integrado via merge.

---

## 📌 Dependências do Projeto

Arquivo `requirements.txt`:

```txt
pytest
pytest-cov
```

Instalação rápida:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Autor

Projeto desenvolvido para estudos de:

* Testes unitários em Python
* CI/CD
* Qualidade de software (QA)
* Automação de testes