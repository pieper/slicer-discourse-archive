---
topic_id: 34673
title: "Spharm Pdm Error Not Enough Points Cannot Solve Spharm Coeff"
date: 2024-03-03
url: https://discourse.slicer.org/t/34673
---

# SPHARM-PDM error: "Not enough points; cannot solve SPHARM coefficients."

**Topic ID**: 34673
**Date**: 2024-03-03
**URL**: https://discourse.slicer.org/t/spharm-pdm-error-not-enough-points-cannot-solve-spharm-coefficients/34673

---

## Post #1 by @etour (2024-03-03 04:27 UTC)

<p>Hi everyone!</p>
<p>I’ve just attempted to process 8 .nrrd files using the SPHARM ‘Shape Analysis Module’. 7 of these files have worked as expected, and I get all the right outputs at the end. However, I’m having issues with 1 of the files.</p>
<p>For this 1 problem file, the process failed at the ParatoSPHARMMesh step, with the error “Description: Not enough points; cannot solve SPHARM coefficients.”, however, I think the problem goes all the way back to SegPostProcess step. When I compare the _pp.nrrd file generated for the failed case with those generated for the 7 successful cases, it basically only contains the header and no other information (see image below). The other files for the successful cases seem to be fully formed, and contain a lot more information in the body. I’m assuming this is why other problems are then happening down the line for this particular case. Can you please suggest why this may be happening? I can’t see any real difference between all the .nrrd files I’m using as my original inputs, so unsure what’s causing the problem. Please let me know if further information is required.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a490242c220919d4d8e6d1da972e2710ad3fbacd.png" data-download-href="/uploads/short-url/ntN7Q7fDKW4hM0Cubmbo4FVqQqh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a490242c220919d4d8e6d1da972e2710ad3fbacd.png" alt="image" data-base62-sha1="ntN7Q7fDKW4hM0Cubmbo4FVqQqh" width="690" height="209" data-dominant-color="F8F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1252×380 10 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best,</p>
<p>Emily</p>

---

## Post #2 by @bpaniagua (2024-03-04 13:01 UTC)

<p>Hi Emily,</p>
<p>What is the error output of SegPostProcess for that case?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/987ea021edebc14c45b80ab7b502d6c2465264df.png" alt="Screenshot 2024-03-04 at 8.01.07 AM" data-base62-sha1="lL1RU5dM6WFaOUlJFnozuUe4qQv" width="464" height="104"></p>
<p>B.</p>

---
