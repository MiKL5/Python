from http.client import responses

import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from narwhals import to_py_scalar

OPENAI_API_KEY = ""

# interface
st.header("My first chatbot")
with st.sidebar: # colonne à gauche
    st.title("Documents")
    files = st.file_uploader("Download PDF file" , type="pdf" , accept_multiple_files = True) # bouton de chargement

if files : # is not None
    st.write("Thanks!")
    for file in files :
        st.write(f"I've received the file·s {file.name} , weighing {file.size} bits.")
        st.write("If this is the right file·s , I'm delighted to reply. Else , please choose another one.")
else :
    st.write(" ")
    st.write("You can add a PDF file to get started.")

# Analyser le·s fichier·s
if files : # is not None
    text = ""
    for file in files:
        reader = PdfReader(file)  # extraction

        for page in reader.pages : # Parcours page à page
            page_text = page.extract_text() # Extraire le texte et un saut entre chaque page
            if page_text :
                text += page_text + "\n"
            else :
                st.warning(f"At least one page of '{file.name}' contains no usable text!")

    # Divisions en morceaux
    text_spliter = RecursiveCharacterTextSplitter (
        separators = ["\n"] ,
        chunk_size = 1250 , # initialement 1000
        chunk_overlap = 100 , # 150 caractères se chevauchent pour ne pas perdre d'infos
        length_function = len # 1000 caractères
    )
    chunks = text_spliter.split_text(text)

    # Générer les encastrements
    embeddings = OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY)

    # Création de la BDD vectorielle
    vectorial_bdd = FAISS.from_texts(chunks , embeddings)

    # Poser une question
    query = st.text_input("Comment puis-je vous aider ?")

    # Recherche de chunks analogues à la requête
    if query :
        all_results = vectorial_bdd.similarity_search(query)
        results = all_results[:4] # Analyse 4 morceaux
        # st.write(results) # En masquant ce code Le résultat s'affiche au lieu des chuncks

        llm = ChatOpenAI(
            openai_api_key = OPENAI_API_KEY ,
            temperature = 0 , # Plus la température est basse et plus les répose sera précise (entre 0 et 1)
            max_tokens = 100 ,
            model_name = "gpt-3.5-turbo"
        )

        # Chargement de la chaîne de Q&A
        chain = load_qa_chain(llm , chain_type="stuff") # stuff concatène les éléments

        response = chain.run(input_documents = results , question = query)

        # Affichage de la réponse
        st.write("Here is the response:")
        st.write(response)

        # Télécharger la réponse
        st.download_button(
            label = "Upload response" ,
            data = response ,
            file_name = "chatbotResponse.txt" ,
            mime = "text_plain"
        )