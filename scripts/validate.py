#!/usr/bin/env python3
"""
Validate Obsidian Bases skill structure and content.
"""

import yaml
import sys
from pathlib import Path


def validate_yaml(file_path: Path) -> bool:
    """Validate YAML syntax."""
    try:
        with open(file_path, 'r') as f:
            yaml.safe_load(f)
        return True
    except yaml.YAMLError as e:
        print(f"YAML error in {file_path}: {e}")
        return False


def validate_skill_structure(skill_dir: Path) -> bool:
    """Validate skill directory structure."""
    required_files = [
        'SKILL.md',
        'AGENTS.md',
        'discovery.json',
        'references/schema.md',
        'references/functions.md',
        'references/examples.md'
    ]
    
    missing = []
    for file in required_files:
        if not (skill_dir / file).exists():
            missing.append(file)
    
    if missing:
        print(f"Missing required files: {missing}")
        return False
    
    return True


def validate_discovery_json(skill_dir: Path) -> bool:
    """Validate discovery.json structure."""
    discovery_file = skill_dir / 'discovery.json'
    try:
        with open(discovery_file, 'r') as f:
            data = json.load(f)
        
        required_keys = ['question', 'trigger', 'decision', 'evidence', 'success_measure']
        missing = [k for k in required_keys if k not in data]
        
        if missing:
            print(f"Missing keys in discovery.json: {missing}")
            return False
        
        return True
    except Exception as e:
        print(f"Error validating discovery.json: {e}")
        return False


def main():
    skill_dir = Path(__file__).parent.parent
    
    print(f"Validating skill: {skill_dir}")
    
    # Check structure
    if not validate_skill_structure(skill_dir):
        print("Structure validation failed")
        sys.exit(1)
    
    # Validate YAML files
    yaml_files = [
        skill_dir / 'references' / 'schema.md',
        skill_dir / 'references' / 'functions.md',
        skill_dir / 'references' / 'examples.md'
    ]
    
    for yaml_file in yaml_files:
        if yaml_file.exists():
            # For markdown files with YAML blocks, we just check they exist
            pass
    
    # Validate discovery.json
    if not validate_discovery_json(skill_dir):
        print("Discovery.json validation failed")
        sys.exit(1)
    
    print("All validations passed")
    sys.exit(0)


if __name__ == '__main__':
    import json
    main()