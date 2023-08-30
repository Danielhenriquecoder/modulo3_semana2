def decorador_imprimir (funcao):
    def retornar_juros(capital, taxa, tempo):
        print(f'CAPITAL: {capital} TAXA: {taxa} TEMPO: {tempo}')
        resultado = funcao(capital, taxa, tempo)
        print(f'RESULTADO: {resultado}')
    return retornar_juros


@decorador_imprimir
def juros_simples (capital, taxa, tempo):
    return capital * (taxa/100) * tempo

juros_simples (1000, 5, 6)