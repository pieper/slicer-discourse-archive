---
topic_id: 38351
title: "Pulling A Skull From Mr"
date: 2024-09-12
url: https://discourse.slicer.org/t/38351
---

# Pulling a skull from MR

**Topic ID**: 38351
**Date**: 2024-09-12
**URL**: https://discourse.slicer.org/t/pulling-a-skull-from-mr/38351

---

## Post #1 by @BDhoth (2024-09-12 15:45 UTC)

<p>Are there any tips for pulling a skull from MRI images? In this sequence the skull is very comparable in the number as other brain matter/soft tissue.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3ff7f1ccb04c46379f3e2af3dc2a46452048561.png" alt="Screenshot 2024-09-12 104236" data-base62-sha1="noNe2AI646rvZwptASNLPXIYNEJ" width="639" height="451"></p>

---

## Post #2 by @lassoan (2024-09-13 03:50 UTC)

<p>I woild recommend the HDBrainExtraction extension for skull stripping. See some more details in this recent discussion:</p>
<aside class="quote" data-post="6" data-topic="36924">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/brain-segmentation-in-mr/36924/6">Brain Segmentation in MR</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It looks like you correctly created a brain mask segmentation in white, and a new skull-stripped volume.  The green segment looks like it is from a different segmentation node created from threshold of the image before skull stripping. 
If you go back to the data view, you can turn off the node named ‘Segmentation’ with the green head label to see only the brain mask label in white.
  </blockquote>
</aside>


---

## Post #3 by @BDhoth (2024-09-13 17:18 UTC)

<p>I use the HD brain extraction to get a brain segmentation, but this can be used to KEEP only the skull??<br>
Thank you!</p>

---

## Post #4 by @lassoan (2024-09-13 18:51 UTC)

<p>Yes, sure, you can blank out the brain region by a few clicks.</p>
<ul>
<li>Create <code>Brain segmentation</code> output in <code>HD Brain Extraction Tool</code> module</li>
<li>Go to <code>Segment Editor</code> module</li>
<li>Click <code>Mask volume</code> effect, <code>Fill inside</code>, and <code>Apply</code></li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67d7e6d6503c8da084e5016c96e79e6ff52e6a6d.jpeg" data-download-href="/uploads/short-url/eODKir2MyX4NgLOjzC6DfHnbS2x.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67d7e6d6503c8da084e5016c96e79e6ff52e6a6d_2_690x498.jpeg" alt="image" data-base62-sha1="eODKir2MyX4NgLOjzC6DfHnbS2x" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67d7e6d6503c8da084e5016c96e79e6ff52e6a6d_2_690x498.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67d7e6d6503c8da084e5016c96e79e6ff52e6a6d_2_1035x747.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67d7e6d6503c8da084e5016c96e79e6ff52e6a6d_2_1380x996.jpeg 2x" data-dominant-color="343431"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1387 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @BDhoth (2024-10-04 12:24 UTC)

<p>I tried this option, but it doesn’t work the best for getting only the skull. When thresholding it merges right with how it was masked. ANy other options to get a skull only, no soft tissue? Thank you for your help!</p>
<p>Becky</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3aa18a719f156d59e924e93a3c992e35675d302.png" data-download-href="/uploads/short-url/pDnTBuUV6LMX9zFk3lkFqcTSBlo.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3aa18a719f156d59e924e93a3c992e35675d302_2_353x500.png" data-base62-sha1="pDnTBuUV6LMX9zFk3lkFqcTSBlo" alt="image.png" width="353" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3aa18a719f156d59e924e93a3c992e35675d302_2_353x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3aa18a719f156d59e924e93a3c992e35675d302_2_529x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3aa18a719f156d59e924e93a3c992e35675d302.png 2x" data-dominant-color="7A7B6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">696×985 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @nadayoda59 (2025-01-03 01:02 UTC)

<p>Have you solved this problem? If you have, please share your method. Thank you.</p>

---

## Post #7 by @BDhoth (2025-01-03 13:04 UTC)

<p>No, I have not in a simple way besides going almost slice by slice and interpolating the slices.</p>

---

## Post #8 by @jonel (2025-11-11 20:31 UTC)

<p>If you are still searching for a solution to this problem you might be interested in the new ModalityConverter extension: <a href="https://discourse.slicer.org/t/new-extension-modalityconverter-bringing-ai-medical-image-to-image-translation-to-3d-slicer/44405" class="inline-onebox">New extension: ModalityConverter - bringing AI medical image-to-image translation to 3D Slicer</a> You can use it to generate a synthetic CT from your MRI images, from which you can then easily extract the skull with the Segment Editor.</p>

---
