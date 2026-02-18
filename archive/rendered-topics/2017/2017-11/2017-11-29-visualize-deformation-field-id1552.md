# Visualize Deformation field

**Topic ID**: 1552
**Date**: 2017-11-29
**URL**: https://discourse.slicer.org/t/visualize-deformation-field/1552

---

## Post #1 by @eladam (2017-11-29 04:18 UTC)

<p>Hello,<br>
I have been trying to visualize a deformation field in Slicer (it’s a vector image), but I am having some issues. I would like it to be shown with arrows on the respective points.</p>
<p>I am trying to display the Glyph, which is located in Transforms. But it also requires a Transform but I don’t want to convert something, I just want to visualize the deformation field which I have in a different way (with arrows). Is there a way to do that, other than the Transforms module and if not, how can I do that with that module?</p>
<p>Thank you very much,<br>
Eleni</p>

---

## Post #2 by @lassoan (2017-11-29 17:10 UTC)

<p>Display feature of Transforms module is developed specifically for displacement field visualization. The easiest is to load your displacement field as a displacement field transform by selecting <code>Transform</code> in <code>Add data...</code> dialog’s <code>Description</code> column:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4171e6f5a159ff9dc669819d0b551d465cff4f31.png" data-download-href="/uploads/short-url/9kX4kDPRcoGnJnN0TZFgHJ6ybzr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4171e6f5a159ff9dc669819d0b551d465cff4f31_2_690x496.png" alt="image" data-base62-sha1="9kX4kDPRcoGnJnN0TZFgHJ6ybzr" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4171e6f5a159ff9dc669819d0b551d465cff4f31_2_690x496.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4171e6f5a159ff9dc669819d0b551d465cff4f31.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4171e6f5a159ff9dc669819d0b551d465cff4f31.png 2x" data-dominant-color="E5E5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">837×602 35.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @eladam (2017-12-02 06:54 UTC)

<p>Thank you very much!!</p>

---
