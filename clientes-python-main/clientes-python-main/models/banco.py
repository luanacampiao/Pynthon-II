# Model - O que vem do banco de usuarios (BD)
def model_usuario():
    arquivo = open("clientes-python-main\\clientes-python-main\\models\\usuarios.txt","r+") #\\ pra entender que é uma barra, r+ para entender que é de leitura
    conteudo = arquivo.readlines()
    for linha in conteudo:
        usuario_senha = linha.split(";")
    usuario_BD = usuario_senha[0]
    return usuario_BD

def model_senha():
    arquivo = open("clientes-python-main\\clientes-python-main\\models\\usuarios.txt","r+")
    conteudo = arquivo.readlines()
    for linha in conteudo:
        usuario_senha = linha.split(";")
    senha_BD = usuario_senha[1]
    return senha_BD


