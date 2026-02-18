# Using ImageJ segmentations with Pyradiomics

**Topic ID**: 20835
**Date**: 2021-11-30
**URL**: https://discourse.slicer.org/t/using-imagej-segmentations-with-pyradiomics/20835

---

## Post #1 by @Sari_Khalil (2021-11-30 01:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30fba87c1eb541d12d3c92391f1e18e98f21d81c.png" data-download-href="/uploads/short-url/6Zk5O3LBsS0WtAReZpOn1DgxJ6s.png?dl=1" title="Screen Shot 2021-11-29 at 8.18.49 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30fba87c1eb541d12d3c92391f1e18e98f21d81c_2_690x339.png" alt="Screen Shot 2021-11-29 at 8.18.49 PM" data-base62-sha1="6Zk5O3LBsS0WtAReZpOn1DgxJ6s" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30fba87c1eb541d12d3c92391f1e18e98f21d81c_2_690x339.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30fba87c1eb541d12d3c92391f1e18e98f21d81c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30fba87c1eb541d12d3c92391f1e18e98f21d81c.png 2x" data-dominant-color="747373"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-11-29 at 8.18.49 PM</span><span class="informations">742×365 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello,<br>
I want to convert a deck of segmentations of multiple slices in a CT image made using ImageJ into usable input for pyRadiomics. For example, in the attached screenshot, you can see that I have 3 segmentations, one per slice in the CT (outlining a portion of a kidney tumor), and my goal is to save all three of them into a usable mask for pyradiomics, e.g., an nrrd file, so that the radiomic features are extracted only from the area inside each segmentation. Is this possible?</p>
<p>Thanks!<br>
S</p>

---

## Post #2 by @muratmaga (2021-11-30 02:37 UTC)

<p>Should be real simple, if you  use Fiji, which supports exporting NRRD.</p>

---

## Post #3 by @Sari_Khalil (2021-12-01 12:33 UTC)

<p>Not really - the issue is that there are several slices here, each with their own segmentation, and when I save the image as nrrd, none of these segmentations show up on the nrrd file. I then tried to save the segmentations as an overlay (Image &gt; Overlay &gt; From ROI manager), but the overlay is done for a single ROI at a time. Am I missing something?</p>

---

## Post #4 by @muratmaga (2021-12-01 17:37 UTC)

<p>I am not all that knowledgeable with ImageJ/Fiji. I expect you should be able to export each of your ROI to its own imagestack first, and then save as NRRD. But that’s as much as I can help.</p>
<p>If you do not have extensive segmentation, it might be faster to redo the segmentations in Slicer and avoid all these issues.</p>

---

## Post #5 by @Sari_Khalil (2021-12-05 13:15 UTC)

<p>Got it. Yeah, I think it would be easier to redo this in 3D slicer. Unfortunately, it’s a bit of work regardless of what I end up doing - a former colleague left me with 150 meticulously segmented dicoms using Fiji, and I was trying to salvage them. Thanks.</p>
<p>S</p>

---

## Post #6 by @muratmaga (2021-12-05 15:35 UTC)

<p>Then, ask in Fiji forums how you can turn those segment to separate binary image sequences. Once you do that, rest should be more straightforward.</p>

---
