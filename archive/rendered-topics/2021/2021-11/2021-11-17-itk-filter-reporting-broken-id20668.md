---
topic_id: 20668
title: "Itk Filter Reporting Broken"
date: 2021-11-17
url: https://discourse.slicer.org/t/20668
---

# ITK Filter... reporting broken?

**Topic ID**: 20668
**Date**: 2021-11-17
**URL**: https://discourse.slicer.org/t/itk-filter-reporting-broken/20668

---

## Post #1 by @Fluvio_Lobo (2021-11-17 18:41 UTC)

<p>Hello,</p>
<p>I am following <a href="https://discourse.slicer.org/t/most-efficient-way-of-creating-a-thickness-map/18203">this workflow</a>, but the <strong>BinaryThinningImageFilter</strong> takes an incredible amount of time to process without any indication of progress. I found a <a href="https://discourse.slicer.org/t/simplefilters-binarythinningimagefilter-not-working-in-latest-macos-build/10403">post from 2020</a> that talked about the issue, but no clear indication of a fix.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6dc5ec4b8211e623d602a131d43f9ab04258893.jpeg" data-download-href="/uploads/short-url/zdPB7l04BiSIsCT3JRiPJMMgQDh.jpeg?dl=1" title="plasty.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6dc5ec4b8211e623d602a131d43f9ab04258893_2_690x373.jpeg" alt="plasty.PNG" data-base62-sha1="zdPB7l04BiSIsCT3JRiPJMMgQDh" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6dc5ec4b8211e623d602a131d43f9ab04258893_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6dc5ec4b8211e623d602a131d43f9ab04258893_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6dc5ec4b8211e623d602a131d43f9ab04258893_2_1380x746.jpeg 2x" data-dominant-color="3D3D42"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">plasty.PNG</span><span class="informations">1920×1040 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The process took <strong>808.sec (or 13 mins)</strong> for the implant seen above.</p>
<p>I am using the latest Preview version of Slicer <strong>4.13.0-2021-11-16 r30403 / 0e7423f</strong></p>
<p>Is there a solution? Am I doing something wrong with the implementation of the filter?</p>

---
