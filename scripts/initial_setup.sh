#!/bin/bash
# Run this once to do the initial full archive.
# Requires: DISCOURSE_API_KEY and DISCOURSE_API_USERNAME env vars (or pass --api-key / --api-username).

set -e

echo "Installing Python dependencies..."
pip install requests

echo "Running initial archive (this may take a long time for a full forum)..."
python scripts/fetch_discourse.py \
  --url https://discourse.slicer.org \
  --target-dir ./archive \
  --full \
  --debug

echo "Post-processing..."
python scripts/post_process.py

echo "Creating initial commit..."
git add archive/
git commit -m "Initial Discourse archive - $(date +'%Y-%m-%d')"

echo "Done! Push to GitHub to enable automatic updates."
