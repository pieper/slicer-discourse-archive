# Seed Grow Segmentation tool

**Topic ID**: 25687
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/seed-grow-segmentation-tool/25687

---

## Post #1 by @davidP (2022-10-13 16:39 UTC)

<p>Is it possible to ‘rerun’ the seed grow tool on a segment?  That is to say, I ran a seed grow and got a pretty good 3d image, but some sections did not ‘grow’ as they should.  IF I go back into the editor and add more seeds into these areas (using paint for example) and rerun the seed grow, it does not seem to add any more to the segment based on the new seeds.</p>
<p>ANy thoughts??</p>
<p>thank you</p>

---

## Post #2 by @rbumm (2022-10-14 08:23 UTC)

<p>After Grow From Seeds  “Apply” and having a result that does not satisfy you, you could press “Undo last editing operation”</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64e9099ab635dbd89863394fe4a97382a23b9650.png" alt="image" data-base62-sha1="eoH1Ibb1PDcnfrYUJ8MFKAvyZRC" width="45" height="45"></p>
<p>and “initialize” Grow from seeds again. This would use your previous seeds. Then add some paint strokes where the segmentation needs them.</p>

---

## Post #3 by @rbumm (2022-10-14 08:43 UTC)

<p>The other thing you could do is:</p>
<p>Clear the “outer” bordering segment, which is usually disabled after pressing “Apply” in “Grow from seeds”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/9594bcfb6d5f2030ba4204f63015ea7018fbe156.jpeg" data-download-href="/uploads/short-url/llfOq77QRBCqLoeWarOayMx3Q0e.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/9594bcfb6d5f2030ba4204f63015ea7018fbe156_2_690x487.jpeg" alt="image" data-base62-sha1="llfOq77QRBCqLoeWarOayMx3Q0e" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/9594bcfb6d5f2030ba4204f63015ea7018fbe156_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/9594bcfb6d5f2030ba4204f63015ea7018fbe156_2_1035x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/9594bcfb6d5f2030ba4204f63015ea7018fbe156.jpeg 2x" data-dominant-color="A6A7A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1137×803 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then paint a new outer border segment:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1ad87714024a2c77d56258d1d4869af60465261.jpeg" data-download-href="/uploads/short-url/n4gEJKKDfHznNMjLIC3M25lh66J.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1ad87714024a2c77d56258d1d4869af60465261_2_690x471.jpeg" alt="image" data-base62-sha1="n4gEJKKDfHznNMjLIC3M25lh66J" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1ad87714024a2c77d56258d1d4869af60465261_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1ad87714024a2c77d56258d1d4869af60465261_2_1035x706.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1ad87714024a2c77d56258d1d4869af60465261.jpeg 2x" data-dominant-color="A5A39F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1147×784 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>and press “Initialize” again. Do your modifications by adding additional paint strokes.</p>

---

## Post #4 by @RosieB (2024-04-04 11:17 UTC)

<p>Hello, I have probably quite a basic question about this tool. I have defined two segments with some painted regions, but when I initialize the Grow from seed tool, I get an error message saying<br>
Segmentation operation failed: minimum 2 visible segments is required. But I have added 2 segments"<br>
I will try to add a shot of the error<br>
Grateful for your advice, thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbae346d2aee27ffcf8707ce8297a10afef23c33.png" data-download-href="/uploads/short-url/qMiwb6fyHsTe7XXdfevQk22Xlwn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbae346d2aee27ffcf8707ce8297a10afef23c33_2_380x499.png" alt="image" data-base62-sha1="qMiwb6fyHsTe7XXdfevQk22Xlwn" width="380" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbae346d2aee27ffcf8707ce8297a10afef23c33_2_380x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbae346d2aee27ffcf8707ce8297a10afef23c33_2_570x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbae346d2aee27ffcf8707ce8297a10afef23c33.png 2x" data-dominant-color="EDEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">659×866 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2024-04-06 04:14 UTC)

<p>Please use the latest Slicer Preview Release. The problem is probably already fixed there.</p>

---

## Post #6 by @RosieB (2024-04-08 10:28 UTC)

<p>How embarrassing- thank you very much for your help :)))</p>

---

## Post #7 by @lassoan (2024-04-08 13:33 UTC)

<p>No problem at all. Probably the bug reporting instructions did not emphasize enough that it is worth trying the Slicer Preview Release. I’ve submitted a <a href="https://github.com/Slicer/Slicer/pull/7686">change proposal</a> to add this directly to the documentaiton.</p>

---
