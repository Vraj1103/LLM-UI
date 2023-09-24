import streamlit as st
import pickle
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

with st.sidebar:
    st.title("Isolated Falcons")
    st.markdown('''
    # About
    This is a web application that uses the GPT-3 API to generate summaries of text.
    ''')
    add_vertical_space(5)

def main():
    st.header("PDF Analysis")
    pdf = st.file_uploader("Upload a PDF", type='pdf')
    st.write(pdf.name)
    st.write(pdf.type)

    if pdf is not None:

        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)

        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        store_name = pdf.name[:-4]

        with open(f"{store_name}.pkl", "wb") as f:
            pickle.dump(VectorStore, f)

        # st.write(chunks)
        # st.write(text)
        # st.write(pdf_reader)


if __name__ == '__main__':
    main()