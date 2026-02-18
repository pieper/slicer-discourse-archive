# Track motion of anatomical points in 4D DICOM image

**Topic ID**: 4169
**Date**: 2018-09-22
**URL**: https://discourse.slicer.org/t/track-motion-of-anatomical-points-in-4d-dicom-image/4169

---

## Post #1 by @Melanie (2018-09-22 12:06 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.9<br>
Expected behavior:<br>
Actual behavior: Could someone kindly advise on how to analyse 4 D dicom data using slicer please. I can not even get it  to load to slicer (one series is about7-8Gb) I don’t know how to split using any other software. (compatible with a PC with windows 10)<br>
Thanks</p>

---

## Post #2 by @lassoan (2018-09-22 12:09 UTC)

<p>Would you like to load 4D volumes (3D image sequence)?<br>
What kind of analysis would you like to do?</p>
<p>In general, use latest nightly version of Slicer for this (as DICOM import of 4D data sets have been greatly improved since Slicer-4.8.1) and make sure you have 5-10x more memory space than the total image size. If you don’t that much physical memory then allocate that much virtual memory/swap space (everything will work but may be much slower).</p>
<p>If you have problems loading the file, upload the application log (menu: Help / Report a bug) and copy-paste the link here.</p>

---

## Post #3 by @Melanie (2018-09-22 12:18 UTC)

<p>Thank you ever so much Prof Lasso. Being impatient I did search all previous questions and foud you have explained this loading as a sequence. I did that, takes about 7-8 minutes but its great, I managed to do it. I have another question if that alright. I am trying to track motion in real time of bones using 4 D CT. How do I  put fiducial points on bony land marks. When I add them just off the tool bar the fiducial point seem to move away (It does not stick to the landmark I want to track) could you please advise on this please. Thanks a lot.</p>

---

## Post #4 by @lassoan (2018-09-23 02:30 UTC)

<p>You need to use <a href="https://github.com/moselhy/SlicerSequenceRegistration">Sequence Registration</a> module to compute displacements over time as a sequence of transforms. Once you have the transform sequence, you just need to create a markup fiducial node, apply the computed transform, and mark the anatomical points. When you replay the sequence, the computed transform will move the landmarks to the correct position in each frame.</p>

---

## Post #5 by @Melanie (2018-09-23 02:57 UTC)

<p>Thanks a lot, This is very very useful. I will let you know how the project goes. Thank you again. Sorry how do I get the transform sequence? ( I very new to this, so sorry about these questions)</p>

---

## Post #6 by @lassoan (2018-09-23 03:05 UTC)

<p>Sequence registration computes the transform sequence.</p>

---

## Post #7 by @Melanie (2018-09-23 03:19 UTC)

<p>Thanks a lot Prof Lasso.</p>

---
