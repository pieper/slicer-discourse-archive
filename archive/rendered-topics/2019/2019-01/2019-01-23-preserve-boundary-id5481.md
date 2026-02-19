---
topic_id: 5481
title: "Preserve Boundary"
date: 2019-01-23
url: https://discourse.slicer.org/t/5481
---

# Preserve boundary

**Topic ID**: 5481
**Date**: 2019-01-23
**URL**: https://discourse.slicer.org/t/preserve-boundary/5481

---

## Post #1 by @anandmulay3 (2019-01-23 11:11 UTC)

<p>can we add a function which help us to preserve boundary while applying decimation on model .</p>

---

## Post #2 by @lassoan (2019-01-23 18:43 UTC)

<p>There are a number of options to control what points are removed during decimation - see details in the filter’s documentation: <a href="https://vtk.org/doc/nightly/html/classvtkDecimatePro.html" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkDecimatePro.html</a></p>
<p>Some of these options are exposed in Surface Toolbox module, but if you find additional options that would be useful to make adjustable by users then let us know.</p>

---

## Post #3 by @anandmulay3 (2019-01-24 11:32 UTC)

<p>fantastic!  Surface toolbox is the thing i was looking for , tested in slicer editor its working as expected.<br>
How can i call it using my scriptableModule script?</p>
<p>Edit: I got the code in reference , though you can drop me a snippet , may be it comes better than what i have now.</p>
<p>Thanks a ton</p>

---

## Post #4 by @lassoan (2019-01-24 14:05 UTC)

<p>Surface toolbox is a Python scripted module, so just click “Edit” button to see/edit its source code (if you don’t see the button then enable Developer mode in application settings). If Edit does not bring up the source code then search SurfaceToolbox.py file manually.</p>

---

## Post #5 by @lassoan (2023-03-21 03:07 UTC)



---
