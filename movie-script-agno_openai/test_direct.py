#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
import json
from app import lambda_handler
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file


def test_prompt(prompt):
    # Cria um evento como se fosse recebido pelo Lambda:
    event = {"prompt": prompt}

    # Chama a função handler diretamente:
    result = lambda_handler(event, None)

    # Mostra o resultado:
    if result["statusCode"] == 200:
        movie_data = json.loads(result["body"])
        print("\n=== ROTEIRO GERADO ===")
        print(f"Título: {movie_data['name']}")
        print(f"Cenário: {movie_data['setting']}")
        print(f"Gênero: {movie_data['genre']}")
        print(f"Personagens: {', '.join(movie_data['characters'])}")
        print(f"Enredo: {movie_data['storyline']}")
        print(f"Final: {movie_data['ending']}")
    else:
        print(f"Erro: {result['body']}")


if __name__ == "__main__":
    while True:
        prompt = input("\nQual o tema do seu filme? (ou 'sair' para terminar): ")
        if prompt.lower() == "sair":
            break
        test_prompt(prompt)
