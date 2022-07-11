import requests
from bs4 import BeautifulSoup
from datetime import datetime

def gerar_pessoa():
    """
    Retorna um dicionário com os dados falsos de uma pessoa.
    """
    try:
        url = "https://www.invertexto.com/gerador-de-pessoas/?country=BR"
        response = requests.get(url, timeout=2)
        html = BeautifulSoup(response.text, "html.parser")

        nome = html.select_one("section:nth-child(1) h2+ .form-group .form-control")
        nome = str(nome).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        cpf = html.select_one("section:nth-child(1) .form-group:nth-child(3) .form-control")
        cpf = str(cpf).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        telefone = html.select_one("section:nth-child(1) .form-group~ .form-group+ .form-group .form-control")
        telefone = str(telefone).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        data_nascimento = html.select_one("section:nth-child(2) h2+ .form-group .form-control")
        data_nascimento = str(data_nascimento).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        atual = datetime.today()
        idade = str(round((atual - nascimento).days / 365.25))

        cep = html.select_one("section:nth-child(3) h2+ .form-group .form-control")
        cep = str(cep).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        endereco = html.select_one("section:nth-child(3) .form-group:nth-child(3) .form-control")
        endereco = str(endereco).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        cidade = html.select_one("section:nth-child(3) .form-group:nth-child(4) .form-control")
        cidade = str(cidade).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        estado = html.select_one("section:nth-child(3) .form-group:nth-child(5) .form-control")
        estado = str(estado).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        email = html.select_one("section:nth-child(4) h2+ .form-group .form-control")
        email = str(email).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        altura = html.select_one("section:nth-child(6) h2+ .form-group .form-control")
        altura = str(altura).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        peso = html.select_one("section:nth-child(6) .form-group:nth-child(3) .form-control")
        peso = str(peso).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        tipo_sanguineo = html.select_one("section:nth-child(6) .form-group~ .form-group+ .form-group .form-control")
        tipo_sanguineo = str(tipo_sanguineo).replace('<input class="form-control" type="text" value="', '').replace('"/>', '')

        pessoa = {
            "nome": nome,
            "cpf": cpf,
            "idade": idade,
            "data_nascimento": data_nascimento,
            "email": email,
            "telefone": telefone,
            "cep": cep,
            "endereco": endereco,
            "cidade": cidade,
            "estado": estado,
            "altura": altura,
            "peso": peso,
            "tipo_sanguineo": tipo_sanguineo
        }
    except:
        return {}
    else:
        return pessoa

if __name__ == "__main__":
    teste = gerar_pessoa()

    # Converte uma string para o tipo data usando o padrão passado no segundo argumento.
    data = datetime.strptime(teste['data_nascimento'], '%d/%m/%Y')
    print("Data Do Script: ", data)

    data_atual = datetime.today()
    print("Data Do Sistema: ", data_atual)

    idade = (data_atual - data).days / 365.25
    print("Idade Calculada: ", round(idade))

    # # Converte o tipo data para uma string com o formato de saída desejado.
    # data = data.strftime('%d/%m/%Y')

    print(f'\n{gerar_pessoa()}\n')
