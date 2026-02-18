# Convert .stl file into .bmp image set

**Topic ID**: 11149
**Date**: 2020-04-16
**URL**: https://discourse.slicer.org/t/convert-stl-file-into-bmp-image-set/11149

---

## Post #1 by @Mathias (2020-04-16 13:46 UTC)

<p>Hello,<br>
as you see in the title, I need to convert my .stl file into .bmp (bitmap) image set.<br>
I searched on internet but I didn’t find any tutorials about it.<br>
I need my image set for a 3D printing project, each image need to be space of “x” mm.</p>
<p>It would be very significant if someone could help me.</p>
<p>Thank you,</p>
<p>Mathias.</p>

---

## Post #2 by @pieper (2020-04-17 17:37 UTC)

<p>You can use the segment editor for this.  Just load the STL as a segmentation, convert to labelmap and save as a bitmap (bmp is not a good format of course, but sometimes that’s what’s needed for legacy equipment I suppose).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9e2d4b367640f84c1b090dea580ba778a0d6bdc.png" alt="image" data-base62-sha1="qwqjwwYgaq6Vwxe7MAsA4rW4PJa" width="211" height="51"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c472ca66c6eb7f41b9a70fc11a9d2381154cf4f6.png" data-download-href="/uploads/short-url/s1RwmzfByh4bjvLI9fAN9dCUgoC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c472ca66c6eb7f41b9a70fc11a9d2381154cf4f6_2_344x108.png" alt="image" data-base62-sha1="s1RwmzfByh4bjvLI9fAN9dCUgoC" width="344" height="108" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c472ca66c6eb7f41b9a70fc11a9d2381154cf4f6_2_344x108.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c472ca66c6eb7f41b9a70fc11a9d2381154cf4f6_2_516x162.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c472ca66c6eb7f41b9a70fc11a9d2381154cf4f6_2_688x216.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1148×360 32.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b51057f035fb8058e0a6c0fc34d2af30bc29eb5.png" data-download-href="/uploads/short-url/aKhoFQ2Ex4ygP4T0gkbYvPDOngV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b51057f035fb8058e0a6c0fc34d2af30bc29eb5_2_345x97.png" alt="image" data-base62-sha1="aKhoFQ2Ex4ygP4T0gkbYvPDOngV" width="345" height="97" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b51057f035fb8058e0a6c0fc34d2af30bc29eb5_2_345x97.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b51057f035fb8058e0a6c0fc34d2af30bc29eb5_2_517x145.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b51057f035fb8058e0a6c0fc34d2af30bc29eb5_2_690x194.png 2x" data-dominant-color="DAE0E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">946×266 43.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></p>

---
