#!/usr/bin/env python
"""
Test script to verify ProxyAPI connection.
"""

import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from config import OPENAI_API_KEY, OPENAI_BASE_URL, USE_PROXYAPI
from utils.logging import logger


async def test_proxyapi():
    """Test connection to ProxyAPI."""
    print("=" * 60)
    print("ProxyAPI Connection Test")
    print("=" * 60)
    print(f"USE_PROXYAPI: {USE_PROXYAPI}")
    print(f"OPENAI_BASE_URL: {OPENAI_BASE_URL}")
    print(f"OPENAI_API_KEY: {OPENAI_API_KEY[:10]}...{OPENAI_API_KEY[-4:]}")
    print("=" * 60)
    
    try:
        from openai import AsyncOpenAI
        
        client = AsyncOpenAI(
            api_key=OPENAI_API_KEY,
            base_url=OPENAI_BASE_URL
        )
        
        # Test embeddings
        logger.info("Testing embeddings...")
        response = await client.embeddings.create(
            model="text-embedding-ada-002",
            input="Test"
        )
        
        print(f"[OK] Embeddings work! Response has {len(response.data)} embeddings")
        
        # Test chat
        logger.info("Testing chat completion...")
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        
        print(f"[OK] Chat works! Response: {response.choices[0].message.content.strip()}")
        
        print("\n" + "=" * 60)
        print("[SUCCESS] ALL TESTS PASSED! ProxyAPI is working correctly.")
        print("=" * 60)
        return True
        
    except Exception as e:
        print(f"\n[ERROR] {e}")
        print("\nPlease check:")
        print("1. Your API key is correct and complete")
        print("2. Your ProxyAPI account has sufficient balance")
        print("3. The API key is active on proxyapi.ru")
        return False


if __name__ == "__main__":
    result = asyncio.run(test_proxyapi())
    exit(0 if result else 1)
