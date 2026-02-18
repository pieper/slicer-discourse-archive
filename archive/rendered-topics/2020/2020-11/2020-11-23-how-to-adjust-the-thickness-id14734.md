# How to adjust the thickness

**Topic ID**: 14734
**Date**: 2020-11-23
**URL**: https://discourse.slicer.org/t/how-to-adjust-the-thickness/14734

---

## Post #1 by @slicer365 (2020-11-23 01:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85be39a6a820c1cf0d7291651c7a3d89e1fdab3f.jpeg" data-download-href="/uploads/short-url/j593Fu7pFJc7edFIJqaDgfThTZl.jpeg?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85be39a6a820c1cf0d7291651c7a3d89e1fdab3f_2_690x325.jpeg" alt="01" data-base62-sha1="j593Fu7pFJc7edFIJqaDgfThTZl" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85be39a6a820c1cf0d7291651c7a3d89e1fdab3f_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85be39a6a820c1cf0d7291651c7a3d89e1fdab3f_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85be39a6a820c1cf0d7291651c7a3d89e1fdab3f.jpeg 2x" data-dominant-color="AEB7C3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">1365×643 81.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31d66224776ed12017cb2d51d483784d656a4134.jpeg" data-download-href="/uploads/short-url/76SI2oLhUzDn9cRfyg36OM2imIA.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31d66224776ed12017cb2d51d483784d656a4134_2_690x300.jpeg" alt="2" data-base62-sha1="76SI2oLhUzDn9cRfyg36OM2imIA" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31d66224776ed12017cb2d51d483784d656a4134_2_690x300.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31d66224776ed12017cb2d51d483784d656a4134_2_1035x450.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31d66224776ed12017cb2d51d483784d656a4134.jpeg 2x" data-dominant-color="BABBDA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1365×595 59.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I got a guide plate, this model is very thin, is there a way to adjust its thickness? I plan to make a guide plate for hematoma puncture and add a tube to this model.</p>

---

## Post #2 by @timeanddoctor (2020-11-23 14:12 UTC)

<p>you should get this from the segmenteditor and there are many methods in slicercn forum ,and if you have any question about this puncture surgery you can contact me.</p>

---

## Post #3 by @lassoan (2020-11-28 04:18 UTC)

<p>You can make the skin surface a solid mesh (fill all internal holes) usin Wrap Solidify effect (provided by SurfaceWrapSolidify extension) and then grow a thick outer shell using Hollow effect, and finally trim it to the desired region using Scissors effect. To create the drill guide, you can position a cylinder model and when it is at the right position then import it into the segmentation. Use Logical Operators effect to puncture a hole in the thick shell, then use Hollow effect to convert it to a hollow object. You can then remove the caps using Scissors effect. It may sound that these are lot of steps but they are mostly trivial and can be automated using Python scripting.</p>

---

## Post #4 by @slicer365 (2020-11-28 14:59 UTC)

<p>Thank you very much ,I get success!</p>

---
