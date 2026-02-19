---
topic_id: 30990
title: "Cmf Extension Surface Registration Fail To Mark Up More Than"
date: 2023-08-05
url: https://discourse.slicer.org/t/30990
---

# CMF Extension, Surface registration fail to mark up more than one reference point or surface

**Topic ID**: 30990
**Date**: 2023-08-05
**URL**: https://discourse.slicer.org/t/cmf-extension-surface-registration-fail-to-mark-up-more-than-one-reference-point-or-surface/30990

---

## Post #1 by @YOU_DDS (2023-08-05 05:16 UTC)

<p>Good afternoon everyone,</p>
<p>I have just worked with 3D slicer, I am trying to superimpose segmented mandible and dental model using CMF reg, Surface registration.</p>
<p>I am not sure it is the right module for this task or not. I am trying to test it. but when I used it, I notice that <strong>I cannot pick reference point or surface more than one.</strong></p>
<p><strong>I wonder whether is there anyone know how to fixed this problem?</strong><br>
The version I am using is Slicer 5.2.2<br>
The below attached photo is the screenshot of the software I am using in surface registration module and the red triangular shape covering the part that showing that the software I am using have no option for more than 1 reference point or surface.</p>
<p>Best Regard<br>
YOU</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4157803092b506a8b65b5626d4044fe10b3e3ad6.jpeg" data-download-href="/uploads/short-url/9k2vjq9Zjc9ticTRU3y5aqIDWjc.jpeg?dl=1" title="스크린샷(100)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4157803092b506a8b65b5626d4044fe10b3e3ad6_2_690x388.jpeg" alt="스크린샷(100)" data-base62-sha1="9k2vjq9Zjc9ticTRU3y5aqIDWjc" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4157803092b506a8b65b5626d4044fe10b3e3ad6_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4157803092b506a8b65b5626d4044fe10b3e3ad6_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4157803092b506a8b65b5626d4044fe10b3e3ad6_2_1380x776.jpeg 2x" data-dominant-color="8A8B8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷(100)</span><span class="informations">1920×1080 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @YOU_DDS (2023-08-22 02:01 UTC)

<p>I have finally found the answer I was looking for.</p>
<p>For those who might have the same problem, you might need to create point list in markup module. Place the point one by one and go back to ROI Registration and set the size of each ROI you want from each point one by one.</p>
<p>This is what I do and it work for me.<br>
Good Luck!!!</p>

---
