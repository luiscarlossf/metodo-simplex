#File name: simplex.py
#Author: Luis Carlos <luiscarlos.sf@outlook.com>
 #import numpy as np
import sys
"""
    O método Simplex compreende os seguintes passos:
    0 - Colocar o PPL na forma padrão
    1 - Achar uma solução viável básica inicial
    2 - Verificar se a solução atual é ótima, se for PARE
        Caso contrário, vá para o passo 3
    3 - Determinar a variável não básica que deve entrar na base
    4 - Determinar a variável básica que deve sair da base
    5 - Achar a nova solução viável básica e voltar ao passo 2

"""
class Simplex():

    def __init__(self):
        self.tableau = list()
        self.quantVar = 0
        self.quantRest = 0
        self.tipo = 0
        self.solve = list()

    """
        funcao_objetivo : [x1, x2, x3, ...]
        restricoes : [["<= ou >= ou = ",x1, x2, x3, ..., b1],["<= ou >= ou = ", x1, x2, x3, ..., b2], ..., [0, ">=", ">=",">=", ...]]
    """
    def forma_padrao(self,funcao_objetivo, restricoes):

        m = len(restricoes)
        contVarAdd=0
        for i in range(len(funcao_objetivo)):
            #Variável sem restrição de sinal
            if restricoes[m-1][i+1] == "free":
                funcao_objetivo[i]=(1* funcao_objetivo[i], -1* funcao_objetivo[i])
                for j in range(m):
                    restricoes[j][i+1]=(1* restricoes[j][i+1], -1* restricoes[j][i+1])
                restricoes[j][i + 1] = (">=",">=")
            #Variável com restrição negativa
            elif restricoes[m-1][i+1] == "<=":
                funcao_objetivo[i] = -1 * funcao_objetivo[i]
                for j in range(m):
                    restricoes[i][j]= -1 * funcao_objetivo[i]

        for i in range(m-1):
            n = len(restricoes[i])-2
            #Menor ou igual
            if restricoes[i][0] == "<=":
                restricoes[i][0] = "=";
                restricoes[i].insert(n+1, 1)
                for k in range(m-1):
                    if k != i:
                        restricoes[k].insert(n+1, 0)
                self.solve.append(n+1)
            #Maior ou igual
            elif restricoes[i][0] == ">=":
                restricoes[i][0] = "=";
                restricoes[i].insert(n+1, 1)
                for k in range(m-1):
                    if k != i:
                        restricoes[k].insert(n+1, 0)
            #Lado Direito negativo
            print(restricoes[i][len(restricoes[i])-1])
            if restricoes[i][len(restricoes[i])-1] < 0:
                for j in range(1,len(restricoes[i])):
                    #CORRIGE ERRO PARA TUPLAR
                    restricoes[i][j] *= -1;

        self.quantVar = len(restricoes[1][1:])
        self.quantRest = len(restricoes) - 1
        self.tableau_inicial(funcao_objetivo, restricoes)

    def tableau_inicial(self, funcao_objetivo, restricoes):

        for i in range(self.quantRest):
            self.tableau.append(restricoes[i][1:])
        self.tableau.append(funcao_objetivo)
        aux = len(self.tableau)-1
        for i in range( len(funcao_objetivo), len(self.tableau[0])):
            self.tableau[aux].append(0)

    def solution(self):

        for i in range(self.quantRest):
            if self.tableau[self.quantRest][i] == 0:
                self.solve[i]=0
        return self.solve

    def quem_entra(self):
        variavelEntra = min(self.tableau[self.quantRest])
        print(self.tableau[self.quantRest].index(variavelEntra))
        return self.tableau[self.quantRest].index(variavelEntra)

    def quem_sai(self, variavel_entra):
        razao=list()
        for i in range(self.quantRest):
            if self.tableau[i][variavel_entra] != 0:
                aux = self.tableau[i][self.quantVar-1]/self.tableau[i][variavel_entra]
                if aux>=0:
                    razao.append(aux)
                else:
                    razao.append(sys.maxsize)
            else:
                razao.append(sys.maxsize)
        print(razao)
        return razao.index(min(razao))
    def is_otima(self):

        for custo in self.tableau[self.quantRest]:
            if custo< 0:
                return False
        return True

    def new_solution(self, sai, entra):
        for i in range(self.quantVar):
                self.tableau[sai][i] = self.tableau[sai][i]/self.tableau[sai][entra]

        for i in range(self.quantRest+1):
            for j in range(self.quantVar):
                self.tableau[i][j] = self.tableau[i][j]




if __name__=="__main__":

    funcao_objetivo = [-2,-1,1]
    restricoes = [["<=",1,1,2,6], ["<=",1,4,-1, 4], [0, ">=", ">=", ">="]]

    t = Simplex()
    t.forma_padrao(funcao_objetivo, restricoes)
    print("Tableu Inicial")
    print(t.tableau)

    print("Solução Inicial")
    print(t.solve)

    print("Z")
    print(t.tableau[t.quantRest][t.quantVar-1])

    print("Entra")
    entra = t.quem_entra()
    print("Sai")
    print(t.quem_sai(entra))
    #Exibindo o PPL na forma padrão
    funcao= "MIN Z = "
    for i in range(len(funcao_objetivo)):
        if i+1 == len(funcao_objetivo):
            funcao += str(funcao_objetivo[i]) + 'X' + str(i + 1)
        else:
            funcao += str(funcao_objetivo[i])+'X'+ str(i+1)+" + "
    print(funcao)
    print("Restrições: ")
    for i in range(len(restricoes)-1):
        string = ""
        for j in range(1,len(restricoes[i])):
                if j + 1 == len(restricoes[i]):
                    string += str(restricoes[i][j])
                elif j + 2 == len(restricoes[i]):
                    string += str(restricoes[i][j]) + 'X' + str(j)+ " ="
                else:
                    string += str(restricoes[i][j])+'X'+ str(j)+ "  +"
        print(string)


