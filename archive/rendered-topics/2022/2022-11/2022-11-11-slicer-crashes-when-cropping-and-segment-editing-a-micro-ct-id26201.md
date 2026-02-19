---
topic_id: 26201
title: "Slicer Crashes When Cropping And Segment Editing A Micro Ct"
date: 2022-11-11
url: https://discourse.slicer.org/t/26201
---

# Slicer crashes when cropping and segment editing a micro-CT image

**Topic ID**: 26201
**Date**: 2022-11-11
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-cropping-and-segment-editing-a-micro-ct-image/26201

---

## Post #1 by @Sam_Giancarli (2022-11-11 18:44 UTC)

<p>I’m running into issues when I try to work with volumes that require a transform to fix spacing issues between images (although sometimes the “differences detected” in spacing is something like 0.026 to 0.026). Everything i try to do–crop volume, use the segment editor–crashes the entire application or I get a message that the application has run out of memory (I don’t get this when i work with old datasets of mine.)</p>

---

## Post #2 by @lassoan (2022-11-11 18:46 UTC)

<p>It seems that the data set is corrupted or has some unexpected properties. If you can provide an example data set (upload somewhere and post the link here) and instructions for reproducing the issue then we can investigate.</p>

---

## Post #3 by @Sam_Giancarli (2022-11-14 21:19 UTC)

<p>thanks! I’ve uploaded it to a Google Drive folder:<br>
<a href="https://drive.google.com/drive/folders/1DmumfwJgr9DIR5CUUgKFGeNZ96HrL7KY?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1DmumfwJgr9DIR5CUUgKFGeNZ96HrL7KY?usp=sharing</a></p>

---

## Post #4 by @lassoan (2022-11-14 22:57 UTC)

<p>Thank you, it was very useful to see the data that you work with. It looks like this is a micro-CT with the usual issues (very large image, 2036x2018x268 voxels, <code>double</code> voxel type, voxel values not calibrated to be in Haunsfield units, etc.), so it is useful to cast the voxel to integer, calibrate intensity, crop&amp;resample, etc.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> is there a tutorial that explains how to make these micro-CT images to make it more palatable for Slicer?</p>
<p>That said, without doing any of these tune-ups on the image, I was able to load, volume render, segment the image without issues.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/645f531eda7edac65f15f675cb202241b7220682.jpeg" data-download-href="/uploads/short-url/ejVYIeLTCVnrxov15pF4toED4ZA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/645f531eda7edac65f15f675cb202241b7220682_2_690x389.jpeg" alt="image" data-base62-sha1="ejVYIeLTCVnrxov15pF4toED4ZA" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/645f531eda7edac65f15f675cb202241b7220682_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/645f531eda7edac65f15f675cb202241b7220682_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/645f531eda7edac65f15f675cb202241b7220682_2_1380x778.jpeg 2x" data-dominant-color="9A9C9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1085 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Since the image size is about 4.5GB, I would recommend to have at least 45GB physical memory (RAM) in your computer. Many computers don’t have this much memory, so most likely the error message that you got about running out of memory is accurate.</p>
<p>Ideally, you should upgrade your system to have more physical memory, but as a workaround you can change your system settings to allocate more virtual memory. This will avoid getting out of memory error, but the software can slow down a lot. You may also use a stronger computer, with more memory to load the image and crop, downsample, cast to integer, which may reduce the image size that much that you can edit it on less powerful computers.</p>

---

## Post #5 by @muratmaga (2022-11-15 03:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26201">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> is there a tutorial that explains how to make these micro-CT images to make it more palatable for Slicer?</p>
</blockquote>
</aside>
<p>We tried at some point how to use simple filters to rescale intensity ranges, and possibly convert the data to 8 bit. However, this sometimes interpreted as a strict rule to work with the data in Slicer, with some poor results (like loss of intensity or detail). Though, for this dataset double sounds like a unnecessarily large data type.</p>
<p>Nowadays, my suggestion for people who do not have heaps of RAM and want to do segmentation in Slicer with large dataset is strategic use of <code>ImageStacks</code> to only load a certain region, segment that, save the result, and start afresh with a different region to segment the new region. Although this dataset looks like dicom, so ImageStacks won’t be much of use, but the idea still applies. I tell people to benefit from the fact that the physical coordinates continue to line up even in cropped volumes and use partial (but full detail volumes) to segment.</p>

---
