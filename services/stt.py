"""
Speech-to-Text Service.
Handles voice message transcription.
"""

from pathlib import Path
from typing import Union

from services.openai_client import openai_client
from utils.logging import logger
from utils.helpers import convert_ogg_to_wav, cleanup_file


async def transcribe_voice_message(audio_path: Union[str, Path]) -> str:
    """
    Transcribe a voice message to text.
    
    Args:
        audio_path: Path to audio file (OGG or WAV)
    
    Returns:
        Transcribed text
    """
    audio_path = Path(audio_path)
    wav_path = None
    
    try:
        # Send OGG directly to Whisper API (no conversion needed)
        if audio_path.suffix.lower() == '.ogg':
            logger.debug(f"Transcribing OGG directly: {audio_path}")
            transcription_path = audio_path
        elif audio_path.suffix.lower() == '.wav':
            logger.debug(f"Transcribing WAV: {audio_path}")
            transcription_path = audio_path
        else:
            # For other formats, try to send as-is
            logger.warning(f"Unknown audio format: {audio_path.suffix}, sending as-is")
            transcription_path = audio_path
        
        # Transcribe using OpenAI Whisper
        text = await openai_client.transcribe_audio(transcription_path)
        
        logger.info(f"Transcription completed: {len(text)} characters")
        return text
        
    except Exception as e:
        logger.error(f"Error in voice transcription: {e}")
        raise
        
