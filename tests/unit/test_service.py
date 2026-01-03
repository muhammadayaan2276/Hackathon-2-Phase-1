import pytest
from src.todo.service import TodoService
from src.todo.models import TodoItem

@pytest.fixture
def service():
    """Provides a fresh TodoService instance for each test."""
    return TodoService()

def test_add_todo(service):
    """Test adding a single todo item."""
    todo = service.add_todo("Test Title", "Test Description")
    assert todo.id == 1
    assert todo.title == "Test Title"
    assert todo.description == "Test Description"
    assert not todo.completed
    assert len(service.get_all_todos()) == 1

def test_add_todo_no_description(service):
    """Test adding a todo item without a description."""
    todo = service.add_todo("Another Todo")
    assert todo.id == 1
    assert todo.title == "Another Todo"
    assert todo.description is None
    assert not todo.completed
    assert len(service.get_all_todos()) == 1

def test_add_todo_empty_title_raises_error(service):
    """Test that adding a todo with an empty title raises a ValueError."""
    with pytest.raises(ValueError, match="Title cannot be empty."):
        service.add_todo("", "Description")
    assert len(service.get_all_todos()) == 0

def test_get_all_todos_empty(service):
    """Test retrieving all todos when none have been added."""
    assert service.get_all_todos() == []

def test_get_all_todos_multiple(service):
    """Test retrieving multiple todo items."""
    service.add_todo("Todo 1")
    service.add_todo("Todo 2")
    todos = service.get_all_todos()
    assert len(todos) == 2
    assert todos[0].title == "Todo 1"
    assert todos[1].title == "Todo 2"

def test_mark_todo_complete_success(service):
    """Test marking an existing todo as complete."""
    todo = service.add_todo("Finish report")
    assert not todo.completed
    
    assert service.mark_todo_complete(todo.id)
    assert service.get_all_todos()[0].completed

def test_mark_todo_complete_not_found(service):
    """Test marking a non-existent todo as complete."""
    service.add_todo("Existing todo")
    assert not service.mark_todo_complete(999) # Non-existent ID
    assert not service.get_all_todos()[0].completed # Should remain incomplete

def test_mark_todo_incomplete_success(service):
    """Test marking an existing todo as incomplete."""
    todo = service.add_todo("Start report")
    service.mark_todo_complete(todo.id) # Mark it complete first
    assert service.get_all_todos()[0].completed

    assert service.mark_todo_incomplete(todo.id)
    assert not service.get_all_todos()[0].completed

def test_mark_todo_incomplete_not_found(service):
    """Test marking a non-existent todo as incomplete."""
    todo = service.add_todo("Existing todo")
    service.mark_todo_complete(todo.id) # Mark it complete first
    assert service.get_all_todos()[0].completed == True # Ensure it's complete

    assert not service.mark_todo_incomplete(999) # Try to mark a non-existent ID incomplete, should return False
    assert service.get_all_todos()[0].completed == True # It should *still* be complete

def test_update_todo_title(service):
    """Test updating only the title of a todo."""
    todo = service.add_todo("Old Title", "Old Desc")
    assert service.update_todo(todo.id, new_title="New Title")
    updated_todo = service.get_all_todos()[0]
    assert updated_todo.title == "New Title"
    assert updated_todo.description == "Old Desc"

def test_update_todo_description(service):
    """Test updating only the description of a todo."""
    todo = service.add_todo("Title", "Old Desc")
    assert service.update_todo(todo.id, new_description="New Desc")
    updated_todo = service.get_all_todos()[0]
    assert updated_todo.title == "Title"
    assert updated_todo.description == "New Desc"

def test_update_todo_both(service):
    """Test updating both title and description of a todo."""
    todo = service.add_todo("Old Title", "Old Desc")
    assert service.update_todo(todo.id, new_title="New Title", new_description="New Desc")
    updated_todo = service.get_all_todos()[0]
    assert updated_todo.title == "New Title"
    assert updated_todo.description == "New Desc"

def test_update_todo_clear_description(service):
    """Test clearing the description of a todo."""
    todo = service.add_todo("Title", "Existing Desc")
    assert service.update_todo(todo.id, new_description="") # Empty string clears it
    updated_todo = service.get_all_todos()[0]
    assert updated_todo.description == ""

def test_update_todo_not_found(service):
    """Test updating a non-existent todo."""
    service.add_todo("Existing todo")
    assert not service.update_todo(999, new_title="NonExistent") # Non-existent ID
    assert service.get_all_todos()[0].title == "Existing todo" # Should remain unchanged

def test_update_todo_empty_title_raises_error(service):
    """Test that updating a todo with an empty title raises a ValueError."""
    todo = service.add_todo("Valid Title")
    with pytest.raises(ValueError, match="Title cannot be empty."):
        service.update_todo(todo.id, new_title="")
    assert service.get_all_todos()[0].title == "Valid Title" # Title should not change

def test_delete_todo_success(service):
    """Test deleting an existing todo."""
    todo1 = service.add_todo("Todo 1")
    todo2 = service.add_todo("Todo 2")
    assert len(service.get_all_todos()) == 2
    
    assert service.delete_todo(todo1.id)
    assert len(service.get_all_todos()) == 1
    assert service.get_all_todos()[0].id == todo2.id

def test_delete_todo_not_found(service):
    """Test deleting a non-existent todo."""
    service.add_todo("Existing todo")
    assert len(service.get_all_todos()) == 1
    assert not service.delete_todo(999) # Non-existent ID
    assert len(service.get_all_todos()) == 1 # Should remain unchanged
