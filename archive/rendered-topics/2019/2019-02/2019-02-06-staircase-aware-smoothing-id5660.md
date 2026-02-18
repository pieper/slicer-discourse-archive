# Staircase aware smoothing

**Topic ID**: 5660
**Date**: 2019-02-06
**URL**: https://discourse.slicer.org/t/staircase-aware-smoothing/5660

---

## Post #1 by @EricWilson (2019-02-06 17:21 UTC)

<p>I am trying to see if slicer has a built in method for smoothing out the staircase effect on models.<br>
for example, this skull model shows the effect on the back:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eabb9cf7c85200d95627be461516854f0c416af2.jpeg" data-download-href="/uploads/short-url/xuxGCqSOCVGGAPomDJO4bRE4RYm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eabb9cf7c85200d95627be461516854f0c416af2_2_512x500.jpeg" alt="image" data-base62-sha1="xuxGCqSOCVGGAPomDJO4bRE4RYm" width="512" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eabb9cf7c85200d95627be461516854f0c416af2_2_512x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eabb9cf7c85200d95627be461516854f0c416af2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eabb9cf7c85200d95627be461516854f0c416af2.jpeg 2x" data-dominant-color="2D2D2D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">710×693 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>there are certainly papers that outline algorithms to smooth the staircase effect, but implementation can be a rather daunting task. example: <a href="https://pdfs.semanticscholar.org/6f9a/3e71b8eac55500fd1e9535f60c3ad88662cc.pdf" class="inline-onebox" rel="noopener nofollow ugc">[PDF] Staircase-Aware Smoothing of Medical Surface Meshes | Semantic Scholar</a></p>
<p>i see there are posts here (<a href="https://discourse.slicer.org/t/help-with-smoothing-models/597" class="inline-onebox">Help with smoothing models</a>) that state cubic voxels are required to avoid staircase artifacts. does that apply in this case where i am not cropping the volume? are voxels in slicer cubic by default?</p>
<p>i would rather avoid generalized smoothing to preserve the integrity of the model in sections without the stair step effect.</p>

---

## Post #2 by @lassoan (2019-02-06 17:22 UTC)

<p>Slicer has all the tools to deal with this. Do you still have the image where this model is generated from?</p>

---

## Post #3 by @EricWilson (2019-02-06 17:34 UTC)

<p>yes, i have everything needed to generate this model</p>

---

## Post #4 by @lassoan (2019-02-06 18:03 UTC)

<p>OK, if you have the original volume then <a href="https://discourse.slicer.org/t/fetal-lung-volume-calculation/578/5">these instructions</a> should work well.</p>

---
