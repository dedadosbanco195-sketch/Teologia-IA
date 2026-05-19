from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts.prompt_teologico import PROMPT_TEOLOGICO

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0.4
)

prompt = PromptTemplate(
    input_variables=["pergunta"],
    template=PROMPT_TEOLOGICO
)

def perguntar_teologia(pergunta):
    chain = prompt | llm | StrOutputParser()

    resposta = chain.invoke({
        "pergunta": pergunta
    })

    return resposta
