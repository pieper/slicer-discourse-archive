---
topic_id: 4978
title: "New Segment Editor Feature Masking In Grow From Seeds Effect"
date: 2018-12-05
url: https://discourse.slicer.org/t/4978
---

# New Segment Editor feature: masking in Grow from seeds effect

**Topic ID**: 4978
**Date**: 2018-12-05
**URL**: https://discourse.slicer.org/t/new-segment-editor-feature-masking-in-grow-from-seeds-effect/4978

---

## Post #1 by @lassoan (2018-12-05 19:44 UTC)

<p>In the past, “Grow from seeds” effect ignored masking settings. Now region growing can be restricted to certain areas by using “Masking” section in the Segment Editor. Masked area can be defined by image intensity range and/or existing segments.</p>
<p>This can be used for segmenting objects that cannot be easily separated because they have similar image intensity and they are very close to each other (or even fused together in some places). Applications include femur head and hip bone segmentation; or separating vertebrae from each other and from ribs during spine segmentation. The method can be also used for refining or splitting an already created segment.</p>
<p>See this short video how masking simplifies femur segmentation:</p>
<div class="lazyYT" data-youtube-id="8Nbi1Co2rhY" data-youtube-title="Femur segmentation using masked region growing in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>The feature is available in today’s nightly Slicer version. Any feedback or questions are welcome.</p>

---

## Post #2 by @sarvpriya1985 (2018-12-06 15:32 UTC)

<p>Hi,<br>
How can I update my version to 4.11. I ca’t see the option.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #3 by @lassoan (2018-12-06 15:42 UTC)

<p>What option you do not see?</p>

---

## Post #4 by @sarvpriya1985 (2018-12-06 15:43 UTC)

<p>I mean updating it to new version. Do i need to reinstall slicer or is there an option to just update it.</p>
<p>Sarv</p>

---

## Post #5 by @lassoan (2018-12-06 15:47 UTC)

<p>You need to install the latest nightly version of Slicer. No new user interface elements will appear compared to earlier versions, just the behavior is changed.</p>

---

## Post #6 by @Flav1u (2018-12-15 10:53 UTC)

<p>I downloaded the dicom images from the link given in the video description (TCGA-PRAD) subject TCGA-VP-A878. Opening the dicoms in 3D Slicer version 4.10 or 4.11.0 is showing me weird images. Please see image attached. What am I doing wrong?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/956e413cca16d761a390592ffe24c18629830bbb.png" data-download-href="/uploads/short-url/ljVmvkqxnBCcAwdzEneqM3vQMgH.png?dl=1" title="20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/956e413cca16d761a390592ffe24c18629830bbb_2_655x500.png" alt="20" data-base62-sha1="ljVmvkqxnBCcAwdzEneqM3vQMgH" width="655" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/956e413cca16d761a390592ffe24c18629830bbb_2_655x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/956e413cca16d761a390592ffe24c18629830bbb_2_982x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/956e413cca16d761a390592ffe24c18629830bbb.png 2x" data-dominant-color="3B3B47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20</span><span class="informations">1267×966 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2018-12-15 13:18 UTC)

<p>If you just drag-and-drop a single file then by default only that single file is loaded. In general it is recommended to use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM" rel="nofollow noopener">DICOM</a> module to load DICOM data sets.</p>

---

## Post #8 by @dyollb (2022-09-16 08:38 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I tried to follow the video you linked above, to separate an existing (single segment) segmentation of the skull and mandible into two segments: skull_segment and mandible_segment.</p>
<p>The video uses thresholding to set the mask, but my image data is MRI so thresholding does not work very well. Also, I already have a skull and mandible mask.</p>
<p>I am unclear if in this case I should create two additional masks (and use the input mask as masking region) to use grow from seeds. If I start painting seeds for skull_segment and mandible_segment, grow from seeds seems to do nothing.</p>
<p>I also tried masking my MRI and then using only two segments, and selecting “Editable intensity range [0.1, 300.0]” to immitate what the video is doing. Again, grow from seeds is not doing anything (segments are not modified).</p>
<p>Any help would be appreciated.<br>
Thanks, Bryn</p>

---

## Post #9 by @dyollb (2022-09-16 08:45 UTC)

<p>Update:<br>
I tried the second approach again, i.e. masking my MRI with the pre-existing mask and then using only two segments, and selecting “Editable intensity range [0.1, 300.0]” again, and this time it worked. Not sure what I did wrong before. Maybe I pressed “Apply” before the update was done - not sure…</p>

---
