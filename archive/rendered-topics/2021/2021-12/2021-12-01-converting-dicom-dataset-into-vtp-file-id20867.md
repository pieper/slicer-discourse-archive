---
topic_id: 20867
title: "Converting Dicom Dataset Into Vtp File"
date: 2021-12-01
url: https://discourse.slicer.org/t/20867
---

# converting dicom dataset into vtp file

**Topic ID**: 20867
**Date**: 2021-12-01
**URL**: https://discourse.slicer.org/t/converting-dicom-dataset-into-vtp-file/20867

---

## Post #1 by @khater (2021-12-01 17:21 UTC)

<p>i just started using vmtk on python ( windows operating system) and i want to use the vmtkcenterlines but the problem is that vmtkcenterlines uses .vtp file and i didn’t find any tutorial to help converting dicom files into vtp files.<br>
how can i change a .dcm file to .vtp file?</p>
<p>thanks in advance</p>

---

## Post #2 by @lassoan (2021-12-02 16:24 UTC)

<p>You need to segment the DICOM image before you can extract centerline. Vessel segmentation of very well contrasted large vessels can be trivial, so that you can use any of the automatic segmentation methods (thresholding, region growing, fast marching, etc.). However, for most images you need to use a a combination of a few semi-automatic segmentation tools, such as those implemented in 3D Slicer’s Segment Editor (<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">this page</a> is a good starting point).</p>
<p>Once you have the segmentation, you can export it to a polygonal mesh (.vtp file) and automatically extract centerline.</p>
<p>Here is a short video of a typical vessel segmentation and centerline extraction workflow:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="caEuwJ7pCWs" data-video-title="Vessel segmentation and centerline extraction using 3D Slicer and VMTK" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=caEuwJ7pCWs" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/caEuwJ7pCWs/maxresdefault.jpg" title="Vessel segmentation and centerline extraction using 3D Slicer and VMTK" width="" height="">
  </a>
</div>


---

## Post #3 by @khater (2021-12-03 15:22 UTC)

<p>Dear Mr. Lasso,<br>
thank you so much for your help and I’ll definitely check it out.</p>

---
