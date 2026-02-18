# Volume measurement of defect with Surface Scan

**Topic ID**: 18501
**Date**: 2021-07-04
**URL**: https://discourse.slicer.org/t/volume-measurement-of-defect-with-surface-scan/18501

---

## Post #1 by @manjula (2021-07-04 06:08 UTC)

<p>What would be the best way to measure the volume of a surface defect with a surface scan.<br>
The surface scan is in the stl format.<br>
I have tried by using converting to segment and creating a blank volume and segmenting the space. It gives results but too many steps are involved.</p>
<p>Is there a better and easier way of getting the volume of the space (defect) ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e356ab5eba001b3a9d0e145b141ba8bc2bb7288.png" data-download-href="/uploads/short-url/8Sk2ZlhKRHjWpOUTyGoaa9iv8AE.png?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e356ab5eba001b3a9d0e145b141ba8bc2bb7288_2_650x499.png" alt="Screenshot_2" data-base62-sha1="8Sk2ZlhKRHjWpOUTyGoaa9iv8AE" width="650" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e356ab5eba001b3a9d0e145b141ba8bc2bb7288_2_650x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e356ab5eba001b3a9d0e145b141ba8bc2bb7288_2_975x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e356ab5eba001b3a9d0e145b141ba8bc2bb7288.png 2x" data-dominant-color="535269"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1250×961 53 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-07-07 16:48 UTC)

<p>It sounds like this would be another good task for the baffle planner tool.  You could create the cap over the defect and then fill a new segment inside to measure.</p>

---
