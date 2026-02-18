# Blank spaces after segmentation

**Topic ID**: 13201
**Date**: 2020-08-27
**URL**: https://discourse.slicer.org/t/blank-spaces-after-segmentation/13201

---

## Post #1 by @arifeuzundurukan (2020-08-27 18:38 UTC)

<p>Hello everyone,<br>
I was trying to make segmentation of lungs and human soft tissue but after the segmentation I faced some blank spaces between the the lungs and human soft tissue.<br>
I would like to make a FEM analysis by using this CT created image and because of the this blank spaces between the organs there are missing connection between the organs, cannot touch each other.<br>
Could you please help me? How can I fill the blank spaces between the segmented organs?</p>

---

## Post #2 by @lassoan (2020-08-27 20:34 UTC)

<p>Could you post a screenshot to make it clear what blank spaces you are referring to? Thank you.</p>

---

## Post #3 by @arifeuzundurukan (2020-08-27 21:35 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d013a0f5fe263de638c15f7c2aa5a7558179a7b.jpeg" data-download-href="/uploads/short-url/1R2PNIYtB7HqPOdG2hIRY8FS2NR.jpeg?dl=1" title="BlankSpaces" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d013a0f5fe263de638c15f7c2aa5a7558179a7b_2_690x388.jpeg" alt="BlankSpaces" data-base62-sha1="1R2PNIYtB7HqPOdG2hIRY8FS2NR" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d013a0f5fe263de638c15f7c2aa5a7558179a7b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d013a0f5fe263de638c15f7c2aa5a7558179a7b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d013a0f5fe263de638c15f7c2aa5a7558179a7b_2_1380x776.jpeg 2x" data-dominant-color="929694"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BlankSpaces</span><span class="informations">1920×1080 338 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thank you for your interest. You can reach the image of the segmentation, in the attachment.</p>

---

## Post #4 by @muratmaga (2020-08-27 21:43 UTC)

<p>I suspect you are tracing two segments manually and separately, causing a misalignment in the border and leaving gaps. If you do the full chest first segment, then do the lungs, and then subtract, you shouldn’t have these double borders.</p>

---

## Post #5 by @arifeuzundurukan (2020-08-28 20:22 UTC)

<p>Yes, you are absolutely right. Thank you for your valuable suggestion!!<br>
Now, I have solved the connection  problem; however, I have recognized that if I try to simplify the geometry the connection is detorieted.<br>
I have to simplify the geometry at least I have to remove the spike geometries by preserving the connections. Do you have anyrecommended tool or way to do it ?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfbcf4ff5db5b2f3e85756e79542de32496925b2.jpeg" data-download-href="/uploads/short-url/rmc2c6zFofe7jbWhLUQrBZHINz4.jpeg?dl=1" title="InkedCapture d&amp;#39;écran 2020-08-28 16.04.57_LI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfbcf4ff5db5b2f3e85756e79542de32496925b2_2_690x360.jpeg" alt="InkedCapture d'écran 2020-08-28 16.04.57_LI" data-base62-sha1="rmc2c6zFofe7jbWhLUQrBZHINz4" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfbcf4ff5db5b2f3e85756e79542de32496925b2_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfbcf4ff5db5b2f3e85756e79542de32496925b2_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfbcf4ff5db5b2f3e85756e79542de32496925b2_2_1380x720.jpeg 2x" data-dominant-color="A0A7A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">InkedCapture d&amp;#39;écran 2020-08-28 16.04.57_LI</span><span class="informations">1911×998 337 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2020-08-29 02:39 UTC)

<p>You can use Smoothing effect for this. Joint smoothing method is applies to all segments at once and preserves a watertight segmentation.</p>

---
