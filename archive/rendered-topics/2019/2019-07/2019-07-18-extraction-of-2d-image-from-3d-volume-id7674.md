---
topic_id: 7674
title: "Extraction Of 2D Image From 3D Volume"
date: 2019-07-18
url: https://discourse.slicer.org/t/7674
---

# Extraction of 2D Image from 3D Volume

**Topic ID**: 7674
**Date**: 2019-07-18
**URL**: https://discourse.slicer.org/t/extraction-of-2d-image-from-3d-volume/7674

---

## Post #1 by @uwo27 (2019-07-18 18:17 UTC)

<p>Operating system: macOS mojave<br>
Slicer version: 4.10.2</p>
<p>Hi, I am looking for help on how to extract a 2D image from a 3D volume.</p>

---

## Post #2 by @cpinter (2019-07-18 18:29 UTC)

<p>There are many ways to interpret your question.</p>
<p>I’ll start with the simplest and suggest that you take a look at the Screen Capture module, which allows you to capture an image from a volume in a controlled way.</p>

---

## Post #3 by @uwo27 (2019-07-18 19:20 UTC)

<p>Sorry, wasn’t clear. Want to extract it as a 2D nifty image.</p>

---

## Post #4 by @lassoan (2019-07-19 03:42 UTC)

<p>Probably the easiest way is to use the Scissors effect (with Fill inside, Rectangle, Symmetric options), find the slice, and click-and-drag the area you want to extract (can be the full slice, you can also mark multiple slices or regions, each with a separate color). This generates single-slice segment(s) that you can export to single-slice volume(s) using Split volume effect (with Pad voxels=0 option). You can save the exported volumes to nifti file.</p>
<p>You need to install SegmentEditorExtraEffects extension to obtain Split volume effect.</p>

---
