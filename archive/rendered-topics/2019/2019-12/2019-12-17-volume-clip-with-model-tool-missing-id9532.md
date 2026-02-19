---
topic_id: 9532
title: "Volume Clip With Model Tool Missing"
date: 2019-12-17
url: https://discourse.slicer.org/t/9532
---

# Volume Clip with model tool missing !

**Topic ID**: 9532
**Date**: 2019-12-17
**URL**: https://discourse.slicer.org/t/volume-clip-with-model-tool-missing/9532

---

## Post #1 by @Vignesh_Sivakumar (2019-12-17 19:51 UTC)

<p>Hi,<br>
I have Slicer 4.10.2 in my Windows PC and have been using it for some time. I have a need to use the “Volume Clip with model” tool that existed in the previous versions which don’t seem to exist in this version. Is the name changed to something else or some other module been created or has it been removed? I would really appreciate some help here.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2019-12-17 21:41 UTC)

<p>VolumeClip extension is still available for both latest stable and preview releases. Do you have trouble finding the extension in the extension manager or “Volume clip with model” does not show up after installing the extension?</p>
<p>Note that a surface generation and volume masking is available directly in Segment Editor module (after you install SegmentEditorExtraEffects extension). You can create segments using “Surface cut” effect, optionally edit the shape using any other effects, then use “Mask volume” effect to use the segment to blank out part of a volume.</p>
<div class="lazyYT" data-youtube-id="xZwyW6SaoM4" data-youtube-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---
