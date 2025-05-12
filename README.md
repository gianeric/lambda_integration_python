# lambda-integration-python

Project developed in python using requests

#

<p align="center">
<img src="https://imgur.com/FcHql8j.png" width="150" title="Python">
<img src="https://imgur.com/y0KMzg9.png" width="100" title="Requests">
<img src="https://imgur.com/oOxoq5E.png" width="150" title="AWS">
</p>

# PRÉ REQUISITOS:

## ZIP

### Baixar o utilitário zip para compactar pastas

https://sourceforge.net/projects/gnuwin32/

### Adicione o executável extraído ao PATH do sistema ou use o caminho absoluto no script:

C:\Program Files (x86)\GnuWin32\bin\zip.exe

# MODO DE USAR:

1 - Codificar app/lambda_funcion.py
2 - Atualizar app/requirements.txt com as dependencias atuais do projeto incluindo as versões
3 - Rodar o deploy.sh na raiz do projeto para subir a lambda no localstack
./deploy.sh
4 - Abrir o localstack (docker) e testar a lambda no link:
https://app.localstack.cloud/inst/default/resources/lambda/functions/my-function/invoke

# Compactar o arquivo lambda_function.py para funcion.zip dentro da pasta app, ficando app/function.zip

# comando abaixo no git bash para subir a lambda ao localstack

awslocal lambda create-function \
 --function-name my-function \
 --runtime python3.9 \
 --handler lambda_function.handler \
 --role arn:aws:iam::000000000000:role/lambda-role \
 --zip-file fileb://app/function.zip

# ou

# comando abaixo no git bash para ATUALIZAR a lambda no localstack

awslocal lambda update-function-code \
 --function-name my-function \
 --zip-file fileb://app/package/function.zip

# Verificar o estado da função lambda

awslocal lambda get-function --function-name my-function

# Testar função lambda

awslocal lambda invoke \
 --function-name my-function \
 --payload '{}' \
 outputfile.txt
