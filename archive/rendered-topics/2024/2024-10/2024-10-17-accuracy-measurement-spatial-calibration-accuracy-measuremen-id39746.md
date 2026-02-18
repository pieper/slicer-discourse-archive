# ACCURACY MEASUREMENT: Spatial Calibration accuracy measurement

**Topic ID**: 39746
**Date**: 2024-10-17
**URL**: https://discourse.slicer.org/t/accuracy-measurement-spatial-calibration-accuracy-measurement/39746

---

## Post #1 by @jonortegav (2024-10-17 13:38 UTC)

<p>I have done the spatial calibration using a sequence recorded (using PLUS server launcher and 3D slicer sequence module) SlicerIGT Fiducial Registration Wizard module. The thing is that I have noticed that in the tutorial (U31 tutorial - slide 20) is mentioned the next (see figure):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4df80ab4067082bb0d84e5ebb954aef2256fdb8b.png" data-download-href="/uploads/short-url/b7KbVouLdR7097pJt8yZArjcDgv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4df80ab4067082bb0d84e5ebb954aef2256fdb8b_2_690x116.png" alt="image" data-base62-sha1="b7KbVouLdR7097pJt8yZArjcDgv" width="690" height="116" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4df80ab4067082bb0d84e5ebb954aef2256fdb8b_2_690x116.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4df80ab4067082bb0d84e5ebb954aef2256fdb8b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4df80ab4067082bb0d84e5ebb954aef2256fdb8b.png 2x" data-dominant-color="DCDCDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">767×129 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The thing is that I obtained a RMS value of 37.7 but I don’t know how well the calibration has been made (as it says that "RMS increases but accuracy gets better).</p>
<p>I would like to know which is the RMS acceptable value range in order to know if a calibration is acceptable or needs to be done again.</p>
<p>Next image shows the result obtained from the spatial calibration:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0517533c74df41aa0bb3ff2186663c1b0a1bb17a.png" data-download-href="/uploads/short-url/J2moARy0oV4lpOijgeozPIT4cq.png?dl=1" title="spatial calibration accuracy" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0517533c74df41aa0bb3ff2186663c1b0a1bb17a_2_690x401.png" alt="spatial calibration accuracy" data-base62-sha1="J2moARy0oV4lpOijgeozPIT4cq" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0517533c74df41aa0bb3ff2186663c1b0a1bb17a_2_690x401.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0517533c74df41aa0bb3ff2186663c1b0a1bb17a_2_1035x601.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0517533c74df41aa0bb3ff2186663c1b0a1bb17a_2_1380x802.png 2x" data-dominant-color="282526"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">spatial calibration accuracy</span><span class="informations">1636×953 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be appreciated !</p>
<p>Thank you.</p>

---

## Post #2 by @MReza (2024-10-17 16:12 UTC)

<p>Hello,</p>
<p>Based on my experience (always using a linear probe) and what I have observed from other researchers’ work, I would recommend that an error of less than 3 is acceptable.</p>

---

## Post #3 by @jonortegav (2024-10-21 06:08 UTC)

<p>Thank you very much <a class="mention" href="/u/mreza">@MReza</a> !</p>
<p>Can anyone else confirm what <a class="mention" href="/u/mreza">@MReza</a> has said please?</p>

---
