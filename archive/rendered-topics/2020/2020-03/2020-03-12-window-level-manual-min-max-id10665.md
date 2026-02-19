---
topic_id: 10665
title: "Window Level Manual Min Max"
date: 2020-03-12
url: https://discourse.slicer.org/t/10665
---

# Window Level Manual Min/Max

**Topic ID**: 10665
**Date**: 2020-03-12
**URL**: https://discourse.slicer.org/t/window-level-manual-min-max/10665

---

## Post #1 by @Anonymous (2020-03-12 20:35 UTC)

<p>Hello,</p>
<p>I am trying to understand how the manual min/max window level and threshold in the volumes tab works. I need to be able to convert back from pixel intensity to Hounsfield units. I use screen capture to obtain a png image and I save the nifti data to know the Hounsfield units. When I plot (using Matlab) the relationship between the Hounsfield units and pixel intensity, I don’t see any relationship to the window level. If there is a simple way to convert from png back to Hounsfield units, please let me know.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-03-12 22:32 UTC)

<p>Nifti is developed for functional MRI imaging. Try to use nrrd file format instead. Window/Level adjustment is a simple linear mapping of the selected window to 8-bit (0-255) displayable intensity range.</p>

---
