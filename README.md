# LLMs to the Rescue: Explaining DSA Statements of Reason

[![Paper](https://img.shields.io/badge/Paper-ACL%20Anthology-red)](https://aclanthology.org/2024.nllp-1.17/)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains the implementation framework for the paper **"LLMs to the Rescue: Explaining DSA Statements of Reason with Platform's Terms of Services"** presented at the Natural Legal Language Processing Workshop (NLLP) 2024.

## 📄 Abstract

The Digital Services Act (DSA) requires online platforms in the EU to provide "statements of reason" (SoRs) when restricting user content, but their effectiveness in ensuring transparency is still debated due to vague and complex terms of service (ToS). This paper explores the use of NLP techniques, specifically multi-agent systems based on large language models (LLMs), to clarify SoRs by linking them to relevant ToS sections. Analysing SoRs from platforms like Booking.com, Reddit, and LinkedIn, our findings show that LLMs can enhance the interpretability of content moderation decisions, improving user understanding and engagement with DSA requirements.

## 🎯 Overview

This framework uses a multi-agent LLM system to:

1. **Extract Relevant ToS Sections**: Analyze platform Terms and Conditions to identify sections related to content restriction
2. **Refine Legal Context**: Process and refine relevant ToS text to support statement of reason analysis
3. **Generate User-Friendly Explanations**: Produce clear, intelligible explanations of content moderation decisions by linking SoRs to specific ToS provisions

The system employs:
- **Vector databases** (ChromaDB) with legal-domain embeddings (VoyageAI Law-2)
- **Retrieval-Augmented Generation (RAG)** for contextual ToS retrieval
- **Multi-agent prompting** for legal reasoning and explanation generation

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Statement of Reason                     │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│          Vector Database (ChromaDB + VoyageAI)          │
│            Terms and Conditions Corpus                   │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              Refine Agent (LLM)                         │
│     Extract relevant ToS sections & sentences            │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│            Explanation Agent (LLM)                      │
│   Generate user-friendly explanations with:             │
│   - Main ground for restriction                         │
│   - Definition of the ground                            │
│   - Examples of restricted content                      │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key (for GPT models)
- VoyageAI API key (for legal domain embeddings)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sustaz/NLP_DSA_transparency.git
cd NLP_DSA_transparency
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API keys:
```python
import os
os.environ['GPT_KEY'] = 'your-openai-api-key'
os.environ['VOYAGE_API_KEY'] = 'your-voyageai-api-key'
```

### Usage

#### 1. Create Vector Database from ToS Documents

```python
from src.create_chroma_db import create_vector_store
from src.text_chunker import split_by_newline_caps

# Process your ToS document
chunks = split_by_newline_caps(tos_text)

# Create vector database
db_path = './db/platform_tos'
create_vector_store(chunks, db_path)
```

#### 2. Process Statements of Reason

```python
from src.prompts import build_refine_tec, build_prompt
from src.read_chroma_db import retrieve_relevant_tos

# Your statement of reason
statement = "Your content was removed for violating our community guidelines..."

# Retrieve relevant ToS sections
relevant_tos = retrieve_relevant_tos(statement, db_path)

# Refine the ToS sections
refine_prompt = build_refine_tec(statement, relevant_tos)
refined_tos = llm.generate(refine_prompt)

# Generate explanation
explanation_prompt = build_prompt(statement, refined_tos)
explanation = llm.generate(explanation_prompt)
```

#### 3. Run the Complete Notebook

Open and run [statement_of_reason_llm.ipynb](statement_of_reason_llm.ipynb) for a complete end-to-end example.

## 📁 Repository Structure

```
NLP_DSA_transparency/
├── src/
│   ├── create_chroma_db.py      # Vector database creation
│   ├── read_chroma_db.py        # ToS retrieval functions
│   ├── prompts.py               # LLM prompt templates
│   ├── text_chunker.py          # Document preprocessing
│   └── utils.py                 # Utility functions
├── bash_commands/
│   ├── add_commit_push.sh       # Git automation
│   └── set_git_credentials.sh   # Git configuration
├── statement_of_reason_llm.ipynb # Main workflow notebook
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🔑 Key Components

### Vector Database
- **ChromaDB** for efficient similarity search
- **VoyageAI Law-2** embeddings optimized for legal text
- Cosine similarity for semantic matching

### Multi-Agent System
1. **Refinement Agent**: Extracts precise ToS sections without modification
2. **Explanation Agent**: Generates user-friendly explanations with:
   - Main grounds for restriction
   - Definitions from ToS
   - Concrete examples

### Prompt Engineering
The system uses carefully crafted prompts to ensure:
- Legal accuracy
- Plain language explanations
- Structured output format
- No hallucination of information

## 📊 Evaluated Platforms

The framework was tested on SoRs from:
- **Booking.com**
- **Reddit**
- **LinkedIn**

## 📖 Citation

If you use this framework in your research, please cite:

```bibtex
@inproceedings{aspromonte-etal-2024-llms,
    title = "{LLM}s to the Rescue: Explaining {DSA} Statements of Reason with Platform's Terms of Services",
    author = "Aspromonte, Marco and Ferraris, Andrea and Galli, Federico and Contissa, Giuseppe",
    booktitle = "Proceedings of the Natural Legal Language Processing Workshop 2024",
    month = nov,
    year = "2024",
    address = "Miami, FL, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.nllp-1.17",
    doi = "10.18653/v1/2024.nllp-1.17",
    pages = "205--215"
}
```

## 👥 Authors

- **Marco Aspromonte**
- **Andrea Ferraris**
- **Federico Galli**
- **Giuseppe Contissa**

## 📜 License

This project is licensed under the Creative Commons Attribution 4.0 International License - see the [ACL Anthology](https://aclanthology.org/2024.nllp-1.17/) for details.

## 🔗 Links

- [Paper (ACL Anthology)](https://aclanthology.org/2024.nllp-1.17/)
- [Paper (PDF)](https://aclanthology.org/2024.nllp-1.17.pdf)
- [NLLP 2024 Workshop](https://aclanthology.org/volumes/2024.nllp-1/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚖️ Legal & Regulatory Context

This work addresses transparency requirements under the EU's **Digital Services Act (DSA)**, which mandates that platforms provide clear explanations when restricting user content. The framework aims to bridge the gap between complex legal language in Terms of Service and user understanding of content moderation decisions.

## 📧 Contact

For questions or collaboration opportunities, please reach out to the authors through the ACL Anthology contact information.

---

**Note**: This framework requires API access to OpenAI and VoyageAI services. Ensure you have valid API keys and are aware of associated costs before running large-scale experiments.
