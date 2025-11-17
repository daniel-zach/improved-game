import pickle
import os

class SistemaSaves:
    def __init__(self, file_extension, local_save):
        self.extensao = file_extension
        self.local_save = local_save

    def salvar_dados(self, dados, nome):
        with open(self.local_save + "/" + nome + self.extensao, "wb") as arquivo_dados:
            pickle.dump(dados, arquivo_dados)

    def carregar_dados(self, nome):
        try:
            with open((self.local_save + "/" + nome + self.extensao), "rb") as arquivo_dados:
                return pickle.load(arquivo_dados)
        except pickle.PickleError:
            print(f"Não foi possível carregar os dados de {nome}.")
            return
    
    def arquivo_existe(self, nome):
        return os.path.exists(self.local_save + "/" + nome + self.extensao)
    
    def deletar_arquivo(self, nome):
        if self.arquivo_existe(nome):
            os.remove(self.local_save + "/" + nome + self.extensao)
    
    def carregar_dados_jogo(self, arquivos_p_carregar, dados_padrao):
        variaveis = []
        for index, arquivo in enumerate(arquivos_p_carregar):
            if self.arquivo_existe(arquivo):
                variaveis.append(self.carregar_dados(arquivo))
            else:
                variaveis.append(dados_padrao[index])
        
        if len(variaveis) > 1:
            return tuple(variaveis)
        else:
            return variaveis[0]
        
    def salvar_dados_jogo(self, dados_p_salvar, nome_arquivo):
        for index, arquivo in enumerate(dados_p_salvar):
            self.salvar_dados(arquivo, nome_arquivo[index])