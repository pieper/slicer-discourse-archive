---
topic_id: 43707
title: "Segment Visibility In 2D And 3D"
date: 2025-07-13
url: https://discourse.slicer.org/t/43707
---

# segment visibility in 2D and 3D

**Topic ID**: 43707
**Date**: 2025-07-13
**URL**: https://discourse.slicer.org/t/segment-visibility-in-2d-and-3d/43707

---

## Post #1 by @apeneck (2025-07-13 22:28 UTC)

<p>In segment editor, if I click the eye icon next to a segment, it turns it off in the 2D views, but not in the 3D view. I’ve been away from the program for a few weeks, but when I last used it, clicking the eye icon made a segment visible (or invisible) in both 2D and 3D views. I’ve clicked the “Show 3D” button several times, with no change.</p>
<p>I think I’ve forgotten some very basic knowledge that I had just a few weeks ago. Either that or the program’s suddenly gotten squirrely. Help?</p>

---

## Post #2 by @pieper (2025-07-13 22:32 UTC)

<p>Probably you have an extra copy of the segmentation visible, perhaps as a model node?</p>

---

## Post #3 by @apeneck (2025-07-15 17:00 UTC)

<p>Steve - You were correct. Thanks for the help.</p>
<p>I believe this occurred after I converted segments to STL files. Does it make sense that might cause the issue?</p>

---

## Post #4 by @pieper (2025-07-15 17:05 UTC)

<p>Yes, it makes sense that if you exported to STL the segmentation needed to be converted to a model which is displayed in 3D by default.</p>

---
