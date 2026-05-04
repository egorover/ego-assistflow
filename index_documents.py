#!/usr/bin/env python
"""
Script to index documents in the RAG knowledge base.
Run this after adding new documents to data/documents/
"""

import asyncio
from pathlib import Path
import shutil
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from config import DATA_DIR, DOCUMENTS_DIR
from utils.logging import logger


async def main():
    """Main function to index documents."""
    from rag.index import VectorIndex
    
    persist_dir = DATA_DIR / "chroma_db"
    
    # Create new index (will load or create)
    logger.info("Creating new vector index...")
    index = VectorIndex(persist_directory=persist_dir)
    
    # Index documents
    logger.info(f"Indexing documents from {DOCUMENTS_DIR}...")
    count = index.index_documents_directory(DOCUMENTS_DIR, force_reindex=False)
    
    # Show stats
    stats = index.get_stats()
    logger.info(f"✅ Indexing complete!")
    logger.info(f"   Total documents: {stats.get('total_documents', 0)}")
    logger.info(f"   Persist directory: {stats.get('persist_directory')}")
    
    return count


if __name__ == "__main__":
    count = asyncio.run(main())
    print(f"\nIndexed {count} document chunks")
