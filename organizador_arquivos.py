import os
import shutil

# Caminho da pasta que você quer organizar
pasta_origem = "arquivos"

# Criar pasta se não existir
if not os.path.exists(pasta_origem):
    os.makedirs(pasta_origem)
    print(f"Pasta '{pasta_origem}' criada. Coloque arquivos nela e rode novamente.")
    exit()

# Tipos de arquivos
tipos = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Planilhas": [".xlsx", ".csv"],
    "Outros": []
}

# Criar pastas de destino
for pasta in tipos.keys():
    caminho = os.path.join(pasta_origem, pasta)
    if not os.path.exists(caminho):
        os.makedirs(caminho)

# Organizar arquivos
for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)

    if os.path.isfile(caminho_arquivo):
        movido = False

        for pasta, extensoes in tipos.items():
            if any(arquivo.lower().endswith(ext) for ext in extensoes):
                destino = os.path.join(pasta_origem, pasta, arquivo)
                shutil.move(caminho_arquivo, destino)
                print(f"Movido: {arquivo} ? {pasta}")
                movido = True
                break

        if not movido:
            destino = os.path.join(pasta_origem, "Outros", arquivo)
            shutil.move(caminho_arquivo, destino)
            print(f"Movido: {arquivo} ? Outros")

print("\n? Organização concluída!")