---
topic_id: 3119
title: "Different Volumes Statisfics"
date: 2018-06-07
url: https://discourse.slicer.org/t/3119
---

# Different volumes statisfics

**Topic ID**: 3119
**Date**: 2018-06-07
**URL**: https://discourse.slicer.org/t/different-volumes-statisfics/3119

---

## Post #1 by @Ert0 (2018-06-07 21:15 UTC)

<p>I am working with volumes and áreas of cross sectional muscles.<br>
I noticed that the volume and surface areas are different wheter we use<br>
Label Statistics (first picture) or Models (second picture)…<br>
What is the correct volume/área?</p>
<p>Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea76ebbeb6465c8be98dba069b0771e17eeb5332.jpeg" data-download-href="/uploads/short-url/xsavVfn9UYKLKvmnf2s4IixKhr4.jpg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea76ebbeb6465c8be98dba069b0771e17eeb5332_2_690x402.jpg" alt="1" data-base62-sha1="xsavVfn9UYKLKvmnf2s4IixKhr4" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea76ebbeb6465c8be98dba069b0771e17eeb5332_2_690x402.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea76ebbeb6465c8be98dba069b0771e17eeb5332_2_1035x603.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea76ebbeb6465c8be98dba069b0771e17eeb5332_2_1380x804.jpg 2x" data-dominant-color="878986"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1716×1000 464 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92f058be5c445a12eace02b65e290c2262031531.jpeg" data-download-href="/uploads/short-url/kXSEmvTjAVGtmYR98Jo385bUWmB.jpg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92f058be5c445a12eace02b65e290c2262031531_2_690x401.jpg" alt="2" data-base62-sha1="kXSEmvTjAVGtmYR98Jo385bUWmB" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92f058be5c445a12eace02b65e290c2262031531_2_690x401.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92f058be5c445a12eace02b65e290c2262031531_2_1035x601.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92f058be5c445a12eace02b65e290c2262031531_2_1380x802.jpg 2x" data-dominant-color="878985"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1706×992 457 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2018-06-07 21:32 UTC)

<p>Conversion from labelmap to model includes some smoothing, which tends to reduce the volume of the model, so that could explain the discrepancy.</p>
<p>Please let me suggest that you use our next generation segmentation module called Segment Editor. Its usage is very similar to Editor that you use in the 1.5-year old 4.6.2 release, but it has a lot more features and is easier to use. Although it is available in the latest stable, I suggest downloading a recent nightly version, as it is continually improved. You can find some tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">here</a> in case you need them.</p>
<p>To calculate properties of the segmented regions, the Segment Statistics module is the one to use.</p>

---

## Post #3 by @Ert0 (2018-06-07 23:19 UTC)

<p>Thanks, You have been very helpfull!</p>

---
