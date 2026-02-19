---
topic_id: 18566
title: "Edit And Modify The Geometry"
date: 2021-07-07
url: https://discourse.slicer.org/t/18566
---

# Edit and modify the geometry

**Topic ID**: 18566
**Date**: 2021-07-07
**URL**: https://discourse.slicer.org/t/edit-and-modify-the-geometry/18566

---

## Post #1 by @smm9886 (2021-07-07 15:22 UTC)

<p>Hi all,</p>
<p>I am working with some patient-specific DICOM data files in 3D-Slicer, trying to extract the aorta and coronary arteries, see the attached photo, from a whole thorax and heart model.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d611c782549184e4946557765437c5cfafb5bf23.png" alt="Picture1" data-base62-sha1="uxKgMEc02ODCvP5Rt215GW9RgtR" width="474" height="358"></p>
<p>I need to modify this model before I can export it into an STL file and 3D printing processes. For instance, I want to increase the diameter of the coronary arteries (specifically the distal parts which look like some points rather than tubes), or I want to stretch the coronaries or aorta. I am wondering if this is possible in 3D Slicer?<br>
I can provide more detail if necessary. I appreciate any sort of help or suggestions.</p>
<p>Best wishes,<br>
Mahmoud</p>

---

## Post #2 by @lassoan (2021-07-12 14:41 UTC)

<p>You can use “Draw tube” effect (provided by SegmentEditorExtraEffects extension) to make coronary vessels longer and more uniform diameter, and to lengthen the aorta with a tubular segment.</p>

---

## Post #3 by @smm9886 (2021-07-13 07:55 UTC)

<p>Thank you Andras! Also, can I change the coronary angle take-off from Valsalva sinuses?</p>

---

## Post #4 by @lassoan (2021-07-13 13:15 UTC)

<p>There are many tools to edit segmentations, so it should be no problem to modify this angle. For example, you can draw the new vessel branch using Draw tube effect and then remove the old one using the Scissors effect in a 3D view.</p>

---
