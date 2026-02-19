---
topic_id: 18436
title: "Converting Pathological Results To 3D"
date: 2021-06-30
url: https://discourse.slicer.org/t/18436
---

# Converting Pathological Results to 3D

**Topic ID**: 18436
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/converting-pathological-results-to-3d/18436

---

## Post #1 by @arif (2021-06-30 16:35 UTC)

<p>Hi dear slicer users;</p>
<p>I am trying to convert pathological results to 3D. But my results are not usable.  I know that with 8 slices to use, I won’t get any good surface or the best accuracy, but if you have any suggestions on how to make a better model out of what I have, I will appreciate it so much.</p>
<p>-1st image 3d model</p>
<p>-2nd image pathology report</p>
<p>-3rd image how we load the pathological images to slicer( for every instance of the pathological report we use a white canvas and then paste the pathological image to that canvas)</p>
<p>Kind regards</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e864863ff11e0a5052ecc7b5861a4750d9a4f049.png" data-download-href="/uploads/short-url/x9Q925QBhFSlXwA0FOS3DNRRyRz.png?dl=1" title="Image 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e864863ff11e0a5052ecc7b5861a4750d9a4f049_2_638x500.png" alt="Image 1" data-base62-sha1="x9Q925QBhFSlXwA0FOS3DNRRyRz" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e864863ff11e0a5052ecc7b5861a4750d9a4f049_2_638x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e864863ff11e0a5052ecc7b5861a4750d9a4f049.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e864863ff11e0a5052ecc7b5861a4750d9a4f049.png 2x" data-dominant-color="878DB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 1</span><span class="informations">736×576 49.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f66e9dfca36e0c910d4e2248121526c861cc86c.jpeg" data-download-href="/uploads/short-url/dBXQLfwsUmVxqQs0cFdKmMZQP3S.jpeg?dl=1" title="Image 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f66e9dfca36e0c910d4e2248121526c861cc86c_2_649x500.jpeg" alt="Image 2" data-base62-sha1="dBXQLfwsUmVxqQs0cFdKmMZQP3S" width="649" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f66e9dfca36e0c910d4e2248121526c861cc86c_2_649x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f66e9dfca36e0c910d4e2248121526c861cc86c_2_973x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f66e9dfca36e0c910d4e2248121526c861cc86c_2_1298x1000.jpeg 2x" data-dominant-color="7F7E7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 2</span><span class="informations">4614×3554 1.04 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ea140a1111589aa85d861122d80f2fd3091c288.jpeg" data-download-href="/uploads/short-url/fMG0dDgiY9MTAgYEm5J0A1SQ43u.jpeg?dl=1" title="Image 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea140a1111589aa85d861122d80f2fd3091c288_2_557x500.jpeg" alt="Image 3" data-base62-sha1="fMG0dDgiY9MTAgYEm5J0A1SQ43u" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea140a1111589aa85d861122d80f2fd3091c288_2_557x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea140a1111589aa85d861122d80f2fd3091c288_2_835x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea140a1111589aa85d861122d80f2fd3091c288_2_1114x1000.jpeg 2x" data-dominant-color="DBDCDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 3</span><span class="informations">1325×1189 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-06-30 18:55 UTC)

<p>Yes, this will be hard to get perfect, but you can at least make it look smoother if you change the spacing.   Use this button in Segment Editor and change to isotropic spacing, perhaps with down sampling.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3275c1b9d967c28c690fbfe058abad7f9e60c471.png" alt="image" data-base62-sha1="7coaiN3TayXIogqqMeyi4J7ILKx" width="255" height="156"></p>

---
