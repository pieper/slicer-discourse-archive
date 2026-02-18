# How to use endoscopy in python

**Topic ID**: 15211
**Date**: 2020-12-24
**URL**: https://discourse.slicer.org/t/how-to-use-endoscopy-in-python/15211

---

## Post #1 by @yee_lu (2020-12-24 13:52 UTC)

<p>Now I have some txt files which have some centerline nodes，I want to generate endoscopy in  batch, how to use endoscopy in python?</p>

---

## Post #2 by @lassoan (2021-09-05 01:07 UTC)

<p>You can load a text file in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-json-file-format-mrk-json">json</a> format as a markups curve node (just change the <code>"type": "Fiducial"</code> to <code>"type": "Curve"</code>) and then use Endoscopy module to guide the renderer camera through the his trajectory. After each step, you can create a snapshot of the view and in the end merge them into a video using Screen Capture module.</p>

---
