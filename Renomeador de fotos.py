import os
import re


def renomear_imagens(pasta, texto):
    # Atualiza o padrão para capturar o início do nome do arquivo
    padrao = re.compile(r'^IMG_(\d{8})_(\d{6})')
    renomeados = 0
    totalArquivos = 0

    for nomeArquivo in os.listdir(pasta):
        totalArquivos += 1
        correspondencia = padrao.match(nomeArquivo)
        if correspondencia:
            try:
                data, hora = correspondencia.groups()
                nomeAtual = nomeArquivo

                # Extrair a extensão do arquivo
                extensao = os.path.splitext(nomeArquivo)[1]
                novoNomeBase = f"{data[:4]}-{data[4:6]}-{data[6:]
                                                         } {hora[:2]}h{hora[2:4]}m{hora[4:6]}s {texto}"

                novoCaminho = os.path.join(pasta, f"{novoNomeBase}{extensao}")
                sufixo = 1

                # Adicionar sufixo numérico se o arquivo já existir
                while os.path.exists(novoCaminho):
                    novoCaminho = os.path.join(
                        pasta, f"{novoNomeBase} ({sufixo}){extensao}")
                    sufixo += 1

                caminhoAtual = os.path.join(pasta, nomeAtual)
                os.rename(caminhoAtual, novoCaminho)
                print(f"Arquivo '{nomeAtual}' renomeado para '{novoCaminho}'.")
                renomeados += 1
            except Exception as e:
                print(f"Erro ao renomear o arquivo '{nomeArquivo}': {e}")

    print(f"Total de arquivos na pasta: {totalArquivos}")
    print(f"Total de arquivos renomeados: {renomeados}")


if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta: ")
    texto = input("Digite o texto da nova nomenclatura: ")
    renomear_imagens(pasta, texto)
