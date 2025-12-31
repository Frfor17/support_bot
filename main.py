# Псевдокод для иллюстрации логики
from langchain_huggingface import HuggingFaceEndpoint, HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain.chains import RetrievalQA

# 1. Инициализируем модель для эмбеддингов и векторное хранилище
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = QdrantVectorStore.from_documents(your_documents, embeddings, connection=your_qdrant_client)

# 2. Инициализируем LLM
llm = HuggingFaceEndpoint(repo_id="microsoft/Phi-3-mini-4k-instruct", task="text-generation")

# 3. Создаем цепочку RAG
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vector_store.as_retriever())

# 4. Задаем вопрос
answer = qa_chain.run("Как сбросить пароль?")
print(answer)