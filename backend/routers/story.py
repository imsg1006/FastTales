import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends , Cookie , Response , BackgroundTasks
from sqlalchemy.orm import Session

from  db.database import get_db , SessionLocal
from  models.story import Story,StoryNode
from  models.job import StoryJob
from  schemas.story import (
    CompleteStoryNodeResponse , CompleteStoryResponse , CreateStoryRequest
)
from  schemas.job import StoryJobResponse
from core.story_generator import StoryGenerator

router = APIRouter(
    prefix="/stories",
    tags=["stories"],      # API endpoint prefix and tag for story-related operations
)

def get_session_id(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        session_id = str(uuid.uuid4())
    return session_id                    # Generate a new session ID if not provided

@router.post(path="/create", response_model=StoryJobResponse)
def create_story(
    request: CreateStoryRequest,
    background_tasks: BackgroundTasks,
    response: Response,
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db)
):
    response.set_cookie(key="session_id", value=session_id, httponly=True) # Set session ID in the response cookie

    job_id=str(uuid.uuid4())
      # <-- Make sure this is a string, not None!
    job = StoryJob( 
    id=str(uuid.uuid4()),
    job_id=job_id,
    session_id=session_id,
    theme=request.theme,
    status="pending",
    )

    db.add(job)  # Add the job to the database
    db.commit()  # Commit the transaction to save the job 

    background_tasks.add_task(
        generate_story_task,
        job_id=job_id,  # Pass the SAME job_id
        session_id=session_id,
        theme=request.theme
    )

    return job  # Return the job details

def generate_story_task(job_id: str, session_id: str, theme: str):
    db = SessionLocal()

    try:
        job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()
        
        if not job: 
            return
        
        try:
            job.status = "processing"
            db.commit()  # Commit the status change to the database

            story = StoryGenerator.generate_story(db, session_id,theme)

            job.story_id = story.id # Placeholder for story ID, should be generated or fetched from the database
            job.status = "completed"
            job.completed_at = datetime.now()
            db.commit()  # Commit the status change to the database
        except Exception as e:
            job.status = "failed"
            job.completed_at = datetime.now()
            job.error = str(e)
            db.commit()  # Commit the status change to the database
    finally:
        db.close()

@router.get(path="/{story_id}", response_model=CompleteStoryResponse)
def get_complete_story(story_id: int, db: Session = Depends(get_db)):
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    complete_story = build_complete_story_tree(db,story)
    return complete_story

def build_complete_story_tree(db : Session,story : Story) -> CompleteStoryResponse:
    nodes = db.query(StoryNode).filter(StoryNode.story_id == story.id).all()

    node_dict = {}
    for node in nodes:
        node_response = CompleteStoryNodeResponse(
            id=node.id,
            content=node.content,
            is_ending=node.is_ending,
            is_winning_ending=node.is_winning_ending,
            options=node.options
        )
        node_dict[node.id] = node_response

    root_node = next((node for node in nodes if node.is_root), None)
    if not root_node:
        raise HTTPException(status_code=500, detail="Root node not found")
    
    return CompleteStoryResponse(
        id=story.id,
        title=story.title,
        session_id=story.session_id,
        created_at=story.created_at,
        root_node=node_dict[root_node.id],
        all_nodes=node_dict
    )