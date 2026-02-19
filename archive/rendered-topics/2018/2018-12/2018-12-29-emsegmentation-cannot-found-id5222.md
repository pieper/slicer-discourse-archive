---
topic_id: 5222
title: "Emsegmentation Cannot Found"
date: 2018-12-29
url: https://discourse.slicer.org/t/5222
---

# Emsegmentation cannot found

**Topic ID**: 5222
**Date**: 2018-12-29
**URL**: https://discourse.slicer.org/t/emsegmentation-cannot-found/5222

---

## Post #1 by @feng (2018-12-29 21:24 UTC)

<p>Cannot found Emsegmentation module in 4.10. Any clue?</p>

---

## Post #2 by @lassoan (2018-12-29 21:59 UTC)

<p>There were no volunteers to maintain this module, so it was phased out. What would you need to segment?</p>

---

## Post #3 by @feng (2018-12-29 22:30 UTC)

<p>I’m segmenting some vocal tracts from MRI data. It takes ages to clip all the teeth out manually in every mri series, so I was thinking if Emsegmentation could help.</p>
<p>I am also thinking if I can extract the teeth and apply it as a mask to every vocal tract from the same person, but I am not sure how that can be achieved.-- it would involve align the teeth extraction to the images and mask it out so the seeds won’t grow into the area of the teeth. Any advice for this?</p>

---

## Post #4 by @lassoan (2018-12-30 03:03 UTC)

<p>You should be able to all this with Segment Editor module. If you can share an image volume (or at least a couple of annotated screenshots) to illustrate what you described then we can give more specific advice.</p>

---

## Post #5 by @feng (2018-12-30 08:32 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b61948eec5e0a0f2ea8f67a964ccb222c254627.png" alt="7-Figure3-1" data-base62-sha1="hBtNd0qQSJB33BaLKA84t7P7LgP" width="628" height="330"></p>
<p>The area without the part in the red circle, which is teeth, is the area I want. As you can see, both teeth and air are black in MRI images, so the teeth will be captured as well if I run growing from seeds after using paint. So I need to remove all the teeth afterward manually which is really time-consuming as I have lots of vocal tract for segmentation.</p>
<p>The thing is I have several vocal tracts for one person and the teeth for one person is the same, so I think it could be sensible to manually select all the teeth area for the person in vocal tract and make it a mask all other vocal tract images for the same person. And when I run growing from seeds, the teeth area will not be included.</p>
<p>The last page shows what I want.</p>
<p>I hope my explanation is clear to read. Thank you.</p>

---

## Post #6 by @lassoan (2018-12-30 14:30 UTC)

<p>This sounds relatively easily doable using grown from seeds effect in recent nightly Slicer versions (Slicer-4.11.x downloaded not longer than 2 weeks ago):</p>
<ul>
<li>Crop and resample the input volume before segmentation using Crop volume module. Crop it to minimal size to reduce memory usage and enable isotropic spacing for optimal propagation of seeds.</li>
<li>Create segments: air (will contain airways inside the head), teeth, and outside (will contain air outside the head and other airways that you would like to exclude from air segment)</li>
<li>In Segment Editor module, use Threshold effect to highlight air intensity range, the click “Use for masking”</li>
<li>Draw seeds using all 3 segments</li>
<li>Click “Show 3D” near Apply button to preview seed growing result in 3D</li>
<li>Use Paint effect to add more seeds to refine results (hold down shift while moving the mouse to see current position in all views)</li>
<li>Click apply when previewed segmentation looks good enough</li>
<li>Reduce noise using Smoothing effect, joint smoothing method (optional)</li>
</ul>
<p>To segment more images, compute registration using “General registration (Elastix)” module (provided by SlicerElastix extension), use the computed transform to warp the seeds to match the new image, harden the transform, then use Grow from seeds effect using these seeds.</p>

---

## Post #7 by @Wahyu (2019-07-10 22:25 UTC)

<p>Hello Everybody,</p>
<p>Most of Tutorial that I can found regarding Automatic Brain Segmentation is by using this EMSegmenter Module. Is there any alternative way to perform it using current module which available?<br>
Thank you in advance</p>
<p>Wahyu</p>

---

## Post #8 by @pieper (2019-07-11 14:35 UTC)

<p>You might want to start with <a href="https://surfer.nmr.mgh.harvard.edu/" rel="nofollow noopener">freesurfer</a>.  It’s independent of slicer but you can load the results.</p>

---

## Post #9 by @Wahyu (2019-07-12 12:14 UTC)

<p>Thanks Steve Pieper, will give it a try.</p>

---
