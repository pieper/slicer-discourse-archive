# Subtraction of intersect area

**Topic ID**: 37923
**Date**: 2024-08-17
**URL**: https://discourse.slicer.org/t/subtraction-of-intersect-area/37923

---

## Post #1 by @khajta (2024-08-17 05:01 UTC)

<p>Dear Experts,</p>
<p>I have 2 segment dataset, organ and lesion. Some of these lesions are overlap or in the organ, such as liver. How can I erase organ area which overlap with tumor area (other than manual editing)?</p>
<p>Sincerely,<br>
Khajonsak</p>

---

## Post #2 by @philippepellerin (2024-08-18 08:29 UTC)

<p>It is easily done using the logical operator tool in the segment editor module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/795fd2b5892f10925a371163e10bce30963a664b.png" data-download-href="/uploads/short-url/hjJ4Ac13yYAZ8S9NC06zFitBvzJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/795fd2b5892f10925a371163e10bce30963a664b_2_343x500.png" alt="image" data-base62-sha1="hjJ4Ac13yYAZ8S9NC06zFitBvzJ" width="343" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/795fd2b5892f10925a371163e10bce30963a664b_2_343x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/795fd2b5892f10925a371163e10bce30963a664b_2_514x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/795fd2b5892f10925a371163e10bce30963a664b_2_686x1000.png 2x" data-dominant-color="E8E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1136×1652 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @khajta (2024-08-19 03:18 UTC)

<p>Thank you very much.</p>

---
