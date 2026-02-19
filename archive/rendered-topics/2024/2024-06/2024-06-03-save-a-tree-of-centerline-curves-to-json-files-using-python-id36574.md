---
topic_id: 36574
title: "Save A Tree Of Centerline Curves To Json Files Using Python"
date: 2024-06-03
url: https://discourse.slicer.org/t/36574
---

# Save a tree of centerline curves to json files using Python

**Topic ID**: 36574
**Date**: 2024-06-03
**URL**: https://discourse.slicer.org/t/save-a-tree-of-centerline-curves-to-json-files-using-python/36574

---

## Post #1 by @ruili (2024-06-03 14:32 UTC)

<p>Hello,</p>
<p>I have created a tree of centerline curves using functions from the “Extract Centerline” module, and now I want to save the curves in a file structure that can reflect the tree structure. In Slicer, I can do this by right click the stem curve → “Export to file…” → Check all the options.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3d0d76a91429a4225d31bb63afcae66ceecc7a7.png" alt="Screenshot 2024-06-03 at 15.24.27" data-base62-sha1="pEIUikR3GyeRV4F2c2TPGCVyFy7" width="572" height="278"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef7b2021893f7d665d165ef0f2a4e1f418ad36c3.png" alt="Screenshot 2024-06-03 at 15.25.01" data-base62-sha1="yaxUsswzeQ4lQ3cIeLny79UoTTR" width="453" height="276"></p>
<p>This will save my curves in a folder structure that looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e1a0a01b2220ba9499f865db075023d56ea8b5c.png" data-download-href="/uploads/short-url/hZxWSTRvmI9WuLGYrPGloPLpJ5G.png?dl=1" title="Screenshot 2024-06-03 at 15.31.09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e1a0a01b2220ba9499f865db075023d56ea8b5c_2_297x500.png" alt="Screenshot 2024-06-03 at 15.31.09" data-base62-sha1="hZxWSTRvmI9WuLGYrPGloPLpJ5G" width="297" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e1a0a01b2220ba9499f865db075023d56ea8b5c_2_297x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e1a0a01b2220ba9499f865db075023d56ea8b5c_2_445x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e1a0a01b2220ba9499f865db075023d56ea8b5c.png 2x" data-dominant-color="F1F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-06-03 at 15.31.09</span><span class="informations">524×880 66.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now I wonder if there is a python command to do this easily as well? It will be great to add this to my automatic code that runs the centerline extraction.</p>
<p>Many thanks!</p>

---

## Post #2 by @lassoan (2024-06-03 15:41 UTC)

<p>This <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-files-to-directory-structure-matching-subject-hierarchy-folders">code snippet in the script repository</a> implements what you described.</p>

---
