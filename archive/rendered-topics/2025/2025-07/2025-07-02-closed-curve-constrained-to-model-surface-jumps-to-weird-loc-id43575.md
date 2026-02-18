# Closed curve constrained to model surface jumps to weird locations

**Topic ID**: 43575
**Date**: 2025-07-02
**URL**: https://discourse.slicer.org/t/closed-curve-constrained-to-model-surface-jumps-to-weird-locations/43575

---

## Post #1 by @cliftong (2025-07-02 01:48 UTC)

<p>Mac OSX<br>
Slicer 5.9.0-2025-04-25</p>
<p>I’m hoping to use a closed curve to make a new surface model from an existing model, but the closed curve behaves weirdly when I try to constrain it to the model surface.</p>
<p>Based on previous posts regarding the Dynamic Modeler module (for the eventual curve cut), my model has been decimated (0.5% reduction), the largest component extracted, and surface normals computed.</p>
<p>I then place a closed curve around a complex portion of the model. However, when I select to constrain the curve to the model, the curve jumps to other parts of the model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39b92ab8fd2493de8809e96e6cbe1f3fc2874dff.jpeg" data-download-href="/uploads/short-url/8eDVUri04Rlkf5fYAAf9poXot7F.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39b92ab8fd2493de8809e96e6cbe1f3fc2874dff_2_521x500.jpeg" alt="image" data-base62-sha1="8eDVUri04Rlkf5fYAAf9poXot7F" width="521" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39b92ab8fd2493de8809e96e6cbe1f3fc2874dff_2_521x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39b92ab8fd2493de8809e96e6cbe1f3fc2874dff_2_781x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39b92ab8fd2493de8809e96e6cbe1f3fc2874dff_2_1042x1000.jpeg 2x" data-dominant-color="A8A75D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1100×1054 47.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There are internal structures within the model. I tried making the model hollow using the Dynamic Modeler, but this did not stop the behavior.</p>
<p>Does anyone know why this may be happening? Thanks in advance for any suggestions or guidance!</p>

---

## Post #2 by @pieper (2025-07-02 11:55 UTC)

<p>It might be getting confused by nearby surfaces. Maybe use the modeler to make cropped cutouts of just the local surface of interest.</p>

---

## Post #3 by @cliftong (2025-07-02 16:39 UTC)

<p>Thanks, <a class="mention" href="/u/pieper">@pieper</a>. I was hoping not to do the extra step of cutting the model before placing the closed curves, but you’re right that that is a good workaround!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23dbbd938e57d101fc9af6a35c33fe9a6f984d74.jpeg" data-download-href="/uploads/short-url/57dvd0Xvqq7Y7PC9zWGlbILjokA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23dbbd938e57d101fc9af6a35c33fe9a6f984d74_2_425x375.jpeg" alt="image" data-base62-sha1="57dvd0Xvqq7Y7PC9zWGlbILjokA" width="425" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23dbbd938e57d101fc9af6a35c33fe9a6f984d74_2_425x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23dbbd938e57d101fc9af6a35c33fe9a6f984d74_2_637x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23dbbd938e57d101fc9af6a35c33fe9a6f984d74_2_850x750.jpeg 2x" data-dominant-color="6793B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1040×916 34.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(photo to help anyone doing the same)</p>

---
