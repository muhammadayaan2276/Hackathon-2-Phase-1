# Data Model: Todo App

This document outlines the data structures for the In-Memory Python Console-Based Todo App.

## Entities

### TodoItem

Represents a single task in the todo list. A Python dataclass is recommended for implementation.

**Fields**:

- **id** (integer): A unique, auto-incrementing identifier for the todo item.
- **title** (string): The main title or summary of the task. Cannot be empty.
- **description** (string, optional): A more detailed description of the task. Can be empty.
- **completed** (boolean): The status of the task. Defaults to `False` upon creation.

**Validation Rules**:

- The `title` field must not be an empty string.
- The `id` must be unique across all todos.

**State Transitions**:

- A `TodoItem` is created with `completed` as `False`.
- The `completed` status can transition from `False` to `True`.
- The `title` and `description` can be updated at any time.
