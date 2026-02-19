---
topic_id: 29817
title: "Lagging And Freezing With Segment Editor When Working On A L"
date: 2023-06-03
url: https://discourse.slicer.org/t/29817
---

# Lagging and Freezing with Segment Editor when working on a large (10GB) CT image

**Topic ID**: 29817
**Date**: 2023-06-03
**URL**: https://discourse.slicer.org/t/lagging-and-freezing-with-segment-editor-when-working-on-a-large-10gb-ct-image/29817

---

## Post #1 by @ckleindl (2023-06-03 18:46 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.2.2<br>
Expected behavior: Segmenting to be recorded<br>
Actual behavior: Lagging and freezing. No segmenting is recorded after done loading.</p>
<p>Hi, I am new to 3D slicer and am using this software to segment CT scans for a research project. I was able to do a sample as provided by the software with no issues. After downloading my CT scans that are 10GB in size I am now having issues. When using the threshold application my Slicer app just closes and nothing is saved. When using the level tracing application and click to segment something, it doesn’t actually segment the section. Instead, the screen freezes and nothing saves. I have tried this on both of my laptops and seem to be having issues with both. Not sure if it matters but the current one I am trying has 16 GB RAM and 474 GB storage. Any help is greatly appreciated. Thank you!</p>

---

## Post #2 by @lassoan (2023-06-03 18:53 UTC)

<p>For segmenting a 10GB image you need minimum 30-50GB memory to store the segmentation and working buffers (e.g., partial computation results). Since you don’t have that much physical RAM, all operations become several magnitudes slower.</p>
<p>For a CT of 10GB size I would recommend at least 100GB of RAM, and a fast CPU (preferably 4GHz clock speed) with large cache.</p>
<p>If that is not feasible, you can use Crop volume module to remove the irrelevant image regions and/or resample the image to reduce its size. If you load from non-DICOM images then you can use ImageStacks module of SlicerMorph extension to load a lower-resolution cropped version directly.</p>

---

## Post #3 by @ckleindl (2023-06-03 19:15 UTC)

<p>Thank you for the fast response! I am attempting to crop the images and am now getting this error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97286eba380a3586fc7f7dfaf0cc5c8b3cd65091.png" data-download-href="/uploads/short-url/lzcIUkvo6uB4ayaLzlG4NlGzfln.png?dl=1" title="Screenshot (27)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97286eba380a3586fc7f7dfaf0cc5c8b3cd65091_2_690x388.png" alt="Screenshot (27)" data-base62-sha1="lzcIUkvo6uB4ayaLzlG4NlGzfln" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97286eba380a3586fc7f7dfaf0cc5c8b3cd65091_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97286eba380a3586fc7f7dfaf0cc5c8b3cd65091_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97286eba380a3586fc7f7dfaf0cc5c8b3cd65091_2_1380x776.png 2x" data-dominant-color="C8C6C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (27)</span><span class="informations">1920×1080 401 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2023-06-03 19:17 UTC)

<p>Bad allocation means that you have ran out of memory space.</p>
<p>You can increase virtual memory size in your Windows system settings to at least 50GB (maybe up to 100GB if you still get out of memory errors). Things will not be any faster but at least you will not run out of memory.</p>

---

## Post #5 by @ckleindl (2023-06-03 20:27 UTC)

<p>Thank you so much! I got it working a little better now after cropping.</p>

---
