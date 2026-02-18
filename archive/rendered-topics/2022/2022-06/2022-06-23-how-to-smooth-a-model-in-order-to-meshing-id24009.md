# how to smooth a model in order to meshing

**Topic ID**: 24009
**Date**: 2022-06-23
**URL**: https://discourse.slicer.org/t/how-to-smooth-a-model-in-order-to-meshing/24009

---

## Post #1 by @1191620 (2022-06-23 12:55 UTC)

<p>Hello<br>
i have segmented a brain model in to gray matter , white matter and CSF and now I want to export it as a stl file to IA_FEmesh in order to meshing, but my model need to smooth as much as possible. Unfortunately the segment editor does not work properly for me in order to segment my model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8fc73e75703ed591613865ed1fe8d2b5b456e69.jpeg" data-download-href="/uploads/short-url/sG0n2sVSX778uDYLIPcO5cp3PCN.jpeg?dl=1" title="جدید 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8fc73e75703ed591613865ed1fe8d2b5b456e69_2_690x333.jpeg" alt="جدید 1" data-base62-sha1="sG0n2sVSX778uDYLIPcO5cp3PCN" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8fc73e75703ed591613865ed1fe8d2b5b456e69_2_690x333.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8fc73e75703ed591613865ed1fe8d2b5b456e69_2_1035x499.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8fc73e75703ed591613865ed1fe8d2b5b456e69_2_1380x666.jpeg 2x" data-dominant-color="A3A4A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">جدید 1</span><span class="informations">1920×928 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I want to help me if there is a better way in this order.<br>
Thanks</p>

---

## Post #2 by @mau_igna_06 (2022-06-23 17:34 UTC)

<p>Are you allowed to use smoothing algorithms? Slicer smooths the labelmap representation anyway with a taubin filter configured on the segment editor’s button that says “show 3d model” (or something like it).</p>
<p>You may want to change that parameter or try a smoothing segment editor effect to get better results.</p>
<p>It is not totally clear to me what the problem is…</p>
<p>Hope I was helpful</p>

---

## Post #3 by @lassoan (2022-06-24 04:59 UTC)

<p>If you want to build a mesh that is suitable for finite-element modeling then you can try <a href="https://github.com/lassoan/SlicerSegmentMesher#segment-mesher-extension">SegmentMesher extension</a>. If you use Cleaver mesher then it automatically simplifies the mesh.</p>
<p>IA-FEMesh is very old software. Were you able to build it? Does it seem to work well?</p>

---

## Post #4 by @1191620 (2022-07-05 11:35 UTC)

<p>thanks a lot<br>
it works for me properly.</p>

---
