# Data Load Failed

**Topic ID**: 46144
**Date**: 2026-02-13
**URL**: https://discourse.slicer.org/t/data-load-failed/46144

---

## Post #1 by @Daniel_C (2026-02-13 03:41 UTC)

<p>Hi there,</p>
<p>I encountered an error while trying to open a set of CT TIFF images. The error message only shows “load failed.” Is there any way to resolve this issue?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d653894d47ff2da5f0e4321fd00eb7310b7076e6.png" data-download-href="/uploads/short-url/uA19zHCnFq877n7armq4cqRKoJ0.png?dl=1" title="屏幕截图 2026-02-13 113552" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d653894d47ff2da5f0e4321fd00eb7310b7076e6_2_690x410.png" alt="屏幕截图 2026-02-13 113552" data-base62-sha1="uA19zHCnFq877n7armq4cqRKoJ0" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d653894d47ff2da5f0e4321fd00eb7310b7076e6_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d653894d47ff2da5f0e4321fd00eb7310b7076e6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d653894d47ff2da5f0e4321fd00eb7310b7076e6.png 2x" data-dominant-color="B7B8BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2026-02-13 113552</span><span class="informations">998×594 73.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ebrahim (2026-02-13 14:02 UTC)

<p>You can also try the ImageStacks module from the SlicerMorph extension</p>
<p>Is it a stack of tiffs or just the single file? Did you check “single file”?</p>

---

## Post #3 by @Daniel_C (2026-02-13 14:31 UTC)

<p>It is a stack of TIFF files (about 3,000 slices), not a single file.</p>
<p>If I load each TIFF file individually, they can be added successfully. However, when I try to load the whole stack using “Choose Directory to Add”, it shows “Load Failed” and does not provide any error message.</p>
<p>I did not check the “single file” option. If I do check “single file”, it does not report an error, but it only loads a single image instead of the full stack.</p>
<p>My computer has 128 GB of RAM, so it is unlikely to be a memory issue.</p>

---

## Post #4 by @pieper (2026-02-13 19:04 UTC)

<p>If they are named in a way ITK can guess, then just selecting the first and unchecking the “Single File” option may load them as a volume, but definitely ImageStacks is the tool that is designed to support this task.</p>

---
