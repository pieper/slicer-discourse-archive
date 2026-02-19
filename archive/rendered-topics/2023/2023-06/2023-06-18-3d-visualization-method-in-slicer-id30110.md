---
topic_id: 30110
title: "3D Visualization Method In Slicer"
date: 2023-06-18
url: https://discourse.slicer.org/t/30110
---

# 3D Visualization Method in Slicer

**Topic ID**: 30110
**Date**: 2023-06-18
**URL**: https://discourse.slicer.org/t/3d-visualization-method-in-slicer/30110

---

## Post #1 by @DzungDinh (2023-06-18 23:42 UTC)

<p>Hello,</p>
<p>I wonder what 3d visualization method using for reconstructing 3D segmentation in Slicer? (e.g., interpolation, …). Moreover, is there any way I can view the current method?</p>
<p>FYI, I have the segmentation in 2D, and Slicer helps me view it in 3D</p>
<p>Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8231e21e758149bbe2604fe1b8c88557f858dd84.png" data-download-href="/uploads/short-url/izKWCPRzeTBYRnDQiHzjVw9oSS8.png?dl=1" title="Screenshot 2023-06-18 at 7.06.46 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8231e21e758149bbe2604fe1b8c88557f858dd84_2_661x499.png" alt="Screenshot 2023-06-18 at 7.06.46 PM" data-base62-sha1="izKWCPRzeTBYRnDQiHzjVw9oSS8" width="661" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8231e21e758149bbe2604fe1b8c88557f858dd84_2_661x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8231e21e758149bbe2604fe1b8c88557f858dd84_2_991x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8231e21e758149bbe2604fe1b8c88557f858dd84.png 2x" data-dominant-color="9397CA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-18 at 7.06.46 PM</span><span class="informations">1316×994 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2023-06-19 00:11 UTC)

<p>Probably you should start from here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>
<p>and then this:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html</a></p>

---

## Post #3 by @DzungDinh (2023-06-19 04:24 UTC)

<p>I don’t see they specify the visualization methods in the documents that you mentioned.</p>

---

## Post #4 by @muratmaga (2023-06-19 16:11 UTC)

<p>It explains that segmentations are turned into 3D models and visualized as surface meshes? What specifically are looking for visualization methods?</p>

---

## Post #5 by @DzungDinh (2023-06-20 18:18 UTC)

<p>I am sorry for the miscommunication. My question is, what methods are used to turn into 3D models?</p>

---

## Post #6 by @muratmaga (2023-06-20 18:58 UTC)

<p>I believe it uses the <a href="https://vtk.org/doc/nightly/html/classvtkDiscreteFlyingEdges3D.html">vtkDiscreteFlyingEdges3D</a> filter to convert labelmaps into 3D models, but you should check the source code to make sure.</p>

---
