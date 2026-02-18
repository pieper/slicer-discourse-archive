# Combining 3 ScalarVolume/DICOM Files into One?

**Topic ID**: 29702
**Date**: 2023-05-29
**URL**: https://discourse.slicer.org/t/combining-3-scalarvolume-dicom-files-into-one/29702

---

## Post #1 by @ImotVoksim (2023-05-29 00:59 UTC)

<p>Hello, I have an MRI scan whose sagittal, coronal, and transverse DICOM files are separated into 3 files. Or rather, each one of the files is high-dimensional only in one direction, and the other two directions are super sparse. Is there a way I can combine the three files so I end up with a single ScalarVolume/DICOM file of high quality in each direction?</p>
<p>An additional problem is that each of the files has a different number of 2D slices (320, 384, and 272).</p>
<p>Any tips are much appreciated. Nor YouTube, nor Google is returning any useful tutorials.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2023-05-29 02:00 UTC)

<p>This kind of imaging protocol makes sense if the images are only viewed by humans and they only review the acquired 2D image slices (they don’t do any 3D reconstruction). Sadly, this is still standard clinical practice at many hospitals. See more information in this topic:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In general, these multiple low-resolution acquisitions are not well suited for any 3D processing, so the best would be to acquire proper 3D volume, with as isotropic spacing (cubic voxel shape) as possible. 
You may try to find toolkits that can create an isotropic super-resolution image from multiple low-resolution sweeps, but this is a difficult image reconstruction problem, so there are no standard solutions. Have a look at this post <a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/6">Import volume by projections</a> for info on a toolkit that mig…
  </blockquote>
</aside>


---

## Post #3 by @ImotVoksim (2023-06-12 07:56 UTC)

<p>Thanks Andras, I did what you described in the linked post - used the 3 volumes individually to create a high-resolution segment. It’s a bit painstaking but it worked as intended. Cheers.</p>

---

## Post #4 by @mau_igna_06 (2023-06-12 18:59 UTC)

<aside class="quote no-group" data-username="ImotVoksim" data-post="3" data-topic="29702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/imotvoksim/48/66152_2.png" class="avatar"> ImotVoksim:</div>
<blockquote>
<p>used the 3 volumes individually to create a high-resolution segment. It’s a bit painstaking but it worked as intended.</p>
</blockquote>
</aside>
<p>Hi. Do you have a code snippet for this? I’m curious to see its results</p>

---

## Post #5 by @ImotVoksim (2023-06-16 08:23 UTC)

<p>Hi Mauro, I just did it by hand. Switching between the three master views and painting in my segmentation manually (using Grow from Seed and then some polishing)</p>

---
