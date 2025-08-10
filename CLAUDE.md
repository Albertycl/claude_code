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