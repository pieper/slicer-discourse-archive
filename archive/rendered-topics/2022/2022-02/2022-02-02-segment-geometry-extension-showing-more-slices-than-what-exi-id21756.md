# Segment Geometry Extension showing more slices than what exists

**Topic ID**: 21756
**Date**: 2022-02-02
**URL**: https://discourse.slicer.org/t/segment-geometry-extension-showing-more-slices-than-what-exists/21756

---

## Post #1 by @Michel_Atieh (2022-02-02 17:22 UTC)

<p>Hello,<br>
I have noticed when segmenting organs on 3D Slicer that when using the Segment Geometry Extension it shows more slices than what I have contoured. The more the slices I contour the bigger the error (for 60 slices it adds about 15).<br>
For instance in the screenshot below I have drawn only 4 contours without skipping any slice or filling between slices, when I want to get the data that I want, it shows me more slices.<br>
Why is it generating more slices and were are those values coming from?</p>
<p>Thank you</p>

---

## Post #2 by @Michel_Atieh (2022-02-02 17:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f415999ade60bfbf5ff6166b212bc72055d0598.jpeg" data-download-href="/uploads/short-url/i9KEkrkHZ34WyzXZUwboGaFh01i.jpeg?dl=1" title="Screenshot from 2022-02-02 18-15-03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f415999ade60bfbf5ff6166b212bc72055d0598_2_690x399.jpeg" alt="Screenshot from 2022-02-02 18-15-03" data-base62-sha1="i9KEkrkHZ34WyzXZUwboGaFh01i" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f415999ade60bfbf5ff6166b212bc72055d0598_2_690x399.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f415999ade60bfbf5ff6166b212bc72055d0598_2_1035x598.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f415999ade60bfbf5ff6166b212bc72055d0598_2_1380x798.jpeg 2x" data-dominant-color="4F4F4C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-02-02 18-15-03</span><span class="informations">1920×1111 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @jmhuie (2022-02-18 17:38 UTC)

<p>Hi <a class="mention" href="/u/michel_atieh">@Michel_Atieh</a> I am the developer of Segment Geometry.</p>
<p>The reason you’re getting those extra slices is because your volume is anisotropic, meaning the image spacing is not the same in all directions, and Segment Geometry is automatically resampling it so that it is isotropic (necessary for volumes that are transformed). But so long as you’re not applying a transform to the volume and segment, the resampling is not necessary. I have pushed a change to Segment Geometry, so it’ll stop resampling and the output will reflect the exact slices you have segmented. Update will be available tomorrow. Please let me know if that works for you.</p>

---

## Post #4 by @Michel_Atieh (2022-02-19 11:19 UTC)

<p>Hello <a class="mention" href="/u/jmhuie">@jmhuie</a>  thanks for your reply. I have now tried segmenting an organ, and the number of slices in the table matches the number of slices I have drawn on the image.<br>
Thank you so much for the explanation and for the update!</p>

---
