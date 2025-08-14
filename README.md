# Customer-Data-Agent


I implemented this using Ollama with `llama3.1:8b` for the LLM and `mxbai-embed-large` for embeddings - the perfect combo for my laptop's performance. Here's how to get the models running locally after installing Ollama from https://ollama.com/download:

<img width="939" height="730" alt="Capture d'écran 2025-08-10 142654" src="https://github.com/user-attachments/assets/21d4153b-3980-4232-8a56-963bf9a4a268" />

**Virtual Environment Setup**  
Same terminal flow I used: 
<img width="1205" height="247" alt="demo2" src="https://github.com/user-attachments/assets/e683d803-335f-4d47-8fe1-940542195b6c" />
The exact commands that worked for my Windows setup, showing the virtual env activation and package installation.

**Results**  
<img width="1526" height="333" alt="result" src="https://github.com/user-attachments/assets/2ae243be-2550-4395-ae59-6f8485ca0565" />



##  File Structure
├── main.py # Core application logic
├── vector.py # Vector database setup
├── customer1000.csv # Sample customer dataset
├── requirements.txt # Python dependencies
└── README.md # This documentation

## 1. Dataset (`customer1000.csv`)
Contains realistic customer records with these columns:

Index,Customer Id,First Name,LastName,Company,City,Country,Phone 1,Phone 2,Email,Subscription Date,Website

##  `vector.py` - Data Vectorization

### Overview
Transforms structured customer data into a searchable vector database for AI-powered queries.

### Key Features
- **Data Ingestion**
  - Processes CSV files with customer records
  - Handles 10+ fields including contacts, locations, and company data

- **Embedding Pipeline**
  - Utilizes `mxbai-embed-large` model for text vectorization
  - Optimized for European language customer data

- **Document Structure**
  - **Searchable Content**: Combines name, company, and location fields
  - **Filterable Metadata**: 
    - Customer IDs
    - Subscription dates
    - Secondary contact info

- **Storage Solution**
  - Local ChromaDB persistence
  - Automatic collection management
  ##  `main.py` 

 
  ### Core Capabilities
- **Natural Language Interface**
  - Understands business queries about customers
  - Supports location, company, and temporal filters

- **Intelligent Retrieval**
  - Context-aware document fetching (top 5 most relevant)
  - Metadata-enhanced filtering

- **Response Generation**
  - Structured bullet-point outputs
  - Automatic contact verification
  - Privacy-preserving fallbacks ("Data not available")

### Technical Stack
| Component | Implementation Details |
|-----------|------------------------|
| LLM Backend | Ollama with custom-tuned `llama3.1:8b` |
| Temperature | 0.3 |
| Prompt Design | Multi-step verification template |


## Integration Flow
```mermaid
graph TD
    A[CSV Data] --> B(vector.py)
    B --> C[Vector Database]
    C --> D(main.py)
    D --> E[User Queries]
    E --> F[Verified Responses]




