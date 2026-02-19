---
topic_id: 13113
title: "I Cant Achieve Five Lobe Segmentation With Interactive Lobe"
date: 2020-08-20
url: https://discourse.slicer.org/t/13113
---

# I can't achieve five lobe segmentation with interactive lobe segmentation in CIP, can someone help me?

**Topic ID**: 13113
**Date**: 2020-08-20
**URL**: https://discourse.slicer.org/t/i-cant-achieve-five-lobe-segmentation-with-interactive-lobe-segmentation-in-cip-can-someone-help-me/13113

---

## Post #1 by @ava_yektaeian (2020-08-20 12:58 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a01f0ffff95c6981ed3ffbe1c47f8b4e2d49bb46.png" data-download-href="/uploads/short-url/mQuWFQxPCFQyokMJETYPmDpKDqu.png?dl=1" title="xdd" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a01f0ffff95c6981ed3ffbe1c47f8b4e2d49bb46_2_690x375.png" alt="xdd" data-base62-sha1="mQuWFQxPCFQyokMJETYPmDpKDqu" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a01f0ffff95c6981ed3ffbe1c47f8b4e2d49bb46_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a01f0ffff95c6981ed3ffbe1c47f8b4e2d49bb46_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a01f0ffff95c6981ed3ffbe1c47f8b4e2d49bb46.png 2x" data-dominant-color="C5C7CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">xdd</span><span class="informations">1225×667 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I completely follow the the interactive lobe segmentation in slicer but most of the time I can’t achieve the lobe segmentation</p>
<p>can some one give tips?</p>

---

## Post #2 by @anirb14 (2020-09-28 16:10 UTC)

<p>Did you find any solution??? Facing the same problem</p>

---

## Post #3 by @Saffana (2020-10-06 12:03 UTC)

<p>Same issue I find in most scans can you help please</p>

---

## Post #4 by @Richard1 (2022-04-09 22:17 UTC)

<p>Is there a way to circumvent this issue? This only happens in some CT acquired images.</p>

---

## Post #5 by @rbumm (2022-04-10 13:22 UTC)

<p>Try loading the Slicer CTChest demo dataset from “Sample Data”.<br>
Place many fiducials (&gt; 15 each)  on each of the fissures using the sagittal slice view. Use different levels right to left. Press “Apply”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/590c62b9f20c3bb4af49772fc0aafde0132f841a.jpeg" data-download-href="/uploads/short-url/cHL1VaIbIYIh86FlUb10KQ9tk4G.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/590c62b9f20c3bb4af49772fc0aafde0132f841a_2_690x294.jpeg" alt="image" data-base62-sha1="cHL1VaIbIYIh86FlUb10KQ9tk4G" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/590c62b9f20c3bb4af49772fc0aafde0132f841a_2_690x294.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/590c62b9f20c3bb4af49772fc0aafde0132f841a_2_1035x441.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/590c62b9f20c3bb4af49772fc0aafde0132f841a_2_1380x588.jpeg 2x" data-dominant-color="9B9CA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×820 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The output of the procedure is a labelmap, that - before it can be editited in the “Segment Editor” - must be transformed into a segmentation by hand (go “Data” module, right click the labelmap, “Convert to segmentation”.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/aff77a70e6edd1965f87ca92b3685ce74e5246fa.png" alt="image" data-base62-sha1="p6FMbcVljHo3dLlN9Movn2TjGHg" width="462" height="375"></p>
<p>Please note, that the interactive lobe segmentation (as several other modules in CIP) has been implemented in Slicer for years without active maintenance by its developers.</p>
<aside class="quote no-group" data-username="Richard1" data-post="4" data-topic="13113">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/50afbb/48.png" class="avatar"> Richard1:</div>
<blockquote>
<p>only happens in some</p>
</blockquote>
</aside>
<p>Please give more details.<br>
In some it works, in others, it doesn’t?<br>
Which Slicer version are you using?</p>

---

## Post #6 by @Richard1 (2022-04-10 15:43 UTC)

<p>I am using Slicer 4.11.2021.</p>
<p>A few of the CTs are not segmenting into the proper lobes despite having multiple fiducial markers. Could it be a CT acquisition issue or a setting in 3D slicer?</p>

---

## Post #7 by @Richard1 (2022-04-10 15:58 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79c88d2c63da16e8a37043e372ab065426e5f44e.png" alt="image" data-base62-sha1="hnls725H9D3RsvYoS4OvqLITnnU" width="436" height="366"></p>
<p>I put &gt;20 points but still identifies the lungs as one whole lobe.</p>

---

## Post #8 by @rbumm (2022-04-10 17:06 UTC)

<aside class="quote no-group" data-username="Richard1" data-post="6" data-topic="13113">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/50afbb/48.png" class="avatar"> Richard1:</div>
<blockquote>
<p>A few of the CTs are not segmenting into the proper lobes</p>
</blockquote>
</aside>
<p>Could well be an acquisition error - maybe you want to check the “Volumes” module and compare the Volume Information with the ones in which the segmentation is working?</p>
<p>For the CTChest dataset I get:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf5a66b4c42a5c2ba88e83de3fe0ef12c048d61.png" data-download-href="/uploads/short-url/sXsKCg5OtjD2yqJRvNICmPLfaDL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf5a66b4c42a5c2ba88e83de3fe0ef12c048d61.png" alt="image" data-base62-sha1="sXsKCg5OtjD2yqJRvNICmPLfaDL" width="535" height="500" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">673×628 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Richard1 (2022-04-10 18:10 UTC)

<p>I looked over the volumes and they have similar dimensions. Not quite sure what else could be messing up the lobular segmentation.</p>

---

## Post #10 by @rbumm (2022-04-10 18:19 UTC)

<p>If there is one of those you could share for a test let me know.</p>

---
