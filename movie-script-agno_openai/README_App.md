# <h1 align="center"><font color="red">AWS Lambda</font></h1>

<font color="pink">Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro</font>

Um dos serviços mais populares na AWS é o Lambda, que permite executar código em resposta a algum evento, sem precisar se preocupar com os servidores subjacentes.

![](https://miro.medium.com/v2/resize:fit:506/0*bs93Wo0NqHoUE8Yg.png)


# <font color="gree">Interagindo com sua API Gateway</font>

`Aplicação: Gerador de Roteiros de Filmes com AI`

Esta aplicação é um gerador automatizado de roteiros de filmes usando inteligência artificial, desenvolvido como uma função serverless na AWS Lambda.

`Funcionalidade`

* Recebe um prompt/tema do usuário (ex: `"Um filme sobre exploradores no Peru"`)
* Gera um roteiro completo e estruturado de filme em português brasileiro
* Retorna o resultado em formato JSON com todos os elementos narrativos

`Componentes do roteiro gerado`

* Nome: Título do filme
* Cenário: Ambiente/localização principal do filme
* Gênero: Categoria do filme (ação, thriller, comédia romântica, etc.)
* Personagens: Lista de personagens principais
* Enredo: Resumo da história em 3 sentenças
* Final: Como o filme termina

`Tecnologias utilizadas`

1. `AWS Lambda:` Serviço serverless que executa o código sem necessidade de gerenciar servidores
2. `AWS API Gateway:` Cria e expõe uma `API REST` para acessar a função Lambda
3. `AWS SAM:` Framework para facilitar o deploy de aplicações serverless
4. `Python:` Linguagem de programação usada para desenvolver a lógica
5. `Agno:` Framework para construir agentes de IA estruturados
6. `OpenAI:` Modelo de linguagem (`o3-mini`) para gerar o conteúdo criativo
7. `Pydantic:` Biblioteca para validação de dados e definição de esquemas estruturados

`Fluxo de execução`

1. Usuário envia um prompt via `API Gateway`
2. Lambda verifica a chave da `API OpenAI` nas variáveis de ambiente
3. Cria um `agente Agno` configurado com o modelo da `OpenAI`
4. Define o schema estruturado para o roteiro (usando `Pydantic`)
5. Executa o agente com o `prompt` recebido
6. Formata a resposta do modelo em um `JSON` bem estruturado
7. Retorna o roteiro completo ao usuário

`Implantação e gerenciamento`

* Usa `Docker containers` para garantir compatibilidade de dependências
* Configurado para build com `sam build --use-container`
* Testável localmente com `sam local invoke MovieScriptFunction --event events/event.json`
* Implantado na nuvem AWS via `sam deploy --guided`

Esta aplicação demonstra uma integração eficiente entre serviços serverless da `AWS` e tecnologias modernas de `IA` para criar uma `API` de geração de conteúdo criativo estruturado.


## <font color="blue">Obtenha a URL da sua API</font>

Na interface do `API Gateway` que você está visualizando (lá na `AWS`):

1. Clique em `"Estágios"` no menu lateral esquerdo.
2. Selecione o estágio `"Prod"` (criado por default pelo `SAM` (Serverless Application Model)).
3. Você verá a `URL` completa, algo como:

```
https://abc123def.execute-api.us-east-1.amazonaws.com/Prod/movie-script
```
4. Copie a `URL` e use-a para testar sua API.


## <font color="blue">Faça uma requisição usando curl (terminal)</font>

```bash
curl -X POST \
  https://abc123def.execute-api.us-east-1.amazonaws.com/Prod/movie-script \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"Um filme sobre exploradores no Peru"}'
```

## <font color="blue">Faça uma requisição usando Postman (alternativa gráfica)</font>

1. Abra o `Postman`
2. Crie uma nova requisição do tipo `POST`
3. Cole a `URL` da sua `API Gateway`
4. Na aba `"Headers"`, adicione `Content-Type` com valor `application/json`
5. Na aba `"Body"`, selecione `"raw"` e `"JSON"`
6. Digite: `{"prompt":"Um filme sobre o Dr. EddyGiusepe Cientista de Dados Sênior"}`
7. Clique em `"Send"`



## <font color="yellow">OBSERVAÇÃO</font>

A chave da `OpenAI` foi configurada no seu arquivo `template.yaml`. Durante o Deploy, o `SAM` configurou essa `variável de ambiente` na sua função Lambda. É por isso que sua aplicação está funcionando sem que você tenha configurado manualmente a chave. Você pode verificar pela `interface da AWS`, assim:

1. Acesse o console da `AWS` e vá para o serviço `Lambda`
2. Clique no nome da sua função Lambda
3. Desça até a seção `"Configuração"`
4. Clique na aba `"Variáveis de ambiente"`
5. Você verá a variável `OPENAI_API_KEY` com o valor configurado

Esta é uma prática comum para configurar chaves de API em aplicações serverless, mas existem opções mais seguras como `AWS Secrets Manager` ou `AWS Parameter Store` para armazenar chaves sensíveis.




















Thank God!