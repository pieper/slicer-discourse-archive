# Question about DRR

**Topic ID**: 31286
**Date**: 2023-08-22
**URL**: https://discourse.slicer.org/t/question-about-drr/31286

---

## Post #1 by @MYasinMohammadi (2023-08-22 14:25 UTC)

<p>I have prepared a DRR image using Plastimatch<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/555541e940b0aaec512cda224efd419316579c1a.png" data-download-href="/uploads/short-url/caTfokApZs9vv8bWvKp9ZPVm8UG.png?dl=1" title="DRR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/555541e940b0aaec512cda224efd419316579c1a_2_483x500.png" alt="DRR" data-base62-sha1="caTfokApZs9vv8bWvKp9ZPVm8UG" width="483" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/555541e940b0aaec512cda224efd419316579c1a_2_483x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/555541e940b0aaec512cda224efd419316579c1a_2_724x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/555541e940b0aaec512cda224efd419316579c1a.png 2x" data-dominant-color="747474"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DRR</span><span class="informations">836×864 32.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Gray rings can be seen in the display of this image. What is the cause of this phenomenon?</p>

---

## Post #2 by @cpinter (2023-08-24 11:04 UTC)

<p>Images in the 2D views are interpolated by default. You can turn off interpolation in the view controller widget, accessed in the top left corner of the view, in the header.</p>

---
