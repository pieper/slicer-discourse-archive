# HD-BET doesn't work for me

**Topic ID**: 31791
**Date**: 2023-09-19
**URL**: https://discourse.slicer.org/t/hd-bet-doesnt-work-for-me/31791

---

## Post #1 by @MZA (2023-09-19 15:37 UTC)

<p>Hi 3D Slicer team,</p>
<p>I’m having a problem with using HD-BET to extract the brain from a T1WI with contrast .nrrd file. When I select the input and output files, and click ‘Apply (Image 1),’ it seems like it’s working in the background with a rotating cursor, but after 3-4 minutes, the layout on the right only shows a single frame (Yellow arrows in Image 2). Also, when I try to save the stripped file in either .nrrd or .nii format (Image 3), nothing gets saved.</p>
<p>Do you have any suggestions for what I can do to fix this issue?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a2ea2d4223ecb47fcd42bd115b9027664058c36.jpeg" data-download-href="/uploads/short-url/619YcEz6SvOGdQgXzvZZjFUNJL8.jpeg?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a2ea2d4223ecb47fcd42bd115b9027664058c36_2_690x366.jpeg" alt="01" data-base62-sha1="619YcEz6SvOGdQgXzvZZjFUNJL8" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a2ea2d4223ecb47fcd42bd115b9027664058c36_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a2ea2d4223ecb47fcd42bd115b9027664058c36_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a2ea2d4223ecb47fcd42bd115b9027664058c36_2_1380x732.jpeg 2x" data-dominant-color="8B8B91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">1920×1020 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9847f93661361514198187c0f954653aa377968.jpeg" data-download-href="/uploads/short-url/xjN7ScQOvMGXUg00SzCFEAPrSGc.jpeg?dl=1" title="02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9847f93661361514198187c0f954653aa377968_2_690x366.jpeg" alt="02" data-base62-sha1="xjN7ScQOvMGXUg00SzCFEAPrSGc" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9847f93661361514198187c0f954653aa377968_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9847f93661361514198187c0f954653aa377968_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9847f93661361514198187c0f954653aa377968_2_1380x732.jpeg 2x" data-dominant-color="8C8C91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02</span><span class="informations">1920×1020 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8adc1d62dadbba3e444717601cf5b91b1094991.jpeg" alt="03" data-base62-sha1="sDhLyNVtELuNpVR5IdKewjfrsml" width="632" height="337"></p>

---

## Post #2 by @pieper (2023-09-19 19:52 UTC)

<p>Check to see if there were messages in the log window.  Also try with the sample data to see if you can replicate the issue.</p>

---

## Post #3 by @lassoan (2023-09-19 20:02 UTC)

<p>HD-BET <a href="https://github.com/MIC-DKFZ/HD-BET/commit/bfc50c1f978c3f9e63674323f4f17294b57c2321">API has changed</a>, now saving of masked input file must be requested explicitly. I’ve updated the extension accordingly. You can update the extension in the Extensions Manager tomorrow or later to get the fix.</p>

---

## Post #4 by @MZA (2023-09-20 18:58 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you! It works fine now after the update.</p>

---
