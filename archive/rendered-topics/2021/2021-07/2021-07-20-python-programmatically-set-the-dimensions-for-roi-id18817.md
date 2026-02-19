---
topic_id: 18817
title: "Python Programmatically Set The Dimensions For Roi"
date: 2021-07-20
url: https://discourse.slicer.org/t/18817
---

# Python: Programmatically set the Dimensions for ROI

**Topic ID**: 18817
**Date**: 2021-07-20
**URL**: https://discourse.slicer.org/t/python-programmatically-set-the-dimensions-for-roi/18817

---

## Post #1 by @Panda (2021-07-20 11:42 UTC)

<p>Hello,</p>
<p>I am trying to write a script to automate the cropping of volume for quite a few CT scans using Python. Thanks to the previous questions and the documentation, I have been able to figure out pretty much the whole code but one thing is still user-dependent which too I would like to set and function automatically. This is the dimension for the ROI - I have read and gone through the pages for vtkMRMLAnnotationROINode and vtkMRMLCropVolumeParametersNode. As per an earlier post, this should be doable through the Annotation ROI Node but after many hours, can’t figure out. Could someone please provide a code snipped or guide me to the correct function etc. for setting the dimensions, as shown in the picture attached, automatically - for example a tuple (69, 93, 227) ?</p>
<p>Thank you</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9cea672960b20d8ec33bddc0a46bbabe9098eb2.png" data-download-href="/uploads/short-url/sNgIuehCnat3CSv7K4xzO1JDeoO.png?dl=1" title="Screenshot 2021-07-20 at 5.03.51 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9cea672960b20d8ec33bddc0a46bbabe9098eb2_2_645x500.png" alt="Screenshot 2021-07-20 at 5.03.51 AM" data-base62-sha1="sNgIuehCnat3CSv7K4xzO1JDeoO" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9cea672960b20d8ec33bddc0a46bbabe9098eb2_2_645x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9cea672960b20d8ec33bddc0a46bbabe9098eb2_2_967x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9cea672960b20d8ec33bddc0a46bbabe9098eb2.png 2x" data-dominant-color="F3F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-07-20 at 5.03.51 AM</span><span class="informations">1066×826 64.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-08-03 17:42 UTC)

<p>You can set the Annotation ROI center and radius as shown <a href="https://discourse.slicer.org/t/how-to-get-a-roi-to-fit-volume-in-the-volume-rendering-module-with-python/18793/7">here</a>. I would recommend to switch to the Markups ROI node, as it is more powerful (e.g., it can represent an ROI with rotated axes) and it will completely replace Annotation ROIs in a year or two.</p>

---
