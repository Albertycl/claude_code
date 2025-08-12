# standard workflow
1. First think through the problem, read the codebase for relevant files, and write a plan to tasks/todo.md.
2. The plan should have a list of todo items that you can check off as you complete them
3. Before you begin working, check in with me and I will verify the plan.
4. Then, begin working on the todo items, marking them as complete as you go.
5. Please every step of the way just give me a high level explanation of what changes you made
6. Make every task and code change you do as simple as possible. We want to avoid making any massive or complex changes. Every change should impact as little code as possible. Everything is about simplicity.
7. Finally, add a review section to the [todo.md](http://todo.md/) file with a summary of the changes you made and any other relevant information.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current State

This is a minimal learning environment for experimenting with Claude Code. The repository currently contains:
- `hi.txt` - Simple text file
- `.claude/settings.local.json` - Claude Code permissions (allows basic file operations)

## Development Setup

No project framework is currently established. This is a blank slate suitable for:
- Learning Claude Code capabilities
- Experimenting with different project types
- Setting up new projects from scratch

## Version Control

This directory is not currently a git repository. Initialize git if you plan to track changes:
```bash
git init
```

## Permissions

Claude Code is configured with minimal permissions:
- `Bash(find:*)` - File finding operations
- `Bash(ls:*)` - Directory listing operations

Additional permissions may need to be granted for more complex development tasks.

## Future Development

When setting up a new project in this directory:
1. Determine the project type and initialize appropriate structure
2. Set up version control if needed
3. Create relevant configuration files (package.json, requirements.txt, etc.)
4. Update this CLAUDE.md with project-specific information