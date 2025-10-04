from pydantic import BaseModel
from typing import List, Dict, Any, Optional

# --- Character Definition ---
class Character(BaseModel):
    """Defines the structure for a specific AI character."""
    id: str
    name: str
    system_prompt: str
    predefined_responses: Dict[str, str] = {}
    voice_id: str
    # Add more attributes later (e.g., model_asset_name)

# --- Chat Request/Response ---
class ChatMessage(BaseModel):
    """A single message in the conversation history."""
    role: str # 'user' or 'assistant'
    content: str

class ChatRequest(BaseModel):
    """The data structure for an incoming chat request from the client."""
    character_id: str
    user_message: str
    # History for memory, though we'll manage memory on the server soon.
    history: List[ChatMessage] = []

class ChatResponse(BaseModel):
    """The data structure for the outgoing chat response to the client."""
    character_id: str
    response_text: str
    audio_url: Optional[str] = None # Will be filled in the next step
    is_predefined: bool