---
topic_id: 28995
title: "Ultrasound To Stl"
date: 2023-04-18
url: https://discourse.slicer.org/t/28995
---

# Ultrasound to stl

**Topic ID**: 28995
**Date**: 2023-04-18
**URL**: https://discourse.slicer.org/t/ultrasound-to-stl/28995

---

## Post #1 by @vryko (2023-04-18 21:06 UTC)

<p>Hello</p>
<p>I am new to all of this an i would like your help on an subject. Sorry if this problem has already been answered. Well i am trying to make my baby from the ultrasound to 3d model but i cant find out how. I have dowloaded 3d slicer, i have the files in different extensions and formats (vol.dicom.bmp.raw) but i cant do anything. Does anyone has an advice on this? Thank you very much in advance</p>

---

## Post #2 by @lassoan (2023-04-20 04:48 UTC)

<p>If none of the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md">SlicerHeart ultrasound DICOM import instructions</a> are applicable to your images then most likely the files do not contain 3D information (only a screen capture of the 3D rendering that was done on the ultrasound cart) or it is stored in a proprietary format that Slicer does not recognize.</p>

---

## Post #3 by @vryko (2023-04-29 09:22 UTC)

<p>Hello again. I can’t seem to figure it out. I think I tried everything but with no results. Is it possible to provide a training ( not necessarily free) in order to understand what am I doing wrong? Or what to ask for the doctor? Thank you very much.</p>

---

## Post #4 by @lassoan (2023-04-30 13:41 UTC)

<p>If none of the instructions helped then most likely what you have is just screen recording of the ultrasound machine as it displays the 3D rendering. You cannot reconstruct a 3D image from such screen capture video.</p>

---
