from typing import Any, Dict, List,Optional
from pydantic import BaseModel, Field

class StoryOptionalLLM(BaseModel):
    text:str = Field(description="The text of the option shown to the user")
    nextNode:Dict[str, Any] = Field(description="The next node content and its options")


class StoryNodeLLM(BaseModel):
    content: str = Field(description="The content of the story node")
    isEnding: bool = Field(description="Whether this node is an ending")
    isWinningEnding: bool = Field(description="Whether this ending is a winning ending")
    options: List[StoryOptionalLLM] = Field(description="The options for the user to choose from")

class StoryLLMResponse(BaseModel):
    title : str = Field(description="The title of the story")
    rootNode:StoryNodeLLM = Field(description="The root node of the story")
    