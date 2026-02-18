# Why can I only lable the center part of the images?

**Topic ID**: 40599
**Date**: 2024-12-09
**URL**: https://discourse.slicer.org/t/why-can-i-only-lable-the-center-part-of-the-images/40599

---

## Post #1 by @Dan_Cheng (2024-12-09 23:07 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2c7cec410e49512093eb4cab10caaf1f7162d2c.jpeg" data-download-href="/uploads/short-url/ne1r2Izvb7RRR7zTkeHTor01KTa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2c7cec410e49512093eb4cab10caaf1f7162d2c_2_522x500.jpeg" alt="image" data-base62-sha1="ne1r2Izvb7RRR7zTkeHTor01KTa" width="522" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2c7cec410e49512093eb4cab10caaf1f7162d2c_2_522x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2c7cec410e49512093eb4cab10caaf1f7162d2c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2c7cec410e49512093eb4cab10caaf1f7162d2c.jpeg 2x" data-dominant-color="3F403F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">657×629 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
this is the geometry of images<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05876f56a2db66349c000d172febdcaf52530893.png" data-download-href="/uploads/short-url/MUyqEwuX8WHimLXCndoEeezYvp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05876f56a2db66349c000d172febdcaf52530893.png" alt="image" data-base62-sha1="MUyqEwuX8WHimLXCndoEeezYvp" width="475" height="355"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">475×355 42.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>this is the geometry of segementation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaf7d40ea5143535b8007908a0a94ffe3aba18a0.png" data-download-href="/uploads/short-url/xwCHgCDL8iyUA2yRRxPGE6aXDoI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaf7d40ea5143535b8007908a0a94ffe3aba18a0.png" alt="image" data-base62-sha1="xwCHgCDL8iyUA2yRRxPGE6aXDoI" width="475" height="299"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">475×299 33.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I donot manually change anything<br>
just wondering if this is the problem? if it is, how to solve this? many thx!</p>

---

## Post #2 by @cpinter (2024-12-10 10:05 UTC)

<p>You need to make sure the source volume is the one you actually segment. Try this:</p>
<ul>
<li>Make sure you use the latest Slicer</li>
<li>Load your volume</li>
<li>Go to Segment Editor</li>
<li>Make sure “Source volume” is the one you want to segment <strong>before</strong> you create a new segment</li>
<li>Start segmenting</li>
</ul>
<p>If this does not work we need to know what you do exactly, preferibly with a video from the beginning.</p>

---

## Post #3 by @Dan_Cheng (2024-12-10 22:27 UTC)

<p>Hello Csaba,</p>
<p>Thank you very much for your reply. The problem was solved by using the latest version.<br>
Thanks again.</p>

---
