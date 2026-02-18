# Visualizing MRI data taken over time and taking cross sections

**Topic ID**: 18372
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/visualizing-mri-data-taken-over-time-and-taking-cross-sections/18372

---

## Post #1 by @dsoto (2021-06-28 15:02 UTC)

<p>Hello all,</p>
<p>I’m new to using Slicer and have run into a couple issues regarding displaying MRI data. So I have multiple datasets I am working with, some of which are anatomical, taking cross sections over different sagittal planes. These frames display very readily in 3D Slicer, and I have had not issue with them. My issue arises when I attempt to display MRI data in the same plane, that has been taken over time. I tend to get a rhombus-shaped cross section that slides from left to right for a single time-point. See the attachment for an example. How can I have Slicer display the entire 300-frame set?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/288ef84d3a41ffef0d1ed090cb2bbe8265ebe2de.png" alt="cross section MRI" data-base62-sha1="5MNprS838fNSIDLKK71Htkv4f6u" width="500" height="206"></p>
<p>ALSO, in the past I have used ImageJ for these analyses, but learned about Slicer and was hoping it had some capabilities I need for research. The first is, I want to determine changes in a very specific area of an MRI over time. Specifically, I want to draw a line through an organ and have it take the same line from all 300 frames in a data set and display them side-by-side. Is anything like that possible?</p>
<p>Thank you in advance!</p>
<p>Best,<br>
D</p>

---

## Post #2 by @lassoan (2021-06-28 15:08 UTC)

<aside class="quote no-group" data-username="dsoto" data-post="1" data-topic="18372">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsoto/48/11410_2.png" class="avatar"> dsoto:</div>
<blockquote>
<p>These frames display very readily in 3D Slicer, and I have had not issue with them. My issue arises when I attempt to display MRI data in the same plane, that has been taken over time. I tend to get a rhombus-shaped cross section that slides from left to right for a single time-point. See the attachment for an example. How can I have Slicer display the entire 300-frame set?</p>
</blockquote>
</aside>
<p>In Slicer-4.11 and earlier, slice views are aligned to anatomical axes by default and you need to click <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">“Rotate to volume plane” button</a> to make it snap to the image slice’s orientation. In Slicer-4.13 (recent Slicer Preview Releases), when you click on the eye icon of a volume in Data module, the slice view is rotated to the image plane by default. You can also <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#selecting-displayed-data">drag-and-drop a volume into a slice view</a> to make that volume show up in that view, with the slice view orientation aligned with the image axis.</p>

---

## Post #3 by @dsoto (2021-06-28 15:20 UTC)

<p>Thank you, Dr. Lasso, much appreciated!</p>

---
