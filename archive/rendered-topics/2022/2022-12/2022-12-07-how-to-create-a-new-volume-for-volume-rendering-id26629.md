---
topic_id: 26629
title: "How To Create A New Volume For Volume Rendering"
date: 2022-12-07
url: https://discourse.slicer.org/t/26629
---

# How to Create a new Volume for Volume Rendering

**Topic ID**: 26629
**Date**: 2022-12-07
**URL**: https://discourse.slicer.org/t/how-to-create-a-new-volume-for-volume-rendering/26629

---

## Post #1 by @act (2022-12-07 15:04 UTC)

<p>Hi,<br>
I have a MR dicom data and I want to view 3D with volume rendering. Folder include 3 volume but each volume contain only one clear part (as shown in image). My purpose is create a new volume that includes clear parts from other volumes. Is that possible? If possible how can i do step by step.</p>
<p>Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd5ec6fe64d805fd4ab3e6bb468f7e9dfe20a3a0.jpeg" data-download-href="/uploads/short-url/r1fiGwrNuR9yVIveABx89rOKQSI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5ec6fe64d805fd4ab3e6bb468f7e9dfe20a3a0_2_690x380.jpeg" alt="image" data-base62-sha1="r1fiGwrNuR9yVIveABx89rOKQSI" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5ec6fe64d805fd4ab3e6bb468f7e9dfe20a3a0_2_690x380.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5ec6fe64d805fd4ab3e6bb468f7e9dfe20a3a0_2_1035x570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5ec6fe64d805fd4ab3e6bb468f7e9dfe20a3a0_2_1380x760.jpeg 2x" data-dominant-color="55576B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1805×996 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-12-07 15:53 UTC)

<p>This question comes up fairly often, but it’s unfortunately hard to search for in discourse.</p>
<p>This thread summarizes what I believe you are facing:</p>
<aside class="quote quote-modified" data-post="1" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f19dbf/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Mac - High Sierra 
Slicer version: 4.8.1 
Expected behavior: One perfect, high resolution volume 
Actual behavior: Three volumes, each one being high resolution in only one plane (sagittal, coronal, transverse) 
I have been using 3D Slicer for many months and I’m slowly learning the ropes. I am using it to produce anatomical boney models, and have probably created between 10-15 models. 
After loading CT scans from their DICOM folder I always get several volumes, often with the …
  </blockquote>
</aside>


---
