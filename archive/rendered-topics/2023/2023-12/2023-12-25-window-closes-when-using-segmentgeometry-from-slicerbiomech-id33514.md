# Window closes when using SegmentGeometry (from SlicerBiomech), some timer after hiting the "apply" button

**Topic ID**: 33514
**Date**: 2023-12-25
**URL**: https://discourse.slicer.org/t/window-closes-when-using-segmentgeometry-from-slicerbiomech-some-timer-after-hiting-the-apply-button/33514

---

## Post #1 by @Henry_Lopes (2023-12-25 08:07 UTC)

<p>The SegmentGeometry module (from the SlicerBiomech extension) doesn’t work, even with sample data. This is what happens:</p>
<ol>
<li>I select the volume and the segment, with simple parameters;</li>
<li>I click the “apply” button;</li>
<li>The window doesn’t respond anymore;</li>
<li>The whole system gets somewhat slow;</li>
<li>Eventually, about 3-5 minutes later, the window closes alone.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bed86c57791af69833e0d9b215e00a5bef563b0.jpeg" data-download-href="/uploads/short-url/foLZdBNz5Lso3j29FCCRNLvasEg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bed86c57791af69833e0d9b215e00a5bef563b0_2_605x500.jpeg" alt="image" data-base62-sha1="foLZdBNz5Lso3j29FCCRNLvasEg" width="605" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bed86c57791af69833e0d9b215e00a5bef563b0_2_605x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bed86c57791af69833e0d9b215e00a5bef563b0_2_907x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bed86c57791af69833e0d9b215e00a5bef563b0.jpeg 2x" data-dominant-color="8C8B8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1202×992 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Versions tested: 5.4.0, 5.6.0, 5.6.1 (the same happen to both them);<br>
OS  used:  Kubuntu 22.04.03 (kernel 5.15.0-91-generic);<br>
Config: AMD A4-7300 APU (3.8ghz max) with Radeon HD Graphics. 16GB ram (2gb shared to video).</p>
<p>This plugin would really help me to conclude some research since it has a really useful feature “align segment with principal axes” (I was using extract center line from vmtk before, without any reason since my segment is almost totally straight).</p>
<p>Thank you very much again!</p>

---

## Post #2 by @Henry_Lopes (2023-12-26 00:36 UTC)

<p>UPDATE: this DOESN’T happen using ubuntu 23.10, so I assume this bug is related to a specific linux version.</p>

---

## Post #3 by @muratmaga (2023-12-27 05:09 UTC)

<p>Is there anything in the Slicer logs in the kubuntu 22.04 that might point out why it is crashing?</p>

---
