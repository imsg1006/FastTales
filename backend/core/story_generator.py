import google.generativeai as genai
from sqlalchemy.orm import Session
from langchain_core.output_parsers import PydanticOutputParser      

from core.prompts import STORY_PROMPT
from models.story import Story, StoryNode
from core.models import StoryLLMResponse, StoryNodeLLM
from dotenv import load_dotenv
import os

load_dotenv()
  
class StoryGenerator:

    @classmethod 
    def _get_llm(cls):
     genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
     return genai.GenerativeModel(
        'gemini-1.5-flash',
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 2000,  # Limit output size
            "top_p": 0.9,
            "top_k": 40
        }
    )

    @classmethod
    def generate_story(cls, db: Session, session_id: str, theme: str = "fantasy") -> Story:
        llm = cls._get_llm()
        prompt = f"{STORY_PROMPT}\nCreate the story with this theme: {theme}"

        response = llm.generate_content(prompt)
        response_text = response.text if hasattr(response, "text") else str(response)

        # Parse and store as before
        story_parser = PydanticOutputParser(pydantic_object=StoryLLMResponse)
        story_structure = story_parser.parse(response_text)

        story_db = Story(title=story_structure.title, session_id=session_id)
        db.add(story_db)
        db.flush()

        root_node_data = story_structure.rootNode
        if isinstance(root_node_data, dict):
            root_node_data = StoryNodeLLM.model_validate(root_node_data)

        cls._process_story_node(db, story_db.id, root_node_data, is_root=True)

        db.commit()
        return story_db
 
    @classmethod
    def _process_story_node(cls , db:Session,story_id:int,node_data:StoryNodeLLM, is_root:bool = False)-> StoryNode:
        if isinstance(node_data, dict):
          node_data = StoryNodeLLM.model_validate(node_data)
        
        node  = StoryNode(
            story_id=story_id, 
            content=node_data.content,
            is_root=is_root,
            is_ending=node_data.isEnding,
            is_winning_ending=node_data.isWinningEnding,
            options=[]
            )
        db.add(node)
        db.flush()

        if not node.is_ending and node_data.options:
            options_list = []
            for options_data in node_data.options:
                next_node = options_data.nextNode

               
                child_node = cls._process_story_node(db, story_id, next_node, is_root=False)

                options_list.append({
                    "text":options_data.text,
                    "node_id":child_node.id
                })
            node.options = options_list

        db.flush()
        return node    