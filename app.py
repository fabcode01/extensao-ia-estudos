import os
from google import genai

# Inicializa o cliente da API buscando a chave na variável de ambiente
client = genai.Client()

def gerar_plano_estudos(tema, dias=5):
    print(f"\n🧠 Gerando plano de estudos para: '{tema}' focado em {dias} dias...\n")

    prompt = (
        f"Crie um plano de estudos prático e direto para o tema: '{tema}'. "
        f"Divida o conteúdo de forma lógica para ser estudado em {dias} dias. "
        "Para cada dia, inclua: O que focar, um conceito-chave e uma sugestão de exercício prático."
    )

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )

    return response.text

if __name__ == "__main__":
    tema_usuario = input("Digite o assunto que deseja estudar: ")

    try:
        plano = gerar_plano_estudos(tema_usuario)
        print("--- SEU PLANO DE ESTUDOS ---")
        print(plano)

        with open("plano_gerado.txt", "w", encoding="utf-8") as f:
            f.write(plano)
        print("\n✅ Plano salvo com sucesso em 'plano_gerado.txt'!")

    except Exception as e:
        print(f"\n❌ Erro ao gerar o plano: {e}")