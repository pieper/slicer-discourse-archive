---
topic_id: 25545
title: "Markup To Model"
date: 2022-10-04
url: https://discourse.slicer.org/t/25545
---

# Markup to Model

**Topic ID**: 25545
**Date**: 2022-10-04
**URL**: https://discourse.slicer.org/t/markup-to-model/25545

---

## Post #1 by @rtolia (2022-10-04 14:00 UTC)

<p>Hi, I am trying to do lead segmentation and part of that process is tracing the lead trajectory with Markups to Model and using Markup Fiducial to create points along the lead, so that they match the trajectory, however, I am struggling to do this as the 3D view does not place it on the correct position, as shown below, please help! Is there some other view that would make this easier as I cannot use the planar views.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47ba878051843001beb1c09f8178b2d50358174e.png" data-download-href="/uploads/short-url/aexxkud53IdAo6IOvwCJvuau5JA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47ba878051843001beb1c09f8178b2d50358174e_2_690x364.png" alt="image" data-base62-sha1="aexxkud53IdAo6IOvwCJvuau5JA" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47ba878051843001beb1c09f8178b2d50358174e_2_690x364.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47ba878051843001beb1c09f8178b2d50358174e_2_1035x546.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47ba878051843001beb1c09f8178b2d50358174e_2_1380x728.png 2x" data-dominant-color="B5B9DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1015 271 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9c7d90d060dfdf4e4f61bb5c81e41e0cbdb0aa4.png" data-download-href="/uploads/short-url/sN28U3r40nrMKqAProNUMJH1gCE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9c7d90d060dfdf4e4f61bb5c81e41e0cbdb0aa4_2_690x352.png" alt="image" data-base62-sha1="sN28U3r40nrMKqAProNUMJH1gCE" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9c7d90d060dfdf4e4f61bb5c81e41e0cbdb0aa4_2_690x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9c7d90d060dfdf4e4f61bb5c81e41e0cbdb0aa4_2_1035x528.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9c7d90d060dfdf4e4f61bb5c81e41e0cbdb0aa4_2_1380x704.png 2x" data-dominant-color="B0B6D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1842×942 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2022-10-04 23:45 UTC)

<p>Is the issue that the points are being added on the surface of the lead instead of the center?  If that’s the issue you can click the point in the the 3D view to jump the slices to that point and adjust them to the center of the lead.</p>

---

## Post #3 by @rtolia (2022-10-04 23:54 UTC)

<p>Thank you!! Yes that was the issue!</p>

---
