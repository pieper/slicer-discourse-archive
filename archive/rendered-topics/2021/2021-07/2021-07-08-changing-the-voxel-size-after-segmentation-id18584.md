---
topic_id: 18584
title: "Changing The Voxel Size After Segmentation"
date: 2021-07-08
url: https://discourse.slicer.org/t/18584
---

# Changing the voxel size after segmentation

**Topic ID**: 18584
**Date**: 2021-07-08
**URL**: https://discourse.slicer.org/t/changing-the-voxel-size-after-segmentation/18584

---

## Post #1 by @Philipp_Maintz (2021-07-08 15:35 UTC)

<p>I have done multiple segmentations. The problem is I now realized that the voxel size is to big. Can I still change them and if so in what module?</p>

---

## Post #2 by @lassoan (2021-07-11 15:32 UTC)

<p>See detailed instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>. Let us know if something is not clear.</p>

---

## Post #3 by @S_Motch_Perrine (2025-06-30 13:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I had a student who performed segmentations on several specimens but didn’t use the correct spacing (should have been 0.005 rather than 1 mm)  - and now I’m getting this error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e73b4c586f531e4345c833a6454a42a5955b5e9b.png" data-download-href="/uploads/short-url/wZzlaR1cqp9PeV5QkW896Bylomf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e73b4c586f531e4345c833a6454a42a5955b5e9b.png" alt="image" data-base62-sha1="wZzlaR1cqp9PeV5QkW896Bylomf" width="539" height="387"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">539×387 34.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>. I don’t think there’s any way I’ve run out of RAM. Suggestions to fix this, please?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b3c592068fbf8ae103cda01d7ac232ac1de3716.png" data-download-href="/uploads/short-url/m9hiNDIpsDTlL6a6H2uyCXcJolE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b3c592068fbf8ae103cda01d7ac232ac1de3716.png" alt="image" data-base62-sha1="m9hiNDIpsDTlL6a6H2uyCXcJolE" width="570" height="150"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">570×150 6.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2025-06-30 16:29 UTC)

<p>If the physical size of the segmentation remains the same but the resolution is increased 1 / 0.005 = 200 times along each axis then the segmentation would become enormous (a 100MB segmentation size would grow to 100MB * 200 * 200 * 200 = 781 GB). Instead, you need to scale down both the physical size and the resolution of the image and the segmentation.</p>
<p>You can scale the segmentation and the corresponding image by creating a scaling transform in Transforms module (write 0.005 into the first 3 elements of the transformation matrix diagonal) and then apply and harden it on the volume and segmentation.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Is there a SlicerMorph tutorial for this?</p>

---

## Post #5 by @muratmaga (2025-06-30 17:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="18584">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Is there a SlicerMorph tutorial for this?</p>
</blockquote>
</aside>
<p>No, but I guess I should do an FAQ for this. To mitigate suggest exporting the segmentation as a labelmap and then entering correct image spacing <strong>both</strong> for source volume and labelmap, and then reimporting the labelmap as a segmentation to continue the work.</p>
<p>It is a bit simpler for people not to mess with transforms.</p>

---

## Post #6 by @S_Motch_Perrine (2025-06-30 19:07 UTC)

<p>Thanks! I will try it!</p>

---

## Post #7 by @S_Motch_Perrine (2025-06-30 19:07 UTC)

<p>Thanks! If you do a FAQ on it, can you please send/tag me in it if you remember? Thank you.</p>

---
