import os
from decouple import config
from google import genai


client = genai.Client(api_key=config("GEMINI_API_KEY"))


def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    Não quero que o começo da resposta seja "Aqui está a descrição de venda no limite de caracteres solicitado, seguida das especificações técnicas do modelo."
    Quero apenas uma Descrição limpa e objetiva, sem caracteres especiais, emojis ou hashtags. Não quero que a resposta seja em tópicos, quero que seja em parágrafo corrido.
    '''
    message = message.format(brand, model, year)
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=message,
    )

    # No Gemini o texto vem direto em response.text
    return response.text