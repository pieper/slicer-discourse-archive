# Error with calculation image difference using ROI

**Topic ID**: 15315
**Date**: 2021-01-02
**URL**: https://discourse.slicer.org/t/error-with-calculation-image-difference-using-roi/15315

---

## Post #1 by @marianaslicer (2021-01-02 11:46 UTC)

<p>Slicer version: 4.13.0 and Slicer 4.11.20200930</p>
<p>Hello everyone,</p>
<p>I want to calculate the image difference between the fixed and warped image, after registration, using a specified ROI. I manually created the ROI, but after assign it the role as ROI in Registration Quality Assurance module, there was a shift and the result of the image difference was wrong.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2bff5a6c23eacf39e905d96fdefed4b913bf98f.jpeg" data-download-href="/uploads/short-url/rMPTQwGdQ8il8nn18MMWBUPfvcP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2bff5a6c23eacf39e905d96fdefed4b913bf98f_2_517x323.jpeg" alt="image" data-base62-sha1="rMPTQwGdQ8il8nn18MMWBUPfvcP" width="517" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2bff5a6c23eacf39e905d96fdefed4b913bf98f_2_517x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2bff5a6c23eacf39e905d96fdefed4b913bf98f_2_775x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2bff5a6c23eacf39e905d96fdefed4b913bf98f.jpeg 2x" data-dominant-color="4A4A5C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">972×608 93.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The error occurred in both 3D Slicer versions.</p>
<p>If anyone could help me. I would really appreciate it.</p>

---

## Post #2 by @lassoan (2021-01-02 15:53 UTC)

<p>You may need to harden the transform on the warped image.</p>

---

## Post #3 by @marianaslicer (2021-01-02 16:42 UTC)

<p>Thank Andras for your response.</p>
<p>Usually is not necessary to harden the transform on the warped image since the warped image is already the result of the transformation. Nonetheless, I tried to do it and nothing changed.<br>
I also tried to convert the transformation into a vector volume node and then assign it the role as forward vector field. But I’m getting the same error even with a different ROI.</p>
<p>If I don’t use any ROI, the module calculates the difference between the two images correctly. Maybe the difference between the two images can not be calculated with ROI? or is it a bug?</p>
<p>Thanks,<br>
Mariana</p>

---

## Post #4 by @lassoan (2021-01-03 19:32 UTC)

<p>It seems that maintainer of this extension does not read the Slicer forum, so I would recommend to file an error report in the extension’s repository. If you don’t get any answer within 2 weeks then let us know.</p>

---
