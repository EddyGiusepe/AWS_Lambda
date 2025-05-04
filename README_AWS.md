# <h1 align="center"><font color="red">projeto-aws-lambda</font></h1>


<font color="pink">Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro</font>


Este projeto contém código fonte e arquivos de suporte para uma aplicação serverless que você pode implantar com o `SAM CLI`. Ele inclui os seguintes arquivos e pastas:

- hello_world - Código para a `função Lambda` da aplicação.
- events - Eventos de invocação que você pode usar para invocar a função.
- tests - Testes unitários para o código da aplicação.
- `template.yaml` - Um template que define os recursos da AWS para a aplicação.

A aplicação utiliza vários recursos da `AWS`, incluindo funções Lambda e uma `API Gateway`. Esses recursos são definidos no arquivo `template.yaml` neste projeto. Você pode atualizar o template para adicionar recursos da `AWS` através do mesmo processo de implantação que atualiza o código da aplicação.

Se você preferir usar um ambiente de desenvolvimento integrado (`IDE`) para construir e testar sua aplicação, você pode usar o `AWS Toolkit`.  
O `AWS Toolkit` é uma extensão de código aberto para popular `IDEs` que usa o `SAM CLI` para construir e implantar aplicações serverless na `AWS`. O `AWS Toolkit` também adiciona uma experiência de depuração passo a passo simplificada para o código da `função Lambda`. Veja os seguintes links para começar.

