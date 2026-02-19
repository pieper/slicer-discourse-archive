---
topic_id: 14133
title: "Getting An Error Running Extractskin Py"
date: 2020-10-19
url: https://discourse.slicer.org/t/14133
---

# Getting an error running ExtractSkin.py

**Topic ID**: 14133
**Date**: 2020-10-19
**URL**: https://discourse.slicer.org/t/getting-an-error-running-extractskin-py/14133

---

## Post #1 by @snish1 (2020-10-19 12:17 UTC)

<p>Operating system:Windows10<br>
Slicer version:4.1120200930</p>
<p>Hi.<br>
I am a novice and learning scripting slicer.<br>
I copied lassoan’s  ExtractSkin.py  to Python Interactor and got Error for line 41:</p>
<blockquote>
<blockquote>
<blockquote>
<p>surfaceMesh = segmentationNode.GetClosedSurfaceRepresentation(addedSegmentID)</p>
</blockquote>
</blockquote>
</blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
TypeError: GetClosedSurfaceRepresentation() takes exactly 2 arguments (1 given)</p>
<p>Is there any preparation I need before running the example?</p>

---

## Post #2 by @Sunderlandkyl (2020-10-19 13:11 UTC)

<p>There were some updates to the way representation access was handled from segmentation nodes in 4.11. It looks like ExtractSkin.py hasn’t been updated.</p>
<p>If you replace the line with the following, it should work as intended:</p>
<p><code>surfaceMesh = segmentationNode.GetClosedSurfaceInternalRepresentation(addedSegmentID)</code></p>

---

## Post #3 by @lassoan (2020-10-19 13:21 UTC)

<p>Thanks <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, I’ve updated the script.</p>

---

## Post #4 by @snish1 (2020-10-22 02:47 UTC)

<p>Thank you. It worked perfectly.</p>

---
