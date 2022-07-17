import requests as re

def cep_previsao_tempo(cep):
    cep = str(cep)
    #Função que pega as informações do CEP
    def pega_info_cep(cep):
        #Formatando o cep, caso não esteja formatado
        if (len(cep) == 8):
            cep_formatado = cep[0:5] + "-" + cep[5:]
        else:
            cep_formatado = cep

            # Verificar se o CEP corresponde ao seu tamanho
        if len(cep_formatado) != 9:
            raise ValueError("Cep inválido")

            #CEP em formato correto, acessando a APi para pegar as informações do CEP
        else:
            try:
                api_cep = f'https://viacep.com.br/ws/{cep_formatado}/json/'
                verifica_cep = re.get(api_cep)
                return verifica_cep.json()['localidade'], verifica_cep.json()['uf']

            #Caso o cep digitado não exista, irá chamar a seguinte excessão
            except Exception:
                print("O CEP digitado não é válido.")
                return -1, -1

    def pega_temperatura(cep):
        # Chave para o Weather api
        chave_Weather = '6a39e767d0b9cc466c45bcb9042899f4'

        #Informações do CEP
        cidade, UF = pega_info_cep(cep)

        #Verificando se caiu na exception do CEP
        if(cidade == -1):
           return "Não foi possível acessar as informações do CEP"

        #CEP existe, acessando as informações na API de previsão de tempo
        else:
            #link para acessar a API, já com os parâmetros do CEP
            api_weather = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{UF},br&appid={chave_Weather}'

            #acessando a API
            previsao = re.get(api_weather)

            #Pegando a temperatura
            valor_temperatura = previsao.json()['main']['temp'] - 273.15

            #FORMATANDO a temperatura
            temperatura = "{:.2f} °C".format(valor_temperatura)

            return temperatura

    return pega_temperatura(cep)

#Chamando a função que realiza a coleta
if __name__ == '__main__':
    temp = cep_previsao_tempo('95032480')

