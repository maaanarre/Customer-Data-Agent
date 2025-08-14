# Customer-Data-Agent

## 📂 File Structure
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
| Temperature | 0.3 for business-appropriate determinism |
| Prompt Design | Multi-step verification template |
| Error Handling | Graceful fallbacks for missing data |

## Integration Flow
```mermaid
graph TD
    A[CSV Data] --> B(vector.py)
    B --> C[Vector Database]
    C --> D(main.py)
    D --> E[User Queries]
    E --> F[Verified Responses]
