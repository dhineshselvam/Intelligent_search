# Intelligent Search - Academic Paper Discovery

An intelligent search system for discovering academic papers using AI-powered embeddings and semantic similarity search.

## Features

- **AI-Powered Search**: Uses embeddings and FAISS for semantic similarity matching
- **Paper Ingestion**: Automated data ingestion pipeline for academic papers
- **RESTful API**: FastAPI backend for search and metadata queries
- **Web Interface**: Clean, responsive frontend for searching papers
- **Metadata Support**: Rich paper metadata including titles, authors, and abstracts

## Project Structure

```
intelligent-search/
├── backend/
│   ├── api.py           # FastAPI application
│   ├── search.py        # Search functionality
│   ├── embeddings.py    # Embedding generation
│   ├── llm.py          # LLM integration
│   ├── ingest.py       # Data ingestion pipeline
│   └── data/           # Processed data and indices
│       ├── arxiv_data.json
│       ├── papers_meta.csv
│       └── paper_index.faiss
└── frontend/
    ├── index.html      # Web interface
    ├── script.js       # Frontend logic
    └── style.css       # Styling
```

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js (optional, for frontend development)

### Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the backend API:
```bash
python backend/api.py
```

3. Open the frontend:
```bash
# Open frontend/index.html in your browser
```

## Usage

### Search Papers
- Open the web interface in your browser
- Enter your search query
- View results with paper metadata and relevance scores

### API Endpoints
- `GET /search?query=<query>` - Search for papers
- `GET /papers/<id>` - Get paper details
- `POST /ingest` - Trigger data ingestion

## Technologies

- **Backend**: Python, FastAPI, FAISS, Embeddings
- **Frontend**: HTML5, CSS3, JavaScript
- **Data**: JSON, CSV, FAISS indexes

## Contributing

Contributions welcome! Please feel free to submit pull requests.

## License

MIT License - feel free to use and modify as needed.
