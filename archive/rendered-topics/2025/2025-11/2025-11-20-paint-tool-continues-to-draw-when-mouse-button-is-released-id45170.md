---
topic_id: 45170
title: "Paint Tool Continues To Draw When Mouse Button Is Released"
date: 2025-11-20
url: https://discourse.slicer.org/t/45170
---

# Paint tool continues to draw when mouse button is released

**Topic ID**: 45170
**Date**: 2025-11-20
**URL**: https://discourse.slicer.org/t/paint-tool-continues-to-draw-when-mouse-button-is-released/45170

---

## Post #1 by @catemuse (2025-11-20 15:56 UTC)

<p>Operating system: Mac OS 15.6.1 (24G90)<br>
Slicer version: 5.10.0<br>
Expected behavior: Don’t draw just because cursor is moving<br>
Actual behavior: Draws unwanted areas, killing other segments</p>
<p>I finally got nnInteractive to help segment. The problem I’m having is one that I experienced when trying to segment by hand as well, but the consequences are more disastrous using the nninteractive module. It looks like Slicer thinks I’m trying to draw, but the mouse is released and I’m just trying to move the cursor somewhere else. What can I do to stop this behavior?</p>

---

## Post #2 by @pieper (2025-11-20 16:41 UTC)

<p>I just tested Slicer 5.10.0 on a mac book air with OS 15.6.1 and had no problem with the paint tool.  I was using the built in track pad.  I can’t explain why this wouldn’t work for you.</p>
<p>For nnInteractive, you can often use points or closed curves and get good results while you are investigating what why paint isn’t working for you.</p>

---

## Post #3 by @mikebind (2025-11-20 19:53 UTC)

<p>I have occasionally run into this as well. It behaves as if the mouse button-up event got missed while the processor was busy.  Doing another click has sometimes allowed Slicer to catch that event and get out of the dragging mode. Then, whatever was caused just needs to be undone.  Since undo on painting works well, even with nnInteractive, I have found this annoying, but not fatal as long as it is not too frequent. My impression is that the closer you are to working at the limits of the machine’s memory/processing capabilities, the more likely this is to happen.</p>

---
