# NRRD Segmentation To Numpy problem

**Topic ID**: 29122
**Date**: 2023-04-25
**URL**: https://discourse.slicer.org/t/nrrd-segmentation-to-numpy-problem/29122

---

## Post #1 by @Thirawat (2023-04-25 23:40 UTC)

<p>Hi, All<br>
I have .nrrd files of segmentations, so I only have 2 classes.<br>
but not all each file have 2 classes, I can say that most of them are one class for one file.</p>
<p>then let’s talk about my problem.<br>
I try to take segmentations to NumPy array in Python. but when it has one class in the file. It will assume that the class is value 1 by not caring class name or class color.<br>
then I try another way but it did not work.</p>
<h2><a name="p-94060-i-try-these-ways-1" class="anchor" href="#p-94060-i-try-these-ways-1" aria-label="Heading link"></a>I try these ways.</h2>
<ol>
<li>try to read nrrd.  But when it has on class on file. that class will be value 1.</li>
</ol>
<hr>
<ol start="2">
<li>try to convert nrrd to tiff images using Python. But the image has some transformation from the original.</li>
</ol>
<hr>
<ol start="3">
<li>try to convert nrrd to tif stack using 3D Slicer. But like no.1.</li>
</ol>
<hr>
<ol start="4">
<li>try to convert nrrd to dcm files using 3D Slicer. But like no.1.</li>
</ol>
<p>Can someone help me, All I need is class A value is 1. Class B value is 2. even if it has one class on that file.<br>
So all 2 classes on files work as well.</p>
<p>Or I do something wrong ;-;.</p>
<p>thank you a lot.<br>
Thirawat.</p>

---

## Post #2 by @Thirawat (2023-04-26 09:55 UTC)

<p>Should I do it manually?<br>
Map the file name and class on my csv then change its value.</p>

---
