import os
from cryptography.fernet import Fernet

# Gerar uma chave simétrica
def gerar_chave():
    return Fernet.generate_key()

# Criptografar um arquivo com a chave
def criptografar_arquivo(chave, nome_arquivo):
    f = Fernet(chave)
    with open(nome_arquivo, 'rb') as arquivo:
        dados = arquivo.read()
    dados_criptografados = f.encrypt(dados)
    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(dados_criptografados)

# Descriptografar um arquivo com a chave
def descriptografar_arquivo(chave, nome_arquivo):
    f = Fernet(chave)
    with open(nome_arquivo, 'rb') as arquivo:
        dados_criptografados = arquivo.read()
    dados_descriptografados = f.decrypt(dados_criptografados)
    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(dados_descriptografados)

# Diretório onde estão os arquivos a serem criptografados
diretorio = "/caminho/para/sua/pasta"

# Gerar uma chave
chave = gerar_chave()

# Criptografar todos os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    if os.path.isfile(os.path.join(diretorio, nome_arquivo)):
        criptografar_arquivo(chave, os.path.join(diretorio, nome_arquivo))

# Descriptografar todos os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    if os.path.isfile(os.path.join(diretorio, nome_arquivo)):
        descriptografar_arquivo(chave, os.path.join(diretorio, nome_arquivo))
