from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# initialize the model 

model = OllamaLLM(model="llama3.1:8b", temperature=0.3) 

# create the template 

template = """
You are a customer support AI expert working with our client database.
Always respond professionally and verify facts using the provided customer records.

Relevant customer records:
{context}

Question: {question}

Instructions:
1. Answer ONLY using the provided customer data
2. If unsure, say "I don't have that information"
3. For contact requests, always verify the latest details
4. Format responses clearly with bullet points when listing customers
"""

prompt=ChatPromptTemplate.from_template(template)

chain = (
    {"context": lambda x: x["context"], "question": lambda x: x["question"]} 
    | prompt 
    | model 
    | StrOutputParser()
)


while True:
    print("\n" + "="*50)
    question = input("Ask about customers (type 'quit' to exit): ").strip()
    print("\n")
    
    if question.lower() in ("q", "quit", "exit"):
        break
    
    try:
        # 1. Retrieve relevant customer records
        customer_docs = retriever.invoke(question)
        
        # 2. Generate response with proper context
        response = chain.invoke({
            "context": customer_docs,
            "question": question
        })
        
        # 3. Display formatted response
        print("🔍 Customer Data Response:")
        print("-"*40)
        print(response)
        print("\n" + "Sources:")
        for i, doc in enumerate(customer_docs, 1):
            print(f"{i}. Customer ID: {doc.metadata.get('customer_id', 'N/A')}")
    
    except Exception as e:
        print(f"⚠️ Error processing your request: {str(e)}")