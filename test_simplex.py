import unittest
from simplex import Simplex


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Simplex()
        funcao_objetivo = [-2, -1, 1]
        restricoes = [["<=", 1, 1, 2, 6], ["<=", 1, 4, -1, 4], [0, ">=", ">=", ">="]]
        #Passo 0
        s.forma_padrao(funcao_objetivo, restricoes)
        print("Solução Básica Inicial")
        print(s.solve)
        while not (s.is_otima()):
            variavelEntra = s.quem_entra()
            print("Variável que entra")
            print(variavelEntra)
            variavelSai = s.quem_sai(variavelEntra)
            print("Variável que sai")
            print(variavelSai)
            s.new_solution(sai=variavelSai, entra=variavelEntra)
            print("Novo Tableau")
            print(s.tableau)

        self.assertEqual((-1)*s.tableau[s.quantRest][s.quantVar-1], -26/3)


if __name__ == '__main__':
    unittest.main()
