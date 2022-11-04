class Solution(object):
    def romanToInt(self, s):
        dicionario_romano = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        anterior = dicionario_romano[s[0]]
        soma = anterior
        for r in s[1:]:
            if dicionario_romano[r] > anterior:
                soma += dicionario_romano[r] - (2 * anterior)
            else:
                soma += dicionario_romano[r]
            anterior = dicionario_romano[r]
        return soma

solucao = Solution()
print(solucao.romanToInt("I"))