# Create equidistant points along curve for automated measurements

**Topic ID**: 19870
**Date**: 2021-09-26
**URL**: https://discourse.slicer.org/t/create-equidistant-points-along-curve-for-automated-measurements/19870

---

## Post #1 by @nabilgh (2021-09-26 15:26 UTC)

<p>Hello. Is it possible to create equidistant fiducials on a curve (in a module or script)? It means i need to divide a curved into a certain number of points in order to perform automated measurements from these points to a segmented model (using the fiducials to model distance module) such as in the attached screenshot.<br>
Thank you</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1792911534689e1f3dd08583ffcc858573d50152.jpeg" data-download-href="/uploads/short-url/3mwZYqsanfG2FNQRFq8ezu3AQLg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1792911534689e1f3dd08583ffcc858573d50152_2_690x445.jpeg" alt="image" data-base62-sha1="3mwZYqsanfG2FNQRFq8ezu3AQLg" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1792911534689e1f3dd08583ffcc858573d50152_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1792911534689e1f3dd08583ffcc858573d50152.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1792911534689e1f3dd08583ffcc858573d50152.jpeg 2x" data-dominant-color="4A4F4A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">940×607 61.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2021-09-26 18:37 UTC)

<p>You want to use the Resample tab of the Curves markup type. If you don’t want to overwrite the existing manually draw cure, choose to create a new curve.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdbf8d6fda0d906ad2f1700a7e21e106cf1f3114.png" data-download-href="/uploads/short-url/r4ADKSuD6GfaTvj7d1SFVM21RXu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdbf8d6fda0d906ad2f1700a7e21e106cf1f3114.png" alt="image" data-base62-sha1="r4ADKSuD6GfaTvj7d1SFVM21RXu" width="610" height="500" data-dominant-color="F1F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">702×575 16.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
