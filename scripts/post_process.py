#!/usr/bin/env python3
"""
Post-process archived Discourse content:
- Create category-based organization
- Add YAML frontmatter to markdown files
- Create search-friendly structure
"""

import json
import re
from pathlib import Path
from datetime import datetime

ARCHIVE_DIR = Path("archive")
POSTS_DIR = ARCHIVE_DIR / "posts"
TOPICS_DIR = ARCHIVE_DIR / "rendered-topics"

def extract_frontmatter(md_file):
    """Extract metadata from filename and add YAML frontmatter."""
    try:
        content = md_file.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {md_file}: {e}")
        return
    
    # Skip if already has frontmatter
    if content.startswith('---'):
        return
    
    # Parse filename: YYYY-MM-DD-title-idNNN.md
    filename = md_file.stem
    match = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)-id(\d+)', filename)
    
    if not match:
        return
    
    date, title, topic_id = match.groups()
    title_clean = title.replace('-', ' ').title()
    
    # Add frontmatter
    frontmatter = f"""---
topic_id: {topic_id}
title: "{title_clean}"
date: {date}
url: https://discourse.slicer.org/t/{topic_id}
---

"""
    
    try:
        md_file.write_text(frontmatter + content, encoding='utf-8')
        print(f"Added frontmatter to: {md_file.name}")
    except Exception as e:
        print(f"Error writing {md_file}: {e}")

def organize_by_category():
    """Organize topics by extracting category hints from content."""
    if not TOPICS_DIR.exists():
        print(f"Topics directory does not exist: {TOPICS_DIR}")
        return
    
    for md_file in TOPICS_DIR.rglob("*.md"):
        if md_file.name == "README.md":
            continue
        extract_frontmatter(md_file)

def create_category_indexes():
    """Create README files for each year/month directory."""
    if not TOPICS_DIR.exists():
        print(f"Topics directory does not exist: {TOPICS_DIR}")
        return
    
    for year_month_dir in sorted(TOPICS_DIR.glob("*/*")):
        if not year_month_dir.is_dir():
            continue
        
        readme = year_month_dir / "README.md"
        topics = sorted(year_month_dir.glob("*.md"))
        
        if not topics:
            continue
        
        # Filter out existing README
        topics = [t for t in topics if t.name != "README.md"]
        
        if not topics:
            continue
        
        try:
            with open(readme, 'w') as f:
                f.write(f"# Topics from {year_month_dir.name}\n\n")
                
                for topic in topics:
                    title = topic.stem.split('-id')[0].replace('-', ' ').title()
                    f.write(f"- [{title}]({topic.name})\n")
            
            print(f"Created index: {readme}")
        except Exception as e:
            print(f"Error creating index {readme}: {e}")

if __name__ == "__main__":
    print("Post-processing archive...")
    organize_by_category()
    create_category_indexes()
    print("Done!")
