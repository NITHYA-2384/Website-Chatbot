from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    chunks = splitter.split_text(text)
    
    return chunks

if __name__ == "__main__":
    with open("data/website_data.txt", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = split_text(text)

    print("Total chunks:", len(chunks))
    print("\nFirst chunk:\n", chunks[0])