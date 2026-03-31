from pydantic import BaseModel #type: ignore
from typing import List, Dict, Optional

class Lesson(BaseModel):
    lesson_id: int
    topic: str

class Module(BaseModel):
    module_id: int
    name:str
    lessons: List[Lesson]  # List of Lesson objects

class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]  # List of Module objects