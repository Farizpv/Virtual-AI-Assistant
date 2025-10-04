from .schemas import Character, ChatMessage
from typing import Dict, List


class CharacterManager:
    """Manages all defined characters and their configurations."""

    def __init__(self):
        # In a real app, this would load from a database or JSON file.
        # For now, we hardcode the initial characters.
        self._characters: Dict[str, Character] = self._load_characters()

    def _load_characters(self) -> Dict[str, Character]:
        """Loads and initializes character definitions."""

        # --- Predefined Response Logic (The Optimization) ---
        # If the user says a specific keyword, we avoid calling the LLM
        # and return a fast, predefined response.

        sherlock_responses = {
            "hello": "Ah, a new case, or merely a greeting? State your purpose, I've matters to deduce.",
            "who are you": "I am a Consulting Detective, Faari. I observe and deduce, finding the signal in the noise.",
            "what is your name": "You may refer to me as The Detective. Now, focus on the facts.",
            "bye": "Very well. The game is afoot elsewhere, it seems. Do keep your mind sharp."
        }

        # Define Character Objects
        detective = Character(
            id="detective",
            name="The Detective",
            system_prompt="You are a cool, brilliant, and observant detective, similar to Sherlock Holmes. You speak in a formal, slightly condescending tone, and use deductive reasoning to answer. You end every non-deductive response with a thought-provoking question.",
            predefined_responses=sherlock_responses,
            voice_id="sh_male_cool"  # Placeholder
        )

        princess = Character(
            id="princess",
            name="The Princess",
            system_prompt="You are a cheerful, optimistic, and slightly naive fairy-tale princess. You use flowery, encouraging language and avoid dark topics. Your goal is to make the user feel happy and loved. Speak as if you are royalty from a magical kingdom.",
            predefined_responses={},  # No predefined responses for the Princess yet
            voice_id="pr_female_sweet"  # Placeholder
        )

        return {
            detective.id: detective,
            princess.id: princess,
        }

    def get_character(self, character_id: str) -> Character:
        """Retrieves a character by ID, raising an error if not found."""
        if character_id not in self._characters:
            raise ValueError(f"Character ID '{character_id}' not found.")
        return self._characters[character_id]

    def check_predefined_response(self, character_id: str, user_message: str) -> (bool, str):
        """
        Checks if the user's message matches a predefined keyword for the character.
        Returns: (is_predefined: bool, response: str)
        """
        character = self.get_character(character_id)
        # Simple, case-insensitive, whole-word matching for MVP.
        # Future refinement: Use fuzzy matching or regex.
        message_lower = user_message.strip().lower()

        if message_lower in character.predefined_responses:
            return (True, character.predefined_responses[message_lower])

        return (False, "")


# Global instance for easy access across the app
character_manager = CharacterManager()