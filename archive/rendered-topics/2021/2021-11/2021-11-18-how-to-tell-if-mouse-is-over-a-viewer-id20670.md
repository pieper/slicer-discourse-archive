# How to tell if mouse is over a viewer

**Topic ID**: 20670
**Date**: 2021-11-18
**URL**: https://discourse.slicer.org/t/how-to-tell-if-mouse-is-over-a-viewer/20670

---

## Post #1 by @darren (2021-11-18 00:06 UTC)

<p>How can you tell if you’re on the viewer? Is there something you can test so that certain functionality is disabled when the mouse is not hovered over the viewer?</p>

---

## Post #2 by @lassoan (2021-11-18 00:08 UTC)

<p>You can get the current view ID and position in view and RAS coordinate systems via the crosshair singleton node. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-current-mouse-coordinates-in-a-slice-view">script repository</a>.</p>

---

## Post #3 by @darren (2021-11-18 07:30 UTC)

<p>I see. I am currently using a crosshair node to get information from a viewer when the mouse hovers over the scan. However, after I move my mouse off of the scan/view area, the program crashes. Would this likely be something to do with the crosshair node? Or an interactor?</p>
<p>This only started happening after I began using the crosshair node. Specifically, after I call a line that uses -&gt;GetCursorPositionXYZ(xyz);</p>

---

## Post #4 by @lassoan (2021-11-18 15:34 UTC)

<p>I could not reproduce the crash using the latest Slicer Preview Release. If you can create a small standalone example that reproduces the problem then I can investigate.</p>

---
