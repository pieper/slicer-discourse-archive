# Change tickness in slice intersection 

**Topic ID**: 2421
**Date**: 2018-03-26
**URL**: https://discourse.slicer.org/t/change-tickness-in-slice-intersection/2421

---

## Post #1 by @Sepiho (2018-03-26 13:06 UTC)

<p>Hello,</p>
<p>I have severals tracks in the vtkPolyData format that I load into Slicer 4-7. When switching the “slice intersections visible” option on for one of the model, a line appears. That line is too thin for me (I am preparing figures for a paper). Is it possible to set a thicker line?</p>
<p>Thank you,<br>
Sophie</p>
<p>Operating system: Linux 64<br>
Slicer version: Slicer-4.7.0-2017-08-26-linux-amd64</p>

---

## Post #2 by @cpinter (2018-03-26 13:29 UTC)

<p>There is a thickness option (called Line Width) just below the slice intersection visibility checkbox in Models module Slice Display section.</p>

---

## Post #3 by @Sepiho (2018-03-26 13:52 UTC)

<p>Thank you for yours answer. I tried the Line Width option: I see differences in the 3D view but not in the 2D views (see attached images). Maybe I need to go higher than a line Width of 100 but i can’t. Is there another way to do that?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e9b17833696b08d5013b64c9770a8cc57012104.jpeg" data-download-href="/uploads/short-url/4mKBCLVQGoezBNShkFxIvHrO1iA.jpg?dl=1" title="Screenshot_LineWidth_100" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e9b17833696b08d5013b64c9770a8cc57012104_2_690x432.jpg" alt="Screenshot_LineWidth_100" data-base62-sha1="4mKBCLVQGoezBNShkFxIvHrO1iA" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e9b17833696b08d5013b64c9770a8cc57012104_2_690x432.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e9b17833696b08d5013b64c9770a8cc57012104_2_1035x648.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e9b17833696b08d5013b64c9770a8cc57012104_2_1380x864.jpg 2x" data-dominant-color="878895"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_LineWidth_100</span><span class="informations">1915×1199 503 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>!<br>
<a href="/404" data-orig-href="upload://vgWiStIpPs8KJaGL5oCZMBKUZ7s.jpg">Screenshot_LineWidth_1|690x431</a></p>

---

## Post #4 by @cpinter (2018-03-26 14:05 UTC)

<p>You shouldn’t be seeing any difference in the 3D view when you adjust slice intersection thickness. I think you’re changing the wrong parameter. You use version 4.7 and my instructions are for 4.9. In your version there is a “Slice Intersection Thickness”  control that shows “2 px”. It’s 4 rows above the one you set to 100.</p>

---
