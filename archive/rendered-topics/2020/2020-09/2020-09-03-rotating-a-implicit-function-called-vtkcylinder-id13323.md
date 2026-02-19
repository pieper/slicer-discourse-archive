---
topic_id: 13323
title: "Rotating A Implicit Function Called Vtkcylinder"
date: 2020-09-03
url: https://discourse.slicer.org/t/13323
---

# Rotating a implicit function called vtkCylinder

**Topic ID**: 13323
**Date**: 2020-09-03
**URL**: https://discourse.slicer.org/t/rotating-a-implicit-function-called-vtkcylinder/13323

---

## Post #1 by @Anish_Basnet (2020-09-03 15:07 UTC)

<p>Hello everyone,<br>
I am new to VTK and this forum. I just wanted to know if there is a solution to rotate an implicit function called vtkCylinder by 90 degrees. I would like to add the clip functionality in ModelClip extension and set it to the vtkCylinder implicit function. With vtkCylinderSource.h I have read that it is possible by translating the center and rotating by 90 degrees and translating back. Is there similar solution to achieve it?</p>

---

## Post #2 by @lassoan (2020-09-03 16:25 UTC)

<p>You can transform nodes by applying a transformation node as shown here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="bbikx7Edv4g" data-video-title="Transforming objects using Data module in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=bbikx7Edv4g" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/bbikx7Edv4g/hqdefault.jpg" title="Transforming objects using Data module in 3D Slicer" width="" height="">
  </a>
</div>

<p>If you want to use this from a Python script then check out these examples: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Examples">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Examples</a></p>

---

## Post #3 by @Anish_Basnet (2020-09-04 14:53 UTC)

<p>Thank you for your reply! But what I am trying to rotate the implicit function with header name vtkCylinder.h by  90 degrees. I already have assigned the center and the radius of the cylinder but I am editing a loadable module. I would like to clip a stl data in two parts around the center with this cylinder function. But I would have to rotate the cylinder  by 90 degrees to get the clipping functionality right.</p>

---

## Post #4 by @lassoan (2020-09-04 16:19 UTC)

<p>You can change orientation of a vtkCylinder implicit function by calling its <code>SetAxis</code> method.</p>

---

## Post #5 by @Anish_Basnet (2020-09-08 20:07 UTC)

<p>Hey Andras,<br>
Thank you very much! I did as you suggested and now it works. I would like to ask one more thing. I have clipped the stl data successfully. But now I am trying to rotate those clipped parts(one of them would be fine). It’d be really nice if you could give me some suggestions regarding it.</p>

---

## Post #6 by @lassoan (2020-09-08 22:25 UTC)

<p>You can apply transform to the segmentation node. If you want to rotate individual segments but not others, then you can:</p>
<ul>
<li>move the segments to a new segmentation node</li>
<li>apply a transform to the new segmentation node</li>
<li>move the segments back to the original segmentation node</li>
</ul>

---

## Post #7 by @Anish_Basnet (2020-09-10 11:26 UTC)

<p>Thank you will try and let you know!</p>

---

## Post #8 by @lassoan (2020-09-10 13:28 UTC)

<p>A post was merged into an existing topic: <a href="/t/cannot-find-rectangle-segmentation-option/13286/20">Cannot find rectangle segmentation option</a></p>

---
