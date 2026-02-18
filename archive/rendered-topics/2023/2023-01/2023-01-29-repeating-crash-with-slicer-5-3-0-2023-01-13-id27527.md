# Repeating crash with slicer 5-3-0 2023 01 13

**Topic ID**: 27527
**Date**: 2023-01-29
**URL**: https://discourse.slicer.org/t/repeating-crash-with-slicer-5-3-0-2023-01-13/27527

---

## Post #1 by @philippepellerin (2023-01-29 10:16 UTC)

<p>Hello, I have a repeating crash which happens during some segmentation work.<br>
Suddenly I can’t zoom or move the display in 3D or in the red screen. I always get the same log error (see the picture)<br>
and have to restart the app.<br>
Is it a bug or something related to my dicom files? Since most of them have been registered with horos and are associated with an h5 file.<br>
I am using Slicer 5-3-0-2023 01 13<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b387f79a7529f68e464c63e5438e7373a4d86824.png" data-download-href="/uploads/short-url/pCcM5nNAqpeRqFimhLKMRGrzyNC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b387f79a7529f68e464c63e5438e7373a4d86824_2_690x59.png" alt="image" data-base62-sha1="pCcM5nNAqpeRqFimhLKMRGrzyNC" width="690" height="59" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b387f79a7529f68e464c63e5438e7373a4d86824_2_690x59.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b387f79a7529f68e464c63e5438e7373a4d86824_2_1035x88.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b387f79a7529f68e464c63e5438e7373a4d86824_2_1380x118.png 2x" data-dominant-color="E3E3E2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1429×124 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-01-29 10:24 UTC)

<p>If you search for IMKClient you can see it is a mac issue with many different packages, nobody seems to know what’s going on from what I saw.  I’ve used Macs for years and have never seen this.  The suggestion is to attach the Activity Monitor and use the spindump tool when the issue occurs.  I’m not sure if the results will help a lot but you can investigate.  If you have the exact steps to replicate others could test, but it may be elusive.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc71c30069e5ff688b2326206b1b22739fdd34cb.png" data-download-href="/uploads/short-url/A1e3sYuToSb0vqVvMfbLZgFDm5B.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc71c30069e5ff688b2326206b1b22739fdd34cb_2_620x499.png" alt="image" data-base62-sha1="A1e3sYuToSb0vqVvMfbLZgFDm5B" width="620" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc71c30069e5ff688b2326206b1b22739fdd34cb_2_620x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc71c30069e5ff688b2326206b1b22739fdd34cb_2_930x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc71c30069e5ff688b2326206b1b22739fdd34cb.png 2x" data-dominant-color="E8EAEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1154×930 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @philippepellerin (2023-01-29 10:41 UTC)

<p>Thanks a lot for your answer. I will try it. I am not handy with those tools, but I will learn, and if I find a way, I will post it.<br>
Again thanks for your time.</p>

---
