---
topic_id: 6527
title: "3D Reconstruction"
date: 2019-04-17
url: https://discourse.slicer.org/t/6527
---

# 3D reconstruction

**Topic ID**: 6527
**Date**: 2019-04-17
**URL**: https://discourse.slicer.org/t/3d-reconstruction/6527

---

## Post #1 by @zineb (2019-04-17 14:13 UTC)

<p>Hello,<br>
can we have 3D reconstruction from ct images?</p>

---

## Post #2 by @lassoan (2019-04-17 14:20 UTC)

<p>“3D reconstruction” may mean many things, but most likely the answer is yes, since Slicer can do all kinds of reformatting and reconstructing of CT images to volumes or meshes. You can check out <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training" rel="nofollow noopener">Slicer tutorials</a> to get started.</p>

---

## Post #3 by @zineb (2019-05-07 15:07 UTC)

<p>hello, thanks a lot i’ve found a solution on this video   <a href="https://www.youtube.com/watch?v=B_SC_WZgb5A" rel="nofollow noopener">https://www.youtube.com/watch?v=B_SC_WZgb5A</a><br>
I’d like to know if it is possible to add annotations (text) on 3D slicer</p>

---

## Post #4 by @muratmaga (2019-05-07 15:19 UTC)

<p>You can use the Markup module and create a point where you want the text to appear, scale fiducial Glyph to zero, and then change the fiducial label to the text you would like to place.</p>

---

## Post #5 by @cpinter (2019-05-07 15:32 UTC)

<p>The video you found is for a quite old version of Slicer and it uses modules that are since then deprecated.<br>
Please refer to the Slicer training material for segmentation: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a><br>
There is a video about 3D printing that shows the latest tools.</p>

---
