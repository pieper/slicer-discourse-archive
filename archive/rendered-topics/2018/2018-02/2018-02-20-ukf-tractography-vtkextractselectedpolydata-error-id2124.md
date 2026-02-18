# UKF_tractography_vtkExtractSelectedPolyData error

**Topic ID**: 2124
**Date**: 2018-02-20
**URL**: https://discourse.slicer.org/t/ukf-tractography-vtkextractselectedpolydata-error/2124

---

## Post #1 by @ssousa (2018-02-20 13:58 UTC)

<p>When running UKF tractography the following error popup:<br>
ERROR: import port 0 of algorithm vtkExtractSelectedPolyDatalds (0x88e0fa0) has 0 connections but is not optional<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf0bc383a7bc6667b4caeead7049be6f6cdd2698.png" data-download-href="/uploads/short-url/txC2tXNBtBO8iVyboVhZnvweRAs.png?dl=1" title="Descri%C3%A7aoErro" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf0bc383a7bc6667b4caeead7049be6f6cdd2698_2_690x388.png" alt="Descri%C3%A7aoErro" data-base62-sha1="txC2tXNBtBO8iVyboVhZnvweRAs" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf0bc383a7bc6667b4caeead7049be6f6cdd2698_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf0bc383a7bc6667b4caeead7049be6f6cdd2698_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf0bc383a7bc6667b4caeead7049be6f6cdd2698_2_1380x776.png 2x" data-dominant-color="414847"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Descri%C3%A7aoErro</span><span class="informations">1920×1080 342 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Can you help me on this?<br>
Thank you in advance.<br>
Sónia S.</p>

---

## Post #2 by @ihnorton (2018-02-20 21:25 UTC)

<p>Hi Sónia,</p>
<p>Thanks for the report. I’ll check on the <code>vtkExtractSelectedPolyData error</code>. However, the underlying problem is the next one – the error message is “UKF Terminated with an unknown exception”. We’ve seen this happen sometimes with very large output track files. Would you mind to send information about</p>
<ul>
<li>your computer (looks like linux?)</li>
<li>your dataset size</li>
<li>what options you selected for UKFTractography. Please scroll up the Error Log to find the message that looks like the following, and copy it here (or screenshot):</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77b7194ba6990385025c1d300cd3b61b5615709d.png" data-download-href="/uploads/short-url/h536AUmfRHohIPYa556r9TLb2S9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77b7194ba6990385025c1d300cd3b61b5615709d.png" alt="image" data-base62-sha1="h536AUmfRHohIPYa556r9TLb2S9" width="690" height="224" data-dominant-color="D6D8DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">762×248 44.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @ssousa (2018-02-20 22:38 UTC)

<p>Hi Isaiah,</p>
<p>Thanks a lot for your prompt attention to this subject.<br>
Please see below the answers to your queries.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/d/ded36c60b5fe97e71b1c16f5c477d49f34a158c6.png" data-download-href="/uploads/short-url/vNcYc3L6Ys9Qi86Db0lJJUexmjY.png?dl=1" title="ScreenSlicer.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded36c60b5fe97e71b1c16f5c477d49f34a158c6_2_690x388.png" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded36c60b5fe97e71b1c16f5c477d49f34a158c6_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded36c60b5fe97e71b1c16f5c477d49f34a158c6_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded36c60b5fe97e71b1c16f5c477d49f34a158c6_2_1380x776.png 2x" data-dominant-color="C5C5CB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenSlicer.png</span><span class="informations">1920×1080 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @ssousa (2018-02-20 22:40 UTC)

<p>your computer (looks like linux?) YES, THE COMPUTER IS A LINUX<br>
your dataset size - IT WAS JUST A SUBJECT!<br>
what options you selected for UKFTractography. Please scroll up the Error Log to find the message that looks like the following, and copy it here (or screenshot):PLEASE SEE ENCLOSED IMAGE WITH THIS INFORMATION</p>

---

## Post #5 by @ssousa (2018-02-23 15:13 UTC)

<p>Hi Isaiah,</p>
<p>Enclosed please find the shell print screen with the full description of the error. We don’t have more details. Can you help me in solving this?<br>
I thank you in advance for your help!<br>
Best<br>
Sónia<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e4e6d2d84f309d7dc4b6bc756f0bb8f8c20170b.png" data-download-href="/uploads/short-url/6BDZtFHr7OD3DOAG97WREUlnIOD.png?dl=1" title="Descri%C3%A7aoErro2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e4e6d2d84f309d7dc4b6bc756f0bb8f8c20170b_2_690x388.png" alt="Descri%C3%A7aoErro2" data-base62-sha1="6BDZtFHr7OD3DOAG97WREUlnIOD" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e4e6d2d84f309d7dc4b6bc756f0bb8f8c20170b_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e4e6d2d84f309d7dc4b6bc756f0bb8f8c20170b_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e4e6d2d84f309d7dc4b6bc756f0bb8f8c20170b_2_1380x776.png 2x" data-dominant-color="0C0C0C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Descri%C3%A7aoErro2</span><span class="informations">1920×1080 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
