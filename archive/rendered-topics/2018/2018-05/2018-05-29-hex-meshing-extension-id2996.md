# Hex Meshing Extension

**Topic ID**: 2996
**Date**: 2018-05-29
**URL**: https://discourse.slicer.org/t/hex-meshing-extension/2996

---

## Post #1 by @HarishRRao (2018-05-29 15:08 UTC)

<p>Hello,</p>
<p>I discovered that a hex-meshing extension called IA-FEMesh was available in the Slicer version 3.6 and I do not see it anymore. Is it discontinued or is there another extension which can perform hex meshing of segmentations?</p>

---

## Post #2 by @pieper (2018-05-29 15:48 UTC)

<p>I’m afraid we didn’t have resources to bring the IA-FEMesh code into the 4.x version.</p>

---

## Post #3 by @HarishRRao (2018-05-29 16:04 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Are there any alternatives to perform a hex mesh within Slicer?</p>

---

## Post #4 by @brhoom (2018-05-29 16:25 UTC)

<p>I found this <a href="https://github.com/gaoxifeng/Robust-Hexahedral-Re-Meshing" rel="nofollow noopener">openSource</a> but I didn’t test.</p>

---

## Post #5 by @lassoan (2018-05-29 16:46 UTC)

<p>There are many mesh generators out there and it should be quite easy to extend the Segment Mesher module to work with them.</p>
<p>The Segment Mesher is essentially just a Python script, which converts input image or mesh to a format that the mesher accepts, runs the meshing algorithm, and imports the result back into Slicer. The module can already use two libraries (TetGen and Cleaver2) - extending it to support more should not be a problem.</p>

---
