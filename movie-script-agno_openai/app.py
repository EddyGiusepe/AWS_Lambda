#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Script: app.py
==============
* Ao modificar este script sempre execute --> sam build --use-container
  Fazemos isso para que o Lambda possa usar o container do Agno.
* Executamos nosso script localmente, com o seguinte comando:
  
  sam local invoke MovieScriptFunction -e events/event.json
  
"""
import json
import os
from typing import List, Dict, Any
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.openai import OpenAIChat


class MovieScript(BaseModel):
    setting: str = Field(..., description="Fornece um bom cenário para um filme de sucesso.")
    ending: str = Field(..., description="Final do filme. Se não estiver disponível, forneça um final feliz.")
    genre: str = Field(..., description="Gênero do filme. Se não estiver disponível, selecione ação, thriller ou comédia romântica.")
    name: str = Field(..., description="Dê um nome a este filme")
    characters: List[str] = Field(..., description="Nome dos personagens para este filme.")
    storyline: str = Field(..., description="3 sentenças de história para o filme. Faça-o emocionante!")


def lambda_handler(event, context):
    # Verificar se a chave API está configurada
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "OPENAI_API_KEY não configurada no ambiente"
            })
        }
    
    # Obter o prompt do evento:
    body = {}
    if event.get("body"):
        try:
            body = json.loads(event["body"])
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Body inválido. Esperado JSON válido."})
            }
    
    prompt = body.get("prompt", "")
    if not prompt:
        prompt = event.get("prompt", "Um filme sobre a maravilha Machu Picchu do Perú!")
    
    try:
        # Criar o agente para geração de roteiros:
        structured_output_agent = Agent(
            model=OpenAIChat(id="o3-mini", api_key=api_key),
            description="""Você escreve roteiros de filmes.
                           Você sempre responde em português do Brasil (pt-br).
                        """,
            response_model=MovieScript,
        )
        
        # Gerar o roteiro:
        structured_output = structured_output_agent.run(prompt)
        movie_script = structured_output.content
        
        # Formatar resposta:
        result = {
            "name": movie_script.name,
            "setting": movie_script.setting,
            "ending": movie_script.ending,
            "genre": movie_script.genre,
            "characters": movie_script.characters,
            "storyline": movie_script.storyline
        }
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(result)
        }
        
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
