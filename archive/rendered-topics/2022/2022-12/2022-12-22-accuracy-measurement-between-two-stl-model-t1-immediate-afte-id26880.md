# Accuracy measurement between two STL model T1 - immediate after surgery T2 one year after surgery

**Topic ID**: 26880
**Date**: 2022-12-22
**URL**: https://discourse.slicer.org/t/accuracy-measurement-between-two-stl-model-t1-immediate-after-surgery-t2-one-year-after-surgery/26880

---

## Post #1 by @wael_telha (2022-12-22 06:30 UTC)

<p>Dear 3D- Slicer Community I am conducting a research regarding the accuracy between two STL model following orthognathic surgery to check the accuracy between model immediate surgery and one  following surgery. the steps I used<br>
1- VOXEL BASE REGISTERATION FOR BOTH CT<br>
2- PRODUCTION OF TWO STL MODEL T1, T2<br>
3. CHOOSING A PICK’N POINT ON THE T2<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a423479b23a6d30ff51c27ae3e7823748fe05360.jpeg" data-download-href="/uploads/short-url/nq1ThfRR9VRw01KF3BPN11dZpmw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a423479b23a6d30ff51c27ae3e7823748fe05360_2_690x388.jpeg" alt="image" data-base62-sha1="nq1ThfRR9VRw01KF3BPN11dZpmw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a423479b23a6d30ff51c27ae3e7823748fe05360_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a423479b23a6d30ff51c27ae3e7823748fe05360_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a423479b23a6d30ff51c27ae3e7823748fe05360_2_1380x776.jpeg 2x" data-dominant-color="CFC8CD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>IN PICK’N POINT I HAVE CHOSEN NON-CORROSPONDING MESHES !!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1805858d7c29dbbe0ef35492fb9096f840315fd.jpeg" data-download-href="/uploads/short-url/n2HQKIszQiD66OM0L6xxVmMOttj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1805858d7c29dbbe0ef35492fb9096f840315fd_2_690x388.jpeg" alt="image" data-base62-sha1="n2HQKIszQiD66OM0L6xxVmMOttj" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1805858d7c29dbbe0ef35492fb9096f840315fd_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1805858d7c29dbbe0ef35492fb9096f840315fd_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1805858d7c29dbbe0ef35492fb9096f840315fd_2_1380x776.jpeg 2x" data-dominant-color="D3CFC6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>IN MODEL TO MODEL DISTANCE WHAT SHALL I USED - SIGNED DISTANCE OR ABSLOUTE DISTANCE<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b22e5fead956b679d3cf56bbff309d563bf03c9d.jpeg" data-download-href="/uploads/short-url/pqglvYqnacLHh4OnE4VgOtrHvg9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b22e5fead956b679d3cf56bbff309d563bf03c9d_2_690x388.jpeg" alt="image" data-base62-sha1="pqglvYqnacLHh4OnE4VgOtrHvg9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b22e5fead956b679d3cf56bbff309d563bf03c9d_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b22e5fead956b679d3cf56bbff309d563bf03c9d_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b22e5fead956b679d3cf56bbff309d563bf03c9d_2_1380x776.jpeg 2x" data-dominant-color="D1CFC6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>IN MESH STATISTICS I NEED TO KNOW THE TRANSVERSE , SAGITTAL AND VERTICAL DISTANCE THAT’S WHY I USED POINT TO POINT X,Y,Z<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5df3c093fb6769c85c8d226664b5b51c0ed1868.jpeg" data-download-href="/uploads/short-url/pWUHooSHe7hOYgvS4LldjDirqhW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5df3c093fb6769c85c8d226664b5b51c0ed1868_2_690x388.jpeg" alt="image" data-base62-sha1="pWUHooSHe7hOYgvS4LldjDirqhW" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5df3c093fb6769c85c8d226664b5b51c0ed1868_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5df3c093fb6769c85c8d226664b5b51c0ed1868_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5df3c093fb6769c85c8d226664b5b51c0ed1868_2_1380x776.jpeg 2x" data-dominant-color="D3BEC1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I NEED YOU HELP CONFIRMING THE STEPS USED ABOVE</p>

---

## Post #2 by @lassoan (2022-12-22 19:05 UTC)

<p>Model to model distance module cannot provide you accurate displacement vectors, as it can only establish point-to-point correspondence based on closest distance, independently for each point.</p>
<p>Instead, you can use the the transform computed in the registration step to get displacement of each mesh point.</p>

---
