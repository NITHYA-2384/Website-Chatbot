from sklearn.feature_extraction.text import TfidfVectorizer
from langchain_community.vectorstores import FAISS
import numpy as np

class SimpleEmbedding:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.fitted = False

    def embed_documents(self, texts):
        vectors = self.vectorizer.fit_transform(texts)
        self.fitted = True
        return vectors.toarray()

    def embed_query(self, text):
        if not self.fitted:
            raise ValueError("Model not fitted yet!")
        return self.vectorizer.transform([text]).toarray()[0]

    
    def __call__(self, text):
        return self.embed_query(text)


def create_vectorstore(chunks):
    embeddings = SimpleEmbedding()

    db = FAISS.from_texts(chunks, embedding=embeddings)

    db.save_local("vectorstore")

    return db


def get_answer(db, query):
    docs = db.similarity_search(query, k=2)

    if not docs:
        return "I don't know based on the website."

    answer = " ".join([doc.page_content for doc in docs])

    if len(answer.strip()) == 0:
        return "Sorry, I couldn't find relevant info."

    return answer