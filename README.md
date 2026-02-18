# Slicer Discourse Archive

Automated archive of the [3D Slicer Discourse forum](https://discourse.slicer.org).

## 📦 What's in this repository

This repository contains a searchable archive of Slicer Discourse discussions, automatically updated daily via GitHub Actions.

### Structure

- `archive/posts/` - Individual posts in JSON format, organized by date
- `archive/rendered-topics/` - Complete discussion threads rendered as Markdown
- `archive/INDEX.md` - Searchable index of all archived content

## 🔍 How to search

### Using GitHub's search

Press `/` and search for topics, APIs, or code patterns:
- `GetIJKToRASMatrix` - Find coordinate transform discussions
- `vtkMRMLScalarVolumeNode` - Find volume node usage
- `python scripting` - Find Python-related threads

### Using git grep locally

```bash
# Clone the archive
git clone https://github.com/YOUR_USERNAME/slicer-discourse-archive
cd slicer-discourse-archive

# Search for API usage
grep -r "slicer.util.loadVolume" archive/rendered-topics/

# Find geometry-related discussions
grep -r "IJKToRAS" archive/rendered-topics/ -l

# Search posts by user
grep -r "@pieper" archive/posts/
```

### For use with Claude Code

Add to your Slicer project's `.claude/SLICER_SKILL.md`:

```markdown
## Discourse Knowledge Base

Before writing Slicer code, search the archived Discourse forum:

\`\`\`bash
# Clone archive (once)
git clone https://github.com/YOUR_USERNAME/slicer-discourse-archive ~/slicer-discourse-archive

# Search for patterns
grep -r "coordinate transform" ~/slicer-discourse-archive/archive/rendered-topics/ -A 5

# Read specific discussion
view ~/slicer-discourse-archive/archive/rendered-topics/2024-03-March/2024-03-15-coordinate-systems-id1234.md
\`\`\`

Update the archive: `cd ~/slicer-discourse-archive && git pull`
```

## 🤖 Automation

This archive updates automatically via GitHub Actions:
- **Schedule**: Daily at 3:00 AM UTC
- **Manual**: Click "Actions" → "Archive Slicer Discourse" → "Run workflow"

## 📊 Statistics

See [archive/INDEX.md](archive/INDEX.md) for:
- Total archived posts and topics
- Recently updated discussions
- Archive coverage timeline

## ⚙️ Setup (for your own Discourse)

To archive a different Discourse forum:

1. Fork this repository
2. Edit `.github/workflows/archive-discourse.yml`:
   ```yaml
   --url https://YOUR-DISCOURSE-URL.org \
   ```
3. Enable GitHub Actions in your fork
4. Trigger a manual run to start the archive

## 🚀 Quick Start

### Option 1: Let GitHub Actions do the work

1. Push this repository to GitHub
2. Go to Actions tab and enable workflows
3. Click "Run workflow" to start the initial archive
4. Wait for it to complete (first run may take 30-60 minutes)

### Option 2: Run initial archive locally

```bash
# Make script executable
chmod +x scripts/initial_setup.sh

# Run initial archive (requires Python 3.11+)
./scripts/initial_setup.sh

# Push to GitHub
git push
```

## 📝 License

Archive content is subject to the [Discourse forum's terms](https://discourse.slicer.org/tos).
Archiving scripts are MIT licensed.

## 🔗 Links

- [Live Slicer Discourse](https://discourse.slicer.org)
- [discourse-archive tool](https://github.com/jamesob/discourse-archive)
- [3D Slicer homepage](https://www.slicer.org)

## 🛠️ Troubleshooting

### GitHub Action fails on first run

This is normal if the archive directory doesn't exist yet. The action will create it on the first successful run.

### Large repository size

Discourse archives can grow large over time. Consider:
- Running periodic cleanup of very old content
- Using Git LFS for large archives
- Archiving only specific categories

### Rate limiting

The discourse-archive tool respects API rate limits. If you see rate limit errors, the script will automatically retry with exponential backoff.
