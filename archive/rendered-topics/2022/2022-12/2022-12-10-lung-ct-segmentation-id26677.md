---
topic_id: 26677
title: "Lung Ct Segmentation"
date: 2022-12-10
url: https://discourse.slicer.org/t/26677
---

# Lung CT Segmentation

**Topic ID**: 26677
**Date**: 2022-12-10
**URL**: https://discourse.slicer.org/t/lung-ct-segmentation/26677

---

## Post #1 by @Paula_R (2022-12-10 18:23 UTC)

<p>Hello,</p>
<p>I’ve watched this video: <a href="https://www.youtube.com/watch?v=v1-L_niLZxQ" class="inline-onebox" rel="noopener nofollow ugc">COVID-19 lung CT segmentation using 3D Slicer - YouTube</a><br>
and, in Resample Scalar Volume, Spacing (2,2,2) and linear interpolation are recommended, and I’d like to know why these are the recommended values.</p>
<p>I’m working with CT dicom series, with different pixel spacing in the slices in each series, like (x=1.807, y=1.807), (x=0.699, y=0.699), and similar values, and I’d like to know if this pixel spacing of the slices must be taken into account to define the Spacing for resampling.</p>
<p>Thanks</p>

---

## Post #2 by @curtislisle (2022-12-10 19:31 UTC)

<p>Hi Paula,<br>
Slicer can perform the segmentation at different Voxel resolutions. So you would, theoretically, be able to perform segmentation on your images without resampling first. However, in practice, as the volume resolution increases, a more powerful computer and longer processing time will be needed. Voxel spacing of (2,2,2) is a size that provides reasonable resolution for many applications without being too taxing on the computer. Therefore, it is a good resolution to start with. What size is right for you, will depend on your application.</p>
<p>Also, some analytical processes may come out better when the voxels are cubical and not anisotropic. So making the Z plane size the same is also a reasonable setting to start with.</p>
<p>Slicer will take your original volume resolution into account during any resizing operation. Bilinear resampling was recommended because it offers generally good resampling results with less computational cost than options like Bicubic resampling.</p>
<p>In summary, after becoming comfortable with segmentation you<br>
Might find you want to change these parameters, but they are good initial choices for many applications. I hope this helps.</p>
<p>Curtis</p>

---

## Post #3 by @Paula_R (2022-12-11 11:21 UTC)

<p>Hi Curtis,</p>
<p>yes, this information is very useful. Thank you very much for your answer.</p>
<p>Paula</p>

---

## Post #4 by @rbumm (2022-12-11 11:45 UTC)

<p>Maybe check out the video <a href="https://www.youtube.com/watch?v=fpLxm7uAvZQ">Automated Lung CT segmentation</a> to see a faster solution that includes a (2,2,2) resampling for speed, creates lungs, optionally lobes and airways, and switches back to the original resolution.</p>

---
