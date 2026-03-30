from backend import create_vectorstore, get_answer
from text_splitter import split_text

with open("data/website_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = split_text(text)
db = create_vectorstore(chunks)

print("Chatbot Ready!\n")

while True:
    query = input("Ask something (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    response = get_answer(db, query)
    print("\n🤖:", response, "\n")