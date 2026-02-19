---
topic_id: 7487
title: "How Read The Tag File For Landmarks Visualization"
date: 2019-07-09
url: https://discourse.slicer.org/t/7487
---

# How read the .tag file for landmarks visualization

**Topic ID**: 7487
**Date**: 2019-07-09
**URL**: https://discourse.slicer.org/t/how-read-the-tag-file-for-landmarks-visualization/7487

---

## Post #1 by @ljc19800331 (2019-07-09 21:59 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior:</p>
<p>Hello, I want to check the fiducial on the ultrasound and MRI data and all the fiducials are saved in a .tag file. Since it is not a common .fcsv file and I could not load the .tag file directly in 3D slicer. Any methods to solve this problem? Thanks.</p>
<p>An example of the file looks like:</p>
<pre><code class="lang-auto">MNI Tag Point File
Volumes = 2;
% Case 1: XXX landmarks

Points =
 10 20 30 40 -30 30 ""
......
</code></pre>

---

## Post #2 by @lassoan (2019-07-10 03:25 UTC)

<p>The easiest would be to write a short python script that parses the file line by line by a few regular expressions and adds landmark point positions to a markups fiducial node.</p>
<p>If you want to be able to load a tag file by “Add data” window (or drag-and-dropping to the application window) then you need to add a file reader plug-in. Let us know if you are interested in this and we can help with more specific instructions.</p>

---

## Post #3 by @ljc19800331 (2019-07-10 21:51 UTC)

<p>Thanks for your guidance <a class="mention" href="/u/lassoan">@lassoan</a> . I have wrote the python script to convert the .tag file to .fcsv file and it can be loaded in 3D slicer.</p>
<p>I have two fiducial dataset (one is preoperative MRI and one is 3D ultrasound) and I want to calculate the displacement vector for each fiducial pair. I am wondering if there is a method to calculate the displacement vector for each fiducial point and show all the vectors in the slice and 3D scene. My final goal is to manually check the outlier for each fiducial pairs in both image slice. Thanks.</p>
<p>For example in the two fcsv files, we have:<br>
.fcsv_1 file:<br>
vtkMRMLMarkupsFiducialNode_0,50.164402 -31.719656 34.845306,-5.771,-11.195,9.070,1.000,1,1,0,F1-1,F1-3, …</p>
<p>.fcsv_2 file:<br>
vtkMRMLMarkupsFiducialNode_0,48.972829 -32.396878 34.952277,0.000,0.000,0.000,1.000,1,1,0,M1-2,</p>
<p>The displacement vector = (x1 - x2, y1 - y2, z1 - z2) for each pair. I could calculate all the displacement vectors from two fiducial sets and I would like to load the result to 3D slicer, and able to visualize all the vectors automatically. The result is similar to the following figure (refer from another question “calculating-the-displacement-between-two-models”). And I am not sure if this can be finished all in python.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40580beb33b2184a94762266822cca123af621ba.png" data-download-href="/uploads/short-url/9bdcddSkljzguzkenssmTeBj1sS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40580beb33b2184a94762266822cca123af621ba_2_690x402.png" alt="image" data-base62-sha1="9bdcddSkljzguzkenssmTeBj1sS" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40580beb33b2184a94762266822cca123af621ba_2_690x402.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40580beb33b2184a94762266822cca123af621ba_2_1035x603.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40580beb33b2184a94762266822cca123af621ba_2_1380x804.png 2x" data-dominant-color="C4C3C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1455×848 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks again for your help.</p>

---

## Post #4 by @koeglfryderyk (2021-10-19 14:11 UTC)

<p>Hi, would you mind sharing the script that you wrote? Thanks!</p>

---
