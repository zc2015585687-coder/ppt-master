#!/usr/bin/env python3
"""
PPT Master - Project Management Paths

Own the repository and Skill resource roots used by project-management modules.

Usage:
    Import the required path constants from project_management.paths.

Examples:
    from project_management.paths import PROJECTS_ROOT, SCHEMA_DIR

Dependencies:
    None (only uses the standard library)
"""

from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = PACKAGE_DIR.parent
SKILL_DIR = SCRIPTS_DIR.parent
REPO_ROOT = SKILL_DIR.parent.parent
# Generated presentation projects belong to the caller's active workspace by
# default. Skill resources still resolve from SKILL_DIR/REPO_ROOT, while an
# explicit ``project_manager.py init --dir ...`` continues to override this
# default at the CLI layer.
PROJECTS_ROOT = Path.cwd() / "projects"
SOURCE_TO_MD_DIR = SCRIPTS_DIR / "source_to_md"
CHARTS_DIR = SKILL_DIR / "templates" / "charts"
SCHEMA_DIR = SKILL_DIR / "templates" / "schemas"
SCAFFOLD_DIR = SKILL_DIR / "templates" / "scaffolds"
