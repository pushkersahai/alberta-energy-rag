# Alberta Energy Regulations RAG Assistant

Regulations RAG for Alberta energy using Databricks + Azure OpenAI.

## Business Problem
Energy companies and regulatory professionals spend hours searching through dense regulatory documents. This RAG system provides instant, accurate answers grounded in official AER directives.

## Tech Stack
- **Azure Databricks**: Unity Catalog, Delta Lake, Vector Search
- **Azure OpenAI**: text-embedding-3-small, gpt-4o-mini
- **Data Source**: Alberta Energy Regulator public directives

## Architecture
```
User Question → Embedding → Vector Search → Context Retrieval → LLM Generation → Answer
```

## Key Features
1. **Unified Lakehouse**: Single Delta table stores text + embeddings + metadata
2. **Databricks Vector Search**: No separate vector database needed
3. **Source Attribution**: Every answer cites specific documents

## Documents Indexed
- AER Directive 017: Measurement Requirements (866K chars)
- AER Directive 060: Upstream Petroleum Industry Flaring (250K chars)
- Total: 1,396 chunks with 1536-dimensional embeddings

## Demo Queries
- "What are the flaring requirements in Alberta?"
- "What does Directive 017 cover?"
- "What are measurement requirements for oil production?"

## Technical Highlights
- **Delta Lake**: ACID transactions, time travel, Change Data Feed
- **Unity Catalog**: Centralized governance and lineage tracking
- **Vector Search**: HNSW index for sub-second similarity search
- **Multi-region**: Optimized endpoints (Canada East + East US 2)


## Project Structure
```
azure-energy-rag/
├── notebooks/
│   └── energy_rag_system.ipynb    # Main implementation
├── docs/
│   └── ARCHITECTURE.md             # Detailed architecture
├── test_azure_openai.py            # Local testing script
└── README.md
```

## Setup Instructions

### Prerequisites
- Azure account with Databricks Premium workspace
- Azure OpenAI resource with deployed models
- Python 3.10+


## Future Enhancements
- Add more AER directives and regulations
- Multi-modal: Include diagrams and tables from PDFs
- Real-time updates: Auto-sync when new directives published
- Fine-tuned embeddings for domain-specific terminology

## Contact
www.linkedin.com/in/pushkersahai
