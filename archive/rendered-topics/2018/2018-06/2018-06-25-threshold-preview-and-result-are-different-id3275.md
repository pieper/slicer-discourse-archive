# Threshold preview and result are different

**Topic ID**: 3275
**Date**: 2018-06-25
**URL**: https://discourse.slicer.org/t/threshold-preview-and-result-are-different/3275

---

## Post #1 by @Fernando (2018-06-25 10:26 UTC)

<p>Hi all,</p>
<p>One clinician I’m working with noticed how he gets more little blobs/islands/connected components than he expected from the segmentation preview after applying a threshold in Segment Editor. Can this be avoided?</p>
<p>Preview:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe5ebd64d0d04df94454597a9ef56e51ffcb5aee.jpeg" data-download-href="/uploads/short-url/AigfUs3A1YpDzC8sFPykxbX7HNc.jpg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe5ebd64d0d04df94454597a9ef56e51ffcb5aee_2_650x500.jpg" alt="Screenshot" data-base62-sha1="AigfUs3A1YpDzC8sFPykxbX7HNc" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe5ebd64d0d04df94454597a9ef56e51ffcb5aee_2_650x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe5ebd64d0d04df94454597a9ef56e51ffcb5aee_2_975x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe5ebd64d0d04df94454597a9ef56e51ffcb5aee.jpeg 2x" data-dominant-color="1D1515"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1235×949 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39a973dd7f5c437337985a991f2e917c09e625f1.jpeg" data-download-href="/uploads/short-url/8e6gvMKvY54xzgHXtNO1L0uJAI1.jpg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39a973dd7f5c437337985a991f2e917c09e625f1_2_650x500.jpg" alt="Screenshot_2" data-base62-sha1="8e6gvMKvY54xzgHXtNO1L0uJAI1" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39a973dd7f5c437337985a991f2e917c09e625f1_2_650x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39a973dd7f5c437337985a991f2e917c09e625f1_2_975x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39a973dd7f5c437337985a991f2e917c09e625f1.jpeg 2x" data-dominant-color="211414"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1235×949 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2018-06-25 10:54 UTC)

<p>The reason for the difference is probably that the preview is applied on the slice view, whatever zoom/etc is used there, and threshold is applied on the actual image data. If she/he doesn’t zoom in too much, and maybe turns off interpolation, then the results should be more similar.<br>
Also it’s possible to use the Islands filter to get rid of the speckes afterwards.</p>

---

## Post #3 by @Fernando (2018-06-25 11:17 UTC)

<p>Turning off interpolation seems to fix it. Thanks <a class="mention" href="/u/cpinter">@cpinter</a>.</p>
<p>We do use the Islands* effect to get rid of small speckles afterwards.</p>
<p><sup>* enjoy the Canary ones!</sup></p>

---

## Post #4 by @cpinter (2018-06-25 12:32 UTC)

<p>Sounds great, thanks!</p>
<p><sup>* We miss you here! Davide, Paolo and the others are saying hi <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></sup></p>

---
