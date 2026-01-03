# Tasks: In-Memory Python Console-Based Todo App (Phase I)

**Input**: Design documents from `specs/1-console-todo-app/`
**Prerequisites**: plan.md, spec.md, data-model.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to

## Path Conventions
Paths assume a single project structure as defined in `plan.md`.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [x] T001 Create the initial directory structure: `src/todo/`, `tests/unit/`
- [x] T002 Create empty Python package file `src/todo/__init__.py`
- [x] T003 Create main application entry point file `src/main.py`
- [x] T004 Create a `pyproject.toml` file to manage project dependencies (e.g., pytest).

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data model and service structure.

- [x] T005 Define the `TodoItem` dataclass in `src/todo/models.py` based on `data-model.md`.
- [x] T006 [P] Create the `TodoService` class in `src/todo/service.py` with an in-memory list for storage.
- [x] T007 [P] Create the basic CLI structure and menu loop in `src/todo/cli.py`.

---

## Phase 3: User Story 1 - Add a Todo (Priority: P1) 🎯 MVP

**Goal**: Allow a user to add a new todo item.
**Independent Test**: Run the app, add a todo, and see it appear in the list.

### Implementation for User Story 1
- [x] T008 [US1] Implement the `add_todo` method in the `TodoService` class in `src/todo/service.py`. It should accept a title and optional description, and add a new `TodoItem` to the in-memory list.
- [x] T009 [US1] Implement the CLI prompt and input handling for adding a new todo in `src/todo/cli.py`. This task depends on T008.

---

## Phase 4: User Story 2 - View All Todos (Priority: P1)

**Goal**: Allow a user to see all their todo items.
**Independent Test**: Add multiple todos and see them all displayed correctly.

### Implementation for User Story 2
- [x] T010 [US2] Implement the `get_all_todos` method in `src/todo/service.py` that returns the full list of todos.
- [x] T011 [US2] Implement the CLI display logic for showing all todos in `src/todo/cli.py`. This task depends on T010.

---

## Phase 5: User Story 3 - Mark a Todo as Complete (Priority: P2)

**Goal**: Allow a user to mark a todo as complete.
**Independent Test**: Add a todo, mark it complete, and verify its status changes when viewed.

### Implementation for User Story 3
- [x] T012 [US3] Implement the `mark_todo_complete` method in `src/todo/service.py` that finds a todo by its ID and sets its `completed` status to `True`.
- [x] T013 [US3] Implement the CLI interaction for marking a todo as complete in `src/todo/cli.py`. This task depends on T012.

---

## Phase 6: User Story 4 - Mark a Todo as Incomplete

**Goal**: Allow a user to mark a todo as incomplete.
**Independent Test**: Add a todo, mark it complete, then mark it incomplete, and verify its status changes when viewed.

### Implementation for User Story 4
- [x] T022 [US4] Implement the `mark_todo_incomplete` method in `src/todo/service.py` that finds a todo by its ID and sets its `completed` status to `False`.
- [x] T023 [US4] Implement the CLI interaction for marking a todo as incomplete in `src/todo/cli.py`. This task depends on T022.

---

## Phase 7: User Story 5 - Update a Todo (Priority: P3)

### Implementation for User Story 5
- [x] T014 [US5] Implement the `update_todo` method in `src/todo/service.py` to find a todo by ID and update its title and/or description.
- [x] T015 [US5] Implement the CLI interaction for updating a todo in `src/todo/cli.py`. This task depends on T014.

---

## Phase 8: User Story 6 - Delete a Todo (Priority: P3)

**Goal**: Allow a user to remove a todo from their list.
**Independent Test**: Add a todo, delete it, and verify it is gone from the list.

### Implementation for User Story 6
- [x] T016 [US6] Implement the `delete_todo` method in `src/todo/service.py` to remove a todo by its ID.
- [x] T017 [US6] Implement the CLI interaction for deleting a todo in `src/todo/cli.py`. This task depends on T016.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Finalizing the application logic and ensuring quality.

- [x] T018 Integrate all service methods into the main application loop in `src/main.py` and `src/todo/cli.py`.
- [x] T019 Implement robust error handling for invalid user inputs (e.g., non-existent IDs, non-numeric input) in `src/todo/cli.py`.
- [x] T020 [P] Write unit tests for the `TodoItem` model in `tests/unit/test_models.py`.
- [x] T021 [P] Write unit tests for all public methods in the `TodoService` class in `tests/unit/test_service.py`.

---

## Dependencies & Execution Order

- **Setup (Phase 1)** must be completed first.
- **Foundational (Phase 2)** depends on Phase 1.
- All **User Stories (Phases 3-8)** depend on Phase 2. The user stories can be implemented sequentially in priority order (US1, US2, US3, US4, US5, US6) or in parallel if desired.
- **Polish (Phase 9)** should be done after all user story implementation is complete.
- Within each user story, the service method should be implemented before the CLI interaction.
- Unit tests can be written in parallel with the implementation of the code they are testing.

## Implementation Strategy

### MVP First (User Story 1 & 2)

1.  Complete Phase 1 & 2.
2.  Complete Phase 3 (Add Todo) & Phase 4 (View Todos).
3.  **STOP and VALIDATE**: The app is now a basic, functional MVP.

### Incremental Delivery

1.  Deliver MVP (Add/View).
2.  Add User Story 3 (Mark Complete).
3.  Add User Story 4 (Mark Incomplete).
4.  Add User Stories 5 & 6 (Update/Delete).
5.  Complete Polish phase.
