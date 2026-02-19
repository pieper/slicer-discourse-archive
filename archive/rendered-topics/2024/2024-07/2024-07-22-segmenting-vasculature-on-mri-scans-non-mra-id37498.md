---
topic_id: 37498
title: "Segmenting Vasculature On Mri Scans Non Mra"
date: 2024-07-22
url: https://discourse.slicer.org/t/37498
---

# Segmenting vasculature on MRI scans (non MRA)

**Topic ID**: 37498
**Date**: 2024-07-22
**URL**: https://discourse.slicer.org/t/segmenting-vasculature-on-mri-scans-non-mra/37498

---

## Post #1 by @BDhoth (2024-07-22 13:59 UTC)

<p>What is the best way to segment out vasculature on MRI scans? Normally a post T1 is provided.</p>

---

## Post #2 by @lassoan (2024-07-22 21:36 UTC)

<p>Which vessels? How well they are visible? Can you post a few images?</p>

---

## Post #3 by @BDhoth (2024-07-23 16:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4acbc56997356fcb87a5acfe9d7f3663e9038432.jpeg" data-download-href="/uploads/short-url/aFFUrR4rUbw0YbXgdTkaGsFadQC.jpeg?dl=1" title="Screenshot 2024-07-22 215145" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4acbc56997356fcb87a5acfe9d7f3663e9038432_2_687x499.jpeg" alt="Screenshot 2024-07-22 215145" data-base62-sha1="aFFUrR4rUbw0YbXgdTkaGsFadQC" width="687" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4acbc56997356fcb87a5acfe9d7f3663e9038432_2_687x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4acbc56997356fcb87a5acfe9d7f3663e9038432_2_1030x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4acbc56997356fcb87a5acfe9d7f3663e9038432.jpeg 2x" data-dominant-color="504E59"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-07-22 215145</span><span class="informations">1366×994 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It is very case dependent. Thus far I have just been thresholding and highlighting the areas of concern.<br>
Thank you for your help.</p>

---

## Post #4 by @tsinesh (2024-07-25 12:14 UTC)

<p>Hello Becky,</p>
<p>You are interested in cerebral venes, right?</p>
<p>Try local threshold (you have to install extra modul called SlicerSegmentEditorExtraEffects.)</p>
<p>My tutorial (to get some ideas) how to segment cerebral arteries you can find here. <a href="https://discourse.slicer.org/t/extracting-stl-from-dicom-images-to-generate-brain-arteries-geometry/25215/6" class="inline-onebox">Extracting STL from DICOM images to generate Brain Arteries geometry - #6 by tsinesh</a></p>

---

## Post #5 by @BDhoth (2024-07-31 12:54 UTC)

<p>Thank you for this. I attempted the vesselness filter as I think that would be best for what I need, but maybe the extensions has changed slightly? There were multiple options and none with the “seed point” option.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f72b458349bab227a97f393e560d37c13ff6fab6.png" data-download-href="/uploads/short-url/zgyDVFPZqibZiOyUZobbSVhh1OK.png?dl=1" title="Screenshot 2024-07-31 075148" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f72b458349bab227a97f393e560d37c13ff6fab6_2_690x415.png" alt="Screenshot 2024-07-31 075148" data-base62-sha1="zgyDVFPZqibZiOyUZobbSVhh1OK" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f72b458349bab227a97f393e560d37c13ff6fab6_2_690x415.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f72b458349bab227a97f393e560d37c13ff6fab6_2_1035x622.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f72b458349bab227a97f393e560d37c13ff6fab6_2_1380x830.png 2x" data-dominant-color="94949B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-07-31 075148</span><span class="informations">1784×1073 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @tsinesh (2024-07-31 14:49 UTC)

<p>Yes, your modul look different. I hadfor arteries good experiences with frangi filter.</p>

---
