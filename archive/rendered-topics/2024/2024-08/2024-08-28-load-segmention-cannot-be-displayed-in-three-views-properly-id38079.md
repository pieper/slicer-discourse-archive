---
topic_id: 38079
title: "Load Segmention Cannot Be Displayed In Three Views Properly"
date: 2024-08-28
url: https://discourse.slicer.org/t/38079
---

# Load segmention cannot be displayed in three views properly

**Topic ID**: 38079
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/load-segmention-cannot-be-displayed-in-three-views-properly/38079

---

## Post #1 by @dingdanpeng (2024-08-28 12:27 UTC)

<p>Operating system:windows11<br>
Slicer version:slicer 5.7.0<br>
Expected behavior:I first opened a nii file for a brain tumor, and then opened a corresponding nii file for segmentation results. In three views, I should be able to display the patient image and segmentation results.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba2c9b211b28b98f87b60c41b116d7eed8dded3e.png" data-download-href="/uploads/short-url/qyYnozTM0P4wz4YyuTmB3GEXxJI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba2c9b211b28b98f87b60c41b116d7eed8dded3e_2_690x272.png" alt="image" data-base62-sha1="qyYnozTM0P4wz4YyuTmB3GEXxJI" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba2c9b211b28b98f87b60c41b116d7eed8dded3e_2_690x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba2c9b211b28b98f87b60c41b116d7eed8dded3e_2_1035x408.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba2c9b211b28b98f87b60c41b116d7eed8dded3e_2_1380x544.png 2x" data-dominant-color="9B9AB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1889×747 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Actual behavior:I first opened a nii file for a brain tumor, and then opened the corresponding segmentation results. The segmentation result does not display properly in the three views.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf18c16efc349d63308ade914751245624b8bc5e.png" data-download-href="/uploads/short-url/rgweBcl6jLP9MHxLHWsrzxejcw6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf18c16efc349d63308ade914751245624b8bc5e_2_690x238.png" alt="image" data-base62-sha1="rgweBcl6jLP9MHxLHWsrzxejcw6" width="690" height="238" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf18c16efc349d63308ade914751245624b8bc5e_2_690x238.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf18c16efc349d63308ade914751245624b8bc5e_2_1035x357.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf18c16efc349d63308ade914751245624b8bc5e_2_1380x476.png 2x" data-dominant-color="BEBFBC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1900×657 85.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-08-28 13:03 UTC)

<p>I suggest you look at some of the basic documentation, for example</p>
<p>The View Data section of Getting started:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#view-data" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#view-data</a></p>
<p>Basic tutorials such as the 4 minute tutorial and the “Data Loading and 3D Visualization” tutorial for 5.x:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4Minute_Tutorial" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4Minute_Tutorial</a></p>

---
