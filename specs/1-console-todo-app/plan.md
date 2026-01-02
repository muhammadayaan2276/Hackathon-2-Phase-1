# Implementation Plan: In-Memory Python Console-Based Todo App (Phase I)

**Branch**: `1-console-todo-app` | **Date**: 2026-01-02 | **Spec**: [./spec.md](./spec.md)
**Input**: Feature specification from `specs/1-console-todo-app/spec.md` and user prompt for `/sp.plan`.

## Summary
This plan outlines the technical approach for creating a command-line todo application using in-memory data structures, based on the user's provided architecture. The application will support full CRUD functionality and will be built in Python, aligning with Phase I of the project constitution. The architecture will emphasize a clean separation of concerns, with a single entry point, a clear data model, and distinct modules for core operations.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (using only standard library)
**Storage**: In-memory Python list of dictionaries or dataclasses.
**Testing**: pytest
**Target Platform**: Console (CLI)
**Project Type**: Single project
**Performance Goals**: N/A for this phase.
**Constraints**: Must run with `uv` in a standard Python environment. No external libraries for core logic. Data is ephemeral.
**Scale/Scope**: A single user's session.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Simplicity First**: ✅ PASS. This phase uses only in-memory logic and avoids any premature complexity, adhering to the user's simple architectural proposal.
- **II. Correctness and Integrity**: ✅ PASS. The plan includes separate modules for logic, which will contain input validation and error handling.
- **III. Modular Architecture**: ✅ PASS. The proposed structure with `main.py`, `models.py`, `service.py`, and `cli.py` enforces a clear separation of concerns as requested.
- **IV. Code Readability**: ✅ PASS. The code will follow standard Python conventions and be structured for clarity in distinct modules.
- **V. Production-Ready Phases**: ✅ PASS. This phase is a well-defined, runnable starting point for future enhancements.

All gates pass. No violations to report.

## Project Structure

### Documentation (this feature)

```text
specs/1-console-todo-app/
├── plan.md              # This file
├── data-model.md        # To be created
├── quickstart.md        # To be created
└── tasks.md             # To be created by /sp.tasks
```

### Source Code (repository root)
```text
src/
├── todo/
│   ├── __init__.py
│   ├── models.py      # Contains the TodoItem data model (dataclass)
│   ├── service.py     # Business logic for managing todos (add, update, etc.)
│   └── cli.py         # Handles all console I/O and command routing
└── main.py            # Application entry point

tests/
└── unit/
    ├── test_models.py
    └── test_service.py
```

**Structure Decision**: The "Single project" structure is selected. The architecture follows the user's request, with a `main.py` entry point that delegates to `todo/cli.py` for command handling. The business logic is isolated in `todo/service.py`, and the data structure is defined in `todo/models.py`. This provides a clean separation of concerns.

## Complexity Tracking
N/A. No constitutional violations.