* [CLion](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [GoLand](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [WebStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [Rider](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PhpStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [RubyMine](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [DataGrip](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## <font color="red">Implantar a aplicação de exemplo</font>

A `Interface de Linha de Comando` do Modelo de Aplicação Serverless (`SAM CLI`) é uma extensão da `AWS CLI` que adiciona funcionalidades para construir e testar aplicações Lambda. Ela usa o `Docker` para executar suas funções em um ambiente Amazon Linux que corresponde ao Lambda. Ela também pode emular o ambiente de construção e a API da sua aplicação.

Para usar o `SAM CLI`, você precisa dos seguintes ferramentas.

* `SAM CLI` - [Instale o SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 instalado](https://www.python.org/downloads/)
* `Docker` - [Instale a versão comunitária do Docker](https://hub.docker.com/search/?type=edition&offering=community)

Para construir e implantar sua aplicação pela primeira vez, execute o seguinte no seu shell:

```bash
sam build --use-container
sam deploy --guided
```

`O primeiro` comando construirá o código fonte da sua aplicação. `O segundo` comando implantará sua aplicação para a `AWS`, com uma série de prompts:

* **Stack Name**: O nome da pilha (stack) a ser implantado no `CloudFormation`. Este deve ser único para sua conta e região, e um bom ponto de partida seria algo correspondente ao nome do seu projeto.
* **AWS Region**: A região da `AWS` que você deseja implantar sua aplicação.
* **Confirm changes before deploy**: Se definido como `yes`, qualquer conjunto de alterações será mostrado para você antes da execução para revisão manual. Se definido como `no`, a `AWS SAM CLI` implantará automaticamente as alterações da aplicação.
* **Allow SAM CLI IAM role creation**: Muitos templates do `AWS SAM`, incluindo este exemplo, criam funções `IAM` necessárias para que as funções `Lambda` incluídas acessem serviços da `AWS`. Por padrão, essas funções são limitadas a permissões mínimas necessárias. Para implantar uma pilha do `AWS CloudFormation` que cria ou modifica funções `IAM`, o valor `CAPABILITY_IAM` para `capabilities` deve ser fornecido. Se a permissão não for fornecida por meio deste prompt, para implantar este exemplo, você deve passar explicitamente `--capabilities CAPABILITY_IAM` para o comando `sam deploy`.
* **Save arguments to samconfig.toml**: Se definido como `yes`, suas escolhas serão salvas em um arquivo de configuração dentro do projeto, para que no futuro você possa apenas executar `sam deploy` sem parâmetros para implantar alterações na sua aplicação.

Você pode encontrar o `URL` do `Endpoint` da `API Gateway` na saída de valores exibidos após a implantação.

## <font color="red">Use o SAM CLI para construir e testar localmente</font>

Construa sua aplicação com o comando `sam build --use-container`.

```bash
projeto-aws-lambda$ sam build --use-container
```

O `SAM CLI` instala as dependências definidas em `hello_world/requirements.txt`, cria um pacote de implantação e salva em a pasta `.aws-sam/build`.

Teste uma função individual invocando-a diretamente com um evento de teste. Um evento é um documento JSON que representa a entrada que a função recebe do evento de origem. Eventos de teste estão incluídos na pasta `events` neste projeto.

Execute funções localmente e invoque-as com o comando `sam local invoke`.

```bash
projeto-aws-lambda$ sam local invoke HelloWorldFunction --event events/event.json
```

O `SAM CLI` também pode emular sua aplicação's API. Use o `sam local start-api` para executar a API localmente na porta 3000.

```bash
projeto-aws-lambda$ sam local start-api
projeto-aws-lambda$ curl http://localhost:3000/
```

O `SAM CLI` lê o modelo de aplicação para determinar as rotas e as funções que elas invocam. A propriedade `Events` em cada definição de função inclui a rota e o método para cada caminho.

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

## <font color="red">Adicione um recurso à sua aplicação</font>

O modelo de aplicação usa o Modelo de Aplicação Serverless (`AWS SAM`) para definir recursos de aplicação. O `AWS SAM` é uma extensão do `AWS CloudFormation` com uma sintaxe mais simples para configurar recursos comuns de aplicações serverless como funções, gatilhos e APIs. Para recursos não incluídos na [especificação SAM](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), você pode usar tipos de recursos padrão [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html).

## <font color="red">Fetch, tail, and filter Lambda function logs</font>

Para simplificar o troubleshooting, o `SAM CLI` tem um comando chamado `sam logs`. `sam logs` permite que você obtenha logs gerados pela sua função Lambda da linha de comando. Além de imprimir os logs no terminal, este comando tem várias funcionalidades para ajudá-lo a encontrar o bug rapidamente.

`OBS`: Este comando funciona para todas as funções `AWS Lambda`; não apenas as que você implanta usando `SAM`.

```bash
projeto-aws-lambda$ sam logs -n HelloWorldFunction --stack-name "projeto-aws-lambda" --tail
```

Você pode encontrar mais informações e exemplos sobre como filtrar logs de funções Lambda na [Documentação do SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## <font color="red">Tests</font>

Os testes são definidos na pasta `tests` neste projeto. Use `PIP` para instalar as dependências de teste e executar os testes.

```bash
projeto-aws-lambda$ pip install -r tests/requirements.txt --user
# unit test
projeto-aws-lambda$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
projeto-aws-lambda$ AWS_SAM_STACK_NAME="projeto-aws-lambda" python -m pytest tests/integration -v
```

## <font color="red">Cleanup</font>

Para deletar a aplicação de exemplo que você criou, use a `AWS CLI`. Assumindo que você usou o nome do projeto para o nome da pilha, você pode executar o seguinte:

```bash
sam delete --stack-name "projeto-aws-lambda"
```

## <font color="red">Recursos</font>

Veja a [Guia do desenvolvedor do AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) para uma introdução à especificação SAM, o SAM CLI e conceitos de aplicações serverless.

Em seguida, você pode usar o [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo/) para implantar aplicativos prontos para uso que vão além dos exemplos de hello world e aprender como os autores desenvolveram seus aplicativos: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)






# <font color="red">AWS SAM (Serverless Application Model) para testar funções `AWS Lambda` localmente</font>

Para testar funções `AWS Lambda` localmente, você precisa ter o SAM CLI instalado. E seguir os seguintes comandos:

```bash
# Instalar SAM CLI:
pip install aws-sam-cli    ou     uv add aws-sam-cli

# Iniciar projeto
sam init

# ou
sam init --runtime python3.9 --name movie-script-generator
cd movie-script-generator
```





# <font color="red">AWS Lambda</font>

Para executar o projeto, você precisa ter o SAM CLI instalado. E seguir os seguintes comandos:

* Primeiro, eu precisei de permissão:

```bash
sudo chmod 666 /var/run/docker.sock
```

* As vezes instalar a biblioteca no seu ambiente local não é suficiente. A função lambda roda em um container isolado. Para seguiremos os seguintes passos:

1. Certifique-se que o arquivo requirements.txt está correto.:

```bash
   echo "requests" > hello_world/requirements.txt
```

2. Execute o build para incorporar as dependências:

```bash
sam build --use-container
```

A flag `--use-container` garante que as dependências sejam instaladas em um ambiente compatível com o Lambda.

3. Execute a função após o build:

```bash
sam local invoke HelloWorldFunction --event events/event.json

# ou no caso de usar o nome da função dentro do template.yaml:
sam local invoke MovieScriptFunction -e events/event.json
```

4. Depois fazemos o Deploy com o assistente guiado:

```bash
sam deploy --guided

# ou usando um parâmetro Key da OpenAI:
sam deploy --guided --parameter-overrides OpenAIApiKey=sk-sua-chave-aqui
```


`OBS:`

Durante o deploy guiado, responda às perguntas:

* Stack Name: escolha um nome (ex: megasena-lambda)
* AWS Region: escolha sua região (ex: us-east-1)
* Confirm changes before deploy: Yes
* Allow SAM CLI IAM role creation: Yes
* Disable rollback: No
* Save arguments to configuration file: Yes

Após a conclusão, o SAM mostrará os outputs, incluindo URLs (se configurado API Gateway). Sua função estará disponível no console AWS Lambda com o nome escolhido.



# <font color="red">AWS configurações</font>

* Configuramos as credenciais da AWS, execute:

```bash
aws configure
```

* Eliminar apenas a função Lambda pela interface não é correto, pois deixará outros recursos ativos que podem gerar custos.
A forma correta é eliminar a `stack completa`, que removerá todos os recursos criados:

```bash
sam delete
```

ou especificando o nome da stack:

```bash
sam delete --stack-name <NOME_QUE_VOCÊ_ESCOLHEU>
```

Você pode encontrar o nome da stack no arquivo `samconfig.toml` na linha `stack_name = <NOME_DA_STACK>`. Se tiver dois `stack_name`, use o nome que está na seção deploy.parameters.

No console da AWS, você pode encontrar a stack na seção `CloudFormation` e clicar no nome da stack (`pilha`).
