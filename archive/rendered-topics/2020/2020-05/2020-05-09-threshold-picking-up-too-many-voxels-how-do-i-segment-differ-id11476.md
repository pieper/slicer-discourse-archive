# Threshold picking up too many voxels. How do I segment different areas with same voxels without having to manually paint it? 

**Topic ID**: 11476
**Date**: 2020-05-09
**URL**: https://discourse.slicer.org/t/threshold-picking-up-too-many-voxels-how-do-i-segment-different-areas-with-same-voxels-without-having-to-manually-paint-it/11476

---

## Post #1 by @Demi_Trimino (2020-05-09 07:42 UTC)

<p>Operating system: Mac<br>
Slicer version: 4-11-0<br>
Expected behavior:<br>
Actual behavior:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05bb0674b0e4e2bae4a5068e1c5dbaaf5eeef556.png" data-download-href="/uploads/short-url/OH5oyCIHwKtOJNq1WyEGboXw4m.png?dl=1" title="Screen Shot 2020-05-08 at 11.35.40 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05bb0674b0e4e2bae4a5068e1c5dbaaf5eeef556.png" alt="Screen Shot 2020-05-08 at 11.35.40 AM" data-base62-sha1="OH5oyCIHwKtOJNq1WyEGboXw4m" width="498" height="500" data-dominant-color="474947"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-05-08 at 11.35.40 AM</span><span class="informations">676×678 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to just segment the outline (cuticle) but the inner muscles are too similar in intensity and threshold keeps picking them up. How do I segment this without have to manually paint it on each z stack?</p>

---

## Post #2 by @timeanddoctor (2020-05-10 11:35 UTC)

<p>you can segment with the Islands after threshold.</p>

---
