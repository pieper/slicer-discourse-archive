# Vector to scalar volume grayed out

**Topic ID**: 33832
**Date**: 2024-01-17
**URL**: https://discourse.slicer.org/t/vector-to-scalar-volume-grayed-out/33832

---

## Post #1 by @Andreas_Vossinakis (2024-01-17 16:19 UTC)

<p>Hi, I load the images in a volume but when I try to convert this volume to a scalar volume, the ‘input vector volume’ dropdown menu is grayed and I can’t choose the volume I work on. Please help</p>

---

## Post #2 by @muratmaga (2024-01-17 16:31 UTC)

<p>Make sure you indeed have vector volume loaded into the scene:</p>
<p>Right click on the Volume, choose “Edit Properties” and then in the opened <code>Volumes</code> module, navigate to the Volume Information and look at the <strong>Volume type r</strong>eported<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6580c13b2253c1dd8e15d87d56ea17a9c1ac9cce.png" data-download-href="/uploads/short-url/etW4Z8rT9zWlDlZd7D8SvGTplX8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6580c13b2253c1dd8e15d87d56ea17a9c1ac9cce_2_690x484.png" alt="image" data-base62-sha1="etW4Z8rT9zWlDlZd7D8SvGTplX8" width="690" height="484" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6580c13b2253c1dd8e15d87d56ea17a9c1ac9cce_2_690x484.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6580c13b2253c1dd8e15d87d56ea17a9c1ac9cce_2_1035x726.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6580c13b2253c1dd8e15d87d56ea17a9c1ac9cce.png 2x" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1170×822 43 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Andreas_Vossinakis (2024-01-18 07:43 UTC)

<p>Hi, thanks for your reply. These are the volume properties<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e0ee26bba2f01122369e10609c27c41d8f2ae3e.jpeg" alt="2024-01-18_094039" data-base62-sha1="hZa3al6rb3fCQNBShQnD5rdjwd0" width="518" height="424"></p>

---

## Post #4 by @muratmaga (2024-01-18 15:13 UTC)

<p>That’s the issue. You don’t have a vector volume, but a scalar one. So the input node selector is grayed out.</p>

---

## Post #5 by @Andreas_Vossinakis (2024-01-19 07:31 UTC)

<p>Can I convert the scalar volume to a vector one??</p>

---

## Post #6 by @muratmaga (2024-01-19 15:42 UTC)

<p>You can, but it will be somewhat pointless. All three channels of the vector volume will contain the same value as the original scalar volume.</p>
<p>What are you trying to accomplish?</p>

---

## Post #7 by @Andreas_Vossinakis (2024-01-19 15:43 UTC)

<p>I have a set of images and I want to make a 3d model</p>

---

## Post #8 by @muratmaga (2024-01-19 16:14 UTC)

<p>That’s usually done by segmentation. And segmentation works on scalar volumes, not vectors ones. I would suggest making yourself familiar with the Slicer documentation, particularly the section on Image Segmentation. <a href="https://slicer.readthedocs.io">https://slicer.readthedocs.io</a></p>

---
