---
topic_id: 4154
title: "Surface Details In Segmenting"
date: 2018-09-20
url: https://discourse.slicer.org/t/4154
---

# Surface details in segmenting

**Topic ID**: 4154
**Date**: 2018-09-20
**URL**: https://discourse.slicer.org/t/surface-details-in-segmenting/4154

---

## Post #1 by @Melanie (2018-09-20 02:15 UTC)

<p>I am new to slicer. I tried segmenting small bones from 3D DICOM images and the 3 d image quality is not very clear as shown in videos. Like bone surface are not smooth ( if I make it smooth by surface tools module, I lose surface details, don’t I?). Trying to recreate good surface details. Could anyone please advise. Thanks</p>

---

## Post #2 by @lassoan (2018-09-20 03:22 UTC)

<p>Could you paste here a few screenshots to illustrate what kind of input images you have and how the segmented output looks like?</p>

---

## Post #4 by @Melanie (2018-09-20 06:13 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91758dd60dbf6b4a6657dddd1ebadb92db4c2cd2.jpeg" data-download-href="/uploads/short-url/kKN5G6TzKKY13f1Vce3u9x5PS0y.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91758dd60dbf6b4a6657dddd1ebadb92db4c2cd2_2_690x389.jpeg" alt="image" data-base62-sha1="kKN5G6TzKKY13f1Vce3u9x5PS0y" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91758dd60dbf6b4a6657dddd1ebadb92db4c2cd2_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91758dd60dbf6b4a6657dddd1ebadb92db4c2cd2_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91758dd60dbf6b4a6657dddd1ebadb92db4c2cd2_2_1380x778.jpeg 2x" data-dominant-color="BDB8C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1910×1078 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Melanie (2018-09-20 06:17 UTC)

<p>This is as opposed  to the following image unsegmented but built from the same CT scan usi g a dicom viewer. Surface! anatomy is clearer and surfaces are smooth<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36b9d5ea91eac0c5d7a44f44a7fae292d32fbf62.jpeg" alt="image" data-base62-sha1="7O7VVGZ2nm8rJBzIhlxQwFwOaJ4" width="175" height="160"></p>

---

## Post #6 by @cpinter (2018-09-20 14:15 UTC)

<p>The two visualizations are very different. What you segmented is a surface rendering of a surface model created from a labelmap of the segmentation. The image you pasted from the DICOM viewer is a volume rendering, which is a visualization technique directly from the volume. Read a bit on this here:</p><aside class="quote quote-modified" data-post="1" data-topic="524">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b19c9b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524">Save volume rendering as STL file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I am a new user on 3D slicer. 
I was using the display preset feature under volume rendering, and I was wondering if there is a way to save what I was viewing as an .stl or 3D printable file. 
For example, I was viewing a sample MRI using the CT-cardiac3 preset display. 
When I tried to save that specific 3D preset displayed sample in a .stl file, the option was unavailable. 
I was only able to see .vp (volume property), .txt formats. 
Is there a way to accomplish what I desire in 3D slic…
  </blockquote>
</aside>

<p>The segmentation is mostly based on intensities, and is usually not perfect. Also the output of it is a binary mask volume (i.e. labelmap), which is by definition “not smooth”. You can do further smoothing in Segment Editor using the Smoothing effect, or you can increase the smoothing factor applied for the surface conversion under the small arrow next to the Show 3D button.</p>

---

## Post #7 by @Melanie (2018-09-20 14:20 UTC)

<p>Thank you very much <a class="mention" href="/u/cpinter">@cpinter</a>. Does this mean segmenting a small bone of about 15 mm diameter and trying to identify a 1mm sized vascular foramen on the surface is not very accurate, after segmentation.</p>

---

## Post #8 by @cpinter (2018-09-20 14:49 UTC)

<p>If you need small details, and you are able to do a very accurate segmentation, then you could increase the resolution of the segmentation. There is a small box-like icon next to the master volume selector in Segment Editor. If you click it (before segmentation), select your image, then increase the oversamplinc factor to 2, then you get a segmentation twice as high resolution in each direction. That said, your original volume won’t contain more details, so this is only usable if you do manual segmentation.</p>
<p>An idea if you’d like to identify a 1mm feature in the 3D view: do a volume rendering using the Volume Rendering module (select a good preset and then adjust shift to get a good visualization). Look for the foramen, and mark it using a fiducial (tool bar icon showing a blue arrow pointing up with a red dot next to it). Go to the fiducial in the 2D views and mark the exact foramen with the Segment Editor tools, now that you know where to look for it.</p>
<p>I hope this helps at least a bit, I’m not familiar with what you’d like to segment, and not sure how you want to do it.</p>

---

## Post #9 by @lassoan (2018-09-20 14:51 UTC)

<p>This picture shows how to oversample the segmentation by a factor of 2:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3bac3fef3739e859a076f0c67c2b8493e6daf45.png" data-download-href="/uploads/short-url/ud2Ta98BqfUkqyNG1ZGNRE0fZJz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3bac3fef3739e859a076f0c67c2b8493e6daf45_2_402x500.png" alt="image" data-base62-sha1="ud2Ta98BqfUkqyNG1ZGNRE0fZJz" width="402" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3bac3fef3739e859a076f0c67c2b8493e6daf45_2_402x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3bac3fef3739e859a076f0c67c2b8493e6daf45.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3bac3fef3739e859a076f0c67c2b8493e6daf45.png 2x" data-dominant-color="E9ECEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">593×736 56 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @rkikinis (2018-09-20 15:01 UTC)

<p>Hi,<br>
It depends on the resolution of your CT data relative to the size of the structure that you want to see. Lets say you have data with 1mm resolution in all directions, then your 1mm vascular opening is just one voxel.<br>
Best<br>
Ron</p>

---

## Post #11 by @Melanie (2018-09-20 15:01 UTC)

<p>Thank you ever so much <a class="mention" href="/u/cpinter">@cpinter</a>. This DOES help a lot</p>

---

## Post #12 by @Melanie (2018-09-20 15:03 UTC)

<p>Thank you very much. Will try this. Thanks a lot again.</p>

---

## Post #13 by @Melanie (2018-09-20 15:05 UTC)

<p>Thank you very much Ron</p>
<p>Melanie</p>

---
