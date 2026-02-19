---
topic_id: 2633
title: "How To Remove An Organ Hands Or Foot In Dicom Image Of Phant"
date: 2018-04-19
url: https://discourse.slicer.org/t/2633
---

# How to remove an organ (Hands or foot) in DICOM Image of Phantom with 3D Slicer

**Topic ID**: 2633
**Date**: 2018-04-19
**URL**: https://discourse.slicer.org/t/how-to-remove-an-organ-hands-or-foot-in-dicom-image-of-phantom-with-3d-slicer/2633

---

## Post #1 by @MeryMB (2018-04-19 13:13 UTC)

<p>Dear Slicer User</p>
<p>Good day<br>
I am a beginner with Slicer<br>
I Produce DICOM image of XCAT and I want to use them in TPS for breast cancer Radiation therapy.<br>
I have to remove its left hand before planning because it is on beam path and make a problem.</p>
<p>I want to do it with 3DSlicer. How Can I remove its hands?<br>
I wonder if someone have time to explain it for me?</p>
<p>Best<br>
Mery</p>

---

## Post #2 by @bharat (2018-04-19 13:55 UTC)

<p>Just do not paint it</p>

---

## Post #3 by @gcsharp (2018-04-19 16:00 UTC)

<p>Bherat may be trying to say that if you exclude the hand from the “skin contour” or “external contour”, your TPS will exclude that region from dose calculation.</p>
<p>But if you want to modify the pixels, you can do that as well.  First, create a mask image (draw in segmentation module, then export as a labelmap volume) of everything you want to keep (everything except the hand).  Then, go to “Simple Filters” and choose “MaskImageFilter”.  Fill in the input values appropriately, and set the value outside mask to -1000.  Click “Apply”.</p>

---

## Post #4 by @lassoan (2018-04-19 17:02 UTC)

<p>If you install SegmentEditorExtraEffects extension then it adds “Mask volume” effect to the Segment editor. This effect can blank out areas of a volume inside or outside a segment. It is equivalent to exporting the segment and applying to a volume using Simple Filters, but Mask volume effect is more convenient, as it takes just a few clicks and you don’t need to switch between modules.</p>
<p>See a short demo video here:</p>
<div class="lazyYT" data-youtube-id="xZwyW6SaoM4" data-youtube-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #5 by @MeryMB (2018-04-19 17:48 UTC)

<p>Hi Dear Greg</p>
<p>I tried to do it by TPS but it is not work, even I try to make a new contour on her hand and change its electron density to 0.002 (as AIR) but I do not know why TPS do not care about the new contour and calculate it as a tissue in the path of beam.<br>
Thanks for your suggestion.</p>
<p>Best<br>
Mery</p>

---
