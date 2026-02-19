---
topic_id: 3008
title: "Does 3D Slicer Have Any Tools With A Function Similar To Ami"
date: 2018-05-29
url: https://discourse.slicer.org/t/3008
---

# Does 3D slicer have any tools with a function similar to AMIRA's "magic wand"?

**Topic ID**: 3008
**Date**: 2018-05-29
**URL**: https://discourse.slicer.org/t/does-3d-slicer-have-any-tools-with-a-function-similar-to-amiras-magic-wand/3008

---

## Post #1 by @Naia (2018-05-29 15:48 UTC)

<p>I’m looking for a 3D Slicer tool that will segment a bone isolated from others from a single click, taking into account the threshold chosen by the user. This logic of this tool would be to select all the pixels that are in contact with the spot where the cick was made (in sequence), within the chosen threshold.<br>
This is how AMIRA’s “Magic Wand” works.<br>
<strong>Does 3D slicer have any tools with a function similar to AMIRA’s “Magic Wand”?</strong></p>
<p>The properties of the computer I’m using for segmentating are as follows:</p>
<p>gpu - Nvidia Quadro P4000<br>
256 GB RAM<br>
Processor: Xeon E5-2643 v4 – 3,4 GHz (6 cores)</p>

---

## Post #2 by @lassoan (2018-05-29 17:07 UTC)

<p>Yes, and also hopefully you find there are also much better tools.</p>
<p>I think the closest to the Magic Wand effect is “Flood filling” effect, provided by SegmentEditorExtraEffects extension.</p>
<p>I would also recommend to try “Grow from seeds” effect as explained here: <a href="https://discourse.slicer.org/t/bone-segmentation-to-create-3d-printable-stl/960/2">Bone segmentation to create 3D-printable STL</a>. You may also try to use Watershed effect, which takes some more time to compute but provides smooth surfaces.</p>
<p>I would also recommend to check out segmentation tutorials here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>

---

## Post #3 by @muratmaga (2018-05-30 16:55 UTC)

<p>It has been a while I used Amira but, isn’t the “level trace” + intensity range is a closer approximation of the magic wand?</p>

---

## Post #4 by @Melodicpinpon (2020-01-31 13:59 UTC)

<p>This one works only on one slice, isn’t it?</p>

---

## Post #5 by @lassoan (2020-01-31 14:18 UTC)

<p>The recently added <a href="https://discourse.slicer.org/t/new-segment-editor-effect-local-threshold/9233">Local threshold</a> effect is an attempt to make magic-wand-like function in 3D. It cannot provide real-time feedback of the region in 3D (computation may take a couple of seconds) but you get live preview of the considered intensity range and it you get w few parameters to control which regions get connected.</p>

---
