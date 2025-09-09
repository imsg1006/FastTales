from langchain_core.output_parsers import PydanticOutputParser
from core.models import StoryLLMResponse

# Create parser for your Pydantic model
story_parser = PydanticOutputParser(pydantic_object=StoryLLMResponse)

# Generate format instructions from the parser
format_instructions = story_parser.get_format_instructions()

# Final STORY_PROMPT
STORY_PROMPT = f"""
Create a choose-your-own-adventure story in JSON format.

Requirements:
- Title and starting situation with 2-3 options
- 3-4 levels deep with branching paths
- Include both winning and losing endings
- Each node has 2-3 options (except endings)

{format_instructions}

Return only valid JSON, no additional text.
"""