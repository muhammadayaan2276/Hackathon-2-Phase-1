import pytest
from src.todo.models import TodoItem

def test_todo_item_creation():
    """Test that a TodoItem can be created correctly."""
    item = TodoItem(id=1, title="Buy groceries")
    assert item.id == 1
    assert item.title == "Buy groceries"
    assert item.description is None
    assert not item.completed

def test_todo_item_creation_with_description():
    """Test TodoItem creation with an optional description."""
    item = TodoItem(id=2, title="Read book", description="Chapter 5")
    assert item.id == 2
    assert item.title == "Read book"
    assert item.description == "Chapter 5"
    assert not item.completed

def test_todo_item_completed_status():
    """Test setting a TodoItem as completed."""
    item = TodoItem(id=3, title="Finish report", completed=True)
    assert item.id == 3
    assert item.title == "Finish report"
    assert item.completed

def test_todo_item_equality():
    """Test equality of TodoItem objects based on their attributes."""
    item1 = TodoItem(id=1, title="Task A", description="Desc A", completed=False)
    item2 = TodoItem(id=1, title="Task A", description="Desc A", completed=False)
    item3 = TodoItem(id=2, title="Task B", description="Desc B", completed=True)

    assert item1 == item2
    assert item1 != item3
    assert item2 != item3
