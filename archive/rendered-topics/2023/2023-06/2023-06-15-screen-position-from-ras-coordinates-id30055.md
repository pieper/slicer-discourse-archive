---
topic_id: 30055
title: "Screen Position From Ras Coordinates"
date: 2023-06-15
url: https://discourse.slicer.org/t/30055
---

# Screen position from RAS coordinates

**Topic ID**: 30055
**Date**: 2023-06-15
**URL**: https://discourse.slicer.org/t/screen-position-from-ras-coordinates/30055

---

## Post #1 by @pearsonm (2023-06-15 15:31 UTC)

<p>slicer.util.clickAndDrag() includes a code snippet that uses an interactor to show the screen position on left mouse click. Is there a way to get the screen position from RAS coordinates in the Red slice? I want to import ROIs from another program and draw them in slicer with simulated mouse clicks.</p>

---

## Post #2 by @pearsonm (2023-06-16 01:59 UTC)

<p>I found <a href="https://github.com/Slicer/Slicer/blob/c3d74d68839078ec02b1053d4ba413643e84630c/Modules/Loadable/Markups/Testing/Python/NeurosurgicalPlanningTutorialMarkupsSelfTest.py#L111" rel="noopener nofollow ugc">rasToDisplay</a> which does what I want.</p>

---
