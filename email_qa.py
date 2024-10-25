import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader

load_dotenv()

loader = CSVLoader(file_paht="data/email_qa.csv")
documents = loader.load()

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(documents, embeddings)

def retrieve_info(query):
	similar_response = db.similarity_search(query, k=3)
	return [doc.page_content for doc in similar_response]

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

template = """
AQUI VAI TODO O PROMPT PRÉ-MENSAGEM DO CLIENTE...

Aqui está uma mensagem recebida de um novo cliente. 
{message}

Aqui está uma lista de e-mails trocados anteriormente entre outros clientes e nossos atendentes.
Este histórico de conversa servirá de base para você compreender nossos produtos e forma de atender
{best_practice}

Escreva a melhor resposta que eu deveria enviar para este potencial cliente:
"""

prompt = PromptTemplate(
	input_variables=["message", "best_practice"],
	template=template
)

chain = LLMChain(llm=llm, prompt=prompt)
def generate_response(message):
	best_practice = retrieve_info(message)
	response = chain.run(message=message, best_practice=best_practice)
	return response

def main():
	st.set_page_config(page_title="E-mail manager", page_icon=":bird:")
	st.header("E-mail manager")
	message = st.text_area("E-mail do cliente")

	if message:
		st.write("Gerando um e-mail resposta baseado nas mehores práticas...")

		result = generate_response(message)

		st.info(result)

if __name__ == '__main__':
	main()
