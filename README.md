# Assistente Virtual Inteligente com ChatGPT e Dados Personalizados

Este projeto demonstra como criar um assistente virtual utilizando o ChatGPT e seus próprios dados de forma simples e eficiente. Utilizando Python e a biblioteca [LangChain](https://github.com/hwchase17/langchain), é possível conectar LLMs (Large Language Models) a diversos tipos de dados personalizados, criando um sistema inteligente e responsivo às necessidades específicas de cada usuário.

## Funcionalidades

- **Alimentação de LLMs com Dados Próprios**: Integração de LLMs com dados específicos que o usuário deseja usar, personalizando o conhecimento do assistente.
- **Processamento Natural de Linguagem (NLP)**: Aproveita o poder da API ChatGPT para entender e responder perguntas com base nos dados fornecidos.
- **Inteligência Adaptável**: Pode ser treinado com diferentes tipos de dados para suportar desde perguntas frequentes até soluções complexas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **LangChain**: Biblioteca que facilita a integração de LLMs com diferentes fontes de dados.
- **ChatGPT**: Utilizado para processar e responder perguntas com base no contexto oferecido pelos dados do usuário.

## Pré-requisitos

1. **Python 3.8+**
2. **Instalar as dependências**:
    ```bash
    pip install langchain openai streamlit python_dotenv langchain_community
    ```

## Como Usar

1. **Configuração da API**: Adicione sua chave de API do OpenAI no arquivo `.env` ou diretamente no código.
2. **Alimentação dos Dados**: Defina os dados que deseja que o assistente utilize. Estes dados podem ser carregados de um banco de dados, arquivos locais, APIs, entre outras fontes.
3. **Inicialização do Assistente**: Execute o script principal para iniciar a interação com o assistente virtual.

## Exemplo de Uso

Após configurar o projeto, basta inicializar a aplicação e começar a fazer perguntas. O assistente responderá com base nos dados fornecidos e no contexto do ChatGPT.

```bash
python assistente_virtual.py
```

---

## Contribuições

Sinta-se à vontade para contribuir com melhorias, sugestões ou correções. Pull requests são bem-vindos!

---

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

--- 

