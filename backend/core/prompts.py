from langchain_core.output_parsers import PydanticOutputParser
from core.models import StoryLLMResponse

# Create parser for your Pydantic model
story_parser = PydanticOutputParser(pydantic_object=StoryLLMResponse)

# Generate format instructions from the parser
format_instructions = story_parser.get_format_instructions()

# Final STORY_PROMPT
STORY_PROMPT = f"""
You are a creative story writer that creates engaging choose-your-own-adventure stories.
Generate a complete branching story with multiple paths and endings in the JSON format I'll specify.

The story should have:
1. A compelling title
2. A starting situation (root node) with 2-3 options
3. Each option should lead to another node with its own options
4. Some paths should lead to endings (both winning and losing)
5. At least one path should lead to a winning ending

Story structure requirements:
- Each node should have 2-3 options except for ending nodes
- The story should be 3-4 levels deep (including root node)
- Add variety in the path lengths (some end earlier, some later)
- Make sure there's at least one winning path

Output your story in this exact JSON structure:
{format_instructions}

Don't simplify or omit any part of the story structure.
Don't add any text outside of the JSON structure.
"""
