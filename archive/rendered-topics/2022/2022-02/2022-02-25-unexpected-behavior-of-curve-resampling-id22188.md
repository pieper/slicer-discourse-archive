# Unexpected behavior of curve resampling

**Topic ID**: 22188
**Date**: 2022-02-25
**URL**: https://discourse.slicer.org/t/unexpected-behavior-of-curve-resampling/22188

---

## Post #1 by @smrolfe (2022-02-25 23:55 UTC)

<p>I used the “Resample” menu in the Markups module to resample a curve and constrain it to a surface model. Unlike in previous versions, the curve was not constrained to the surface, as seen below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96392baa0b8e32ce79fad64683a95eb5b4d11d02.jpeg" data-download-href="/uploads/short-url/lqW6GTQ1oZDCyMndqbE3tjS0JiO.jpeg?dl=1" title="CaptureRC.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96392baa0b8e32ce79fad64683a95eb5b4d11d02_2_690x449.jpeg" alt="CaptureRC.PNG" data-base62-sha1="lqW6GTQ1oZDCyMndqbE3tjS0JiO" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96392baa0b8e32ce79fad64683a95eb5b4d11d02_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96392baa0b8e32ce79fad64683a95eb5b4d11d02_2_1035x673.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96392baa0b8e32ce79fad64683a95eb5b4d11d02_2_1380x898.jpeg 2x" data-dominant-color="BFC0C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CaptureRC.PNG</span><span class="informations">1920×1252 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If I set “Constrain to model” under the “Curve settings” menu first, then I get the resampled curve snapped to my surface model, shown below. Is this change from previous behavior of curve resampling intended? If so, should resample curves be updated to remove the surface constraint?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2fd0566d4c44cc25b2d1ac18dde4936ac461b59.jpeg" data-download-href="/uploads/short-url/yFzDRUfDNVh1TiS8XDmgky3NQ0x.jpeg?dl=1" title="CaptureRC2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2fd0566d4c44cc25b2d1ac18dde4936ac461b59_2_690x446.jpeg" alt="CaptureRC2.PNG" data-base62-sha1="yFzDRUfDNVh1TiS8XDmgky3NQ0x" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2fd0566d4c44cc25b2d1ac18dde4936ac461b59_2_690x446.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2fd0566d4c44cc25b2d1ac18dde4936ac461b59_2_1035x669.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2fd0566d4c44cc25b2d1ac18dde4936ac461b59_2_1380x892.jpeg 2x" data-dominant-color="C0C0C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CaptureRC2.PNG</span><span class="informations">1920×1242 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @smrolfe (2022-03-01 23:25 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a> could you comment on whether setting the curve type before resampling is intended as part of the addition of the curve settings menu, or is a bug?</p>
<p>I am using the windows rev 30663.</p>

---

## Post #3 by @lassoan (2022-03-01 23:35 UTC)

<p>Since constraining to model is now available in “Curve settings” it is not needed anymore in “Resample curve”, so it should be removed from there. If the projection settings (in “Advanced” section) are all available in “Curve settings” then those too can be removed from “Resample curve” section.</p>

---

## Post #4 by @lassoan (2022-03-08 23:45 UTC)

<p>I’ll remove these redundant settings from the curve resampling section today or tomorrow.</p>

---

## Post #5 by @smrolfe (2022-03-08 23:47 UTC)

<p>I just got back to this and was about to submit a pull request.</p>

---

## Post #6 by @lassoan (2022-03-08 23:48 UTC)

<p>Have you already started working on it?</p>

---

## Post #7 by @smrolfe (2022-03-08 23:51 UTC)

<p>Yes, I just finished testing and was rebasing my branch. But it’s a pretty simple fix if it’s faster for you to submit.</p>

---

## Post #8 by @lassoan (2022-03-08 23:52 UTC)

<p>Please submit it then, I’ll review and consolidate it with my WIP changes.</p>

---
