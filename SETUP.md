# Setup Instructions

Follow these steps to set up your Slicer Discourse archive on GitHub.

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Name it: `slicer-discourse-archive`
3. Make it **Public** (so the archive is searchable)
4. **Do NOT** initialize with README, .gitignore, or license
5. Click "Create repository"

## Step 2: Push This Code

```bash
# Extract the zip file you downloaded
unzip slicer-discourse-archive.zip
cd slicer-discourse-archive

# Initialize git
git init
git add .
git commit -m "Initial commit: Discourse archive setup"

# Connect to your GitHub repo (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/slicer-discourse-archive.git
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Actions

1. Go to your repository on GitHub
2. Click the **"Actions"** tab
3. Click **"I understand my workflows, go ahead and enable them"**

## Step 4: Run First Archive

### Option A: Automatic (via GitHub Actions)

1. In the Actions tab, click **"Archive Slicer Discourse"**
2. Click **"Run workflow"** dropdown
3. Click the green **"Run workflow"** button
4. Wait 30-60 minutes for first archive to complete
5. Refresh the page to see progress

### Option B: Manual (on your local machine)

```bash
# Make script executable
chmod +x scripts/initial_setup.sh scripts/post_process.py

# Install Python 3.11+ if needed
python3 --version

# Run the initial archive
./scripts/initial_setup.sh

# Push the archive to GitHub
git push
```

## Step 5: Verify Archive

After the workflow completes:

1. Go to your repo on GitHub
2. Browse to `archive/rendered-topics/`
3. You should see folders organized by date with .md files
4. Check `archive/INDEX.md` for statistics

## Step 6: Use with Claude Code

In your Slicer extension project (e.g., SlicerDMRI):

```bash
# Clone the archive locally
cd ~
git clone https://github.com/YOUR_USERNAME/slicer-discourse-archive

# Create Claude skill file
mkdir -p ~/SlicerDMRI/.claude
cat > ~/SlicerDMRI/.claude/SLICER_SKILL.md << 'EOF'
# Slicer Development Skill

## Knowledge Sources
- Slicer source: ~/Slicer
- Discourse archive: ~/slicer-discourse-archive

## Before Writing Code

1. Check API exists:
\`\`\`bash
grep -r "def functionName" ~/Slicer/Base/Python/slicer/
\`\`\`

2. Search Discourse for examples:
\`\`\`bash
grep -r "functionName" ~/slicer-discourse-archive/archive/rendered-topics/ -A 5
\`\`\`

3. Read relevant threads:
\`\`\`bash
view ~/slicer-discourse-archive/archive/rendered-topics/YYYY-MM-Month/topic.md
\`\`\`

## Update Archive
\`\`\`bash
cd ~/slicer-discourse-archive && git pull
\`\`\`
EOF
```

## Troubleshooting

### Workflow fails with "refusing to allow a GitHub App to create or update workflow"

This happens if you're using a fine-grained personal access token. Solutions:

1. **Recommended**: Use the default `GITHUB_TOKEN` (already configured in the workflow)
2. Go to Settings → Actions → General → Workflow permissions
3. Select "Read and write permissions"
4. Save

### Archive is empty after first run

- Check the Actions log for errors
- Common issue: Rate limiting (the tool will retry automatically)
- May need to run the workflow multiple times for a large forum

### Repository getting too large

Discourse archives can be several GB. Options:

1. Archive only recent content (modify the workflow to use date filters)
2. Use [Git LFS](https://git-lfs.github.com/) for large files
3. Archive only specific categories (modify `--url` to category URLs)

## Next Steps

- The archive will now update automatically every day at 3 AM UTC
- You can manually trigger updates anytime from the Actions tab
- Update your local copy with `git pull` whenever you need fresh data
- Use GitHub's search (press `/`) to find discussions across the entire archive

## Customization

### Archive a different Discourse forum

Edit `.github/workflows/archive-discourse.yml` line 33:
```yaml
--url https://YOUR-DISCOURSE.org \
```

### Change update frequency

Edit `.github/workflows/archive-discourse.yml` line 5:
```yaml
- cron: '0 3 * * *'  # Daily at 3 AM UTC
```

Common cron schedules:
- `0 */6 * * *` - Every 6 hours
- `0 2 * * 0` - Weekly on Sunday at 2 AM
- `0 3 1 * *` - Monthly on the 1st at 3 AM

### Archive only specific categories

Modify the archiver to use category-specific URLs. See the [discourse-archive documentation](https://github.com/jamesob/discourse-archive) for more options.
