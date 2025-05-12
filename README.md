# 🐍 lambda-integration-python

Projeto desenvolvido em **Python** utilizando a biblioteca **`requests`**, com deploy local via **LocalStack**.

<p align="center">
  <img src="https://imgur.com/FcHql8j.png" width="150" alt="Python logo" />
  <img src="https://imgur.com/y0KMzg9.png" width="100" alt="Requests logo" />
  <img src="https://imgur.com/oOxoq5E.png" width="150" alt="AWS logo" />
</p>

---

## 📦 Pré-requisitos

### ✅ Instalar o utilitário `zip`

É necessário o utilitário `zip` para compactar os arquivos da Lambda.

1. Baixe o `zip.exe`:

   👉 [https://sourceforge.net/projects/gnuwin32/](https://sourceforge.net/projects/gnuwin32/)

2. Adicione o executável ao `PATH` do sistema  
   Exemplo de caminho: C:\Program Files (x86)\GnuWin32\bin

### 🐳 Rodar o LocalStack com Docker

Este projeto usa o **LocalStack** para simular os serviços da AWS localmente.  
Há um arquivo `docker-compose.yml` localizado na pasta `docker/` para facilitar a inicialização.

1. Acesse a pasta `docker`:

```bash
cd docker
```

2. Suba o container:

```bash
docker-compose up -d
```

💡 O LocalStack precisa estar rodando para que o script deploy.sh funcione corretamente.

---

## 🚀 Como usar

1. Edite o código da função Lambda em:

```bash
app/lambda_function.py
```

2. Atualize as dependências em:

```bash
app/requirements.txt
```

3. Execute o script de deploy na raiz do projeto:

```bash
./deploy.sh
```

4. Com o LocalStack rodando (via Docker), acesse o painel e teste sua Lambda:

```bash
👉 https://app.localstack.cloud/inst/default/resources/lambda/functions/my-function/invoke
```
