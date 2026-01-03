from typing import List, Optional
from .models import TodoItem

class TodoService:
    """Manages the business logic for todo items."""
    def __init__(self):
        self._todos: List[TodoItem] = []
        self._next_id = 1

    def add_todo(self, title: str, description: Optional[str] = None) -> TodoItem:
        """Adds a new todo item."""
        if not title:
            raise ValueError("Title cannot be empty.")
        
        new_todo = TodoItem(
            id=self._next_id,
            title=title,
            description=description
        )
        self._todos.append(new_todo)
        self._next_id += 1
        return new_todo

    def get_all_todos(self) -> List[TodoItem]:
        """Returns all todo items."""
        return list(self._todos) # Return a copy to prevent external modification

    def mark_todo_complete(self, todo_id: int) -> bool:
        """
        Marks a todo item as complete.
        Returns True if the todo was found and updated, False otherwise.
        """
        for todo in self._todos:
            if todo.id == todo_id:
                todo.completed = True
                return True
        return False

    def mark_todo_incomplete(self, todo_id: int) -> bool:
        """
        Marks a todo item as incomplete.
        Returns True if the todo was found and updated, False otherwise.
        """
        for todo in self._todos:
            if todo.id == todo_id:
                todo.completed = False
                return True
        return False

    def update_todo(self, todo_id: int, new_title: Optional[str] = None, new_description: Optional[str] = None) -> bool:
        """
        Updates an existing todo item's title and/or description.
        Returns True if the todo was found and updated, False otherwise.
        Raises ValueError if new_title is an empty string.
        """
        for todo in self._todos:
            if todo.id == todo_id:
                if new_title is not None:
                    if not new_title:
                        raise ValueError("Title cannot be empty.")
                    todo.title = new_title
                if new_description is not None:
                    todo.description = new_description
                return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Deletes a todo item by its ID.
        Returns True if the todo was found and deleted, False otherwise.
        """
        original_len = len(self._todos)
        self._todos = [todo for todo in self._todos if todo.id != todo_id]
        return len(self._todos) < original_len
