import dataclasses
from typing import Optional

@dataclasses.dataclass
class TodoItem:
    """Represents a single task in the todo list."""
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
