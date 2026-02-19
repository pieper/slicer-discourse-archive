---
topic_id: 20409
title: "How To Update Slicers Python Version From 3 6 7 To 3 7"
date: 2021-10-28
url: https://discourse.slicer.org/t/20409
---

# How to update Slicer's Python version from 3.6.7 to 3.7?

**Topic ID**: 20409
**Date**: 2021-10-28
**URL**: https://discourse.slicer.org/t/how-to-update-slicers-python-version-from-3-6-7-to-3-7/20409

---

## Post #1 by @andieku (2021-10-28 23:44 UTC)

<p>Hi, is there a way to upgrade my Slicer’s (v. 4.11) Python version from 3.6.7 to 3.7 (or newer) without updating the slicer itself? I would like to use skimage’s <a href="https://scikit-image.org/docs/0.18.x/api/skimage.segmentation.html#expand-labels" rel="noopener nofollow ugc"><code>skimage.segmentation.expand_labels()</code></a> function and it requires Python version 3.7 or higher. Thank you!</p>

---

## Post #2 by @jamesobutler (2021-10-29 00:39 UTC)

<p>Updating the Python version is something we’ve been tracking for awhile now at <a href="https://github.com/Slicer/Slicer/issues/5014" class="inline-onebox" rel="noopener nofollow ugc">Update Python version from 3.6.7 to 3.10 · Issue #5014 · Slicer/Slicer · GitHub</a>. Since some python packages are already dropping support for Python 3.7, plans are to upgrade to one of the most recent versions Python.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you or others at Kitware have this scheduled for work soon? I assume it will be completed as part of <a href="https://github.com/Slicer/Slicer/issues/5956" class="inline-onebox" rel="noopener nofollow ugc">Update VTK9 to the latest master · Issue #5956 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #3 by @lassoan (2021-10-29 02:36 UTC)

<p>We’ll update Slicer’s Python, but if your main motivation is to use skimage then you don’t need to wait for that update. skimage is OK for really basic stuff, but you need much more if you work biomedical images.</p>
<p>For example, this <code>skimage.segmentation.expand_labels</code> function takes a <em>single</em> distance value in <em>pixels</em>. This is completely unusable for medical imaging, where images are most often 3D and have anisotropic spacing. If a label expansion filter only supports expansion by the same distance in all directions (which may make sense) then that distance must be specified in physical distance unit, not in pixels.</p>
<p>I would recommend to use SimpleITK for image processing, as it exposes most ITK features with a nice Pythonic interface. Latest version of SimpleITK is already bundled with Slicer. ITK-Python packages may work in Slicer, too (it is a different Python wrapping of ITK).</p>

---

## Post #4 by @andieku (2021-10-29 22:39 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your suggestions! I will definitely take a look at SimpleITK.</p>

---
