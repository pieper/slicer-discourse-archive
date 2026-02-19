---
topic_id: 8117
title: "Combination Of 2 Series With Interslice Gaps Acquired In An"
date: 2019-08-21
url: https://discourse.slicer.org/t/8117
---

# Combination of 2 series with interslice gaps, acquired in an interleaved manner

**Topic ID**: 8117
**Date**: 2019-08-21
**URL**: https://discourse.slicer.org/t/combination-of-2-series-with-interslice-gaps-acquired-in-an-interleaved-manner/8117

---

## Post #1 by @Lee_Ho_Jun (2019-08-21 03:04 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello 3D slicer community.<br>
I have 2 2D MRI series, acquired in an interleaved manner.<br>
Namely, 1 series is acquired in a 1.2mm slice thickness with 1.2mm gap, and the other series with the same dimension, but slighted shifted to acquire slices in the location of the gaps, in the first series.<br>
I want to stich them into 1 series, however when I load them on 3D slicer, and add them, it results in 2.4-mm slice thickness images.<br>
I want to make the 2 series into a 1.2mm slice thickness series, but cannot figure out a way.<br>
I kindly ask for your help.</p>
<p>Best wishes,<br>
Ho-Joon Lee</p>

---

## Post #2 by @lassoan (2019-08-21 13:13 UTC)

<p>One approach could be to patch DICOM files before importing, so that all the files are read as a single series. Probably overwriting Series Instance UID would be enough. You can use DCMTK’s dcmodify command-line tool or pydicom Python package.</p>
<p>Another approach would be to merge the two stacks after loading the volumes. Probably the easiest is to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromVolume" rel="nofollow noopener">get the volumes as 3D numpy arrays</a>, merge the arrays using standard numpy operations, and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateVolumeFromArray" rel="nofollow noopener">set the merged array into a volume node</a>.</p>

---

## Post #3 by @Lee_Ho_Jun (2019-08-21 23:32 UTC)

<p>Thank you Andras for your comments.</p>
<p>I have tried to patch the DICOM files with the tool in 3D slicer, but when imported with the DICOM tool, it recognizes the patched DICOM series as 2 separate series.<br>
Is there some other way to do it in Slicer?<br>
For the second suggesting, I am not really familiar with the Slicer API, is there a tutorial that I might follow?</p>
<p>Best,<br>
HJ</p>

---

## Post #4 by @lassoan (2019-08-22 02:44 UTC)

<aside class="quote no-group" data-username="Lee_Ho_Jun" data-post="3" data-topic="8117">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_ho_jun/48/4519_2.png" class="avatar"> Lee_Ho_Jun:</div>
<blockquote>
<p>I have tried to patch the DICOM files with the tool in 3D slicer, but when imported with the DICOM tool</p>
</blockquote>
</aside>
<p>Slicer’s DICOM Patcher module does not change existing series instance UID in a DICOM file. You need to write your own script to do that.</p>
<aside class="quote no-group" data-username="Lee_Ho_Jun" data-post="3" data-topic="8117">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_ho_jun/48/4519_2.png" class="avatar"> Lee_Ho_Jun:</div>
<blockquote>
<p>I am not really familiar with the Slicer API, is there a tutorial that I might follow?</p>
</blockquote>
</aside>
<p>See programming tutorials on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers">Slicer training page</a>. Mostly those two functions that I’ve posted the links to should be the Slicer-specific functions you need.</p>

---
