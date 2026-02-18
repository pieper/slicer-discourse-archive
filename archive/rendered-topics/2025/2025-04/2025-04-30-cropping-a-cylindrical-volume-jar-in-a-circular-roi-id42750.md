# Cropping a Cylindrical Volume (Jar) in a Circular ROI

**Topic ID**: 42750
**Date**: 2025-04-30
**URL**: https://discourse.slicer.org/t/cropping-a-cylindrical-volume-jar-in-a-circular-roi/42750

---

## Post #1 by @sieunmiin96 (2025-04-30 19:24 UTC)

<p>Hi,</p>
<p>I’m working with MR images of Fricke gel jars and trying to isolate each jar for analysis. I’m currently using the Crop Volume module in 3D Slicer, but it only lets me define a rectangular ROI. Since the jars are cylindrical, I’d like to crop each one using a circular (or cylindrical) ROI instead, to more accurately capture the region of interest and minimize background noise.</p>
<p>Is there a way to crop a volume in a circular shape, or apply a cylindrical mask for this purpose? I’ve attached a screenshot showing what I’m currently working with.</p>
<p>Thanks in advance for any suggestions!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36ffcd15281161666e4986f6f02b0c3acbb9ce20.png" data-download-href="/uploads/short-url/7QxPKKqjXRnATSRDkoAI62WOkHm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36ffcd15281161666e4986f6f02b0c3acbb9ce20_2_690x387.png" alt="image" data-base62-sha1="7QxPKKqjXRnATSRDkoAI62WOkHm" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36ffcd15281161666e4986f6f02b0c3acbb9ce20_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36ffcd15281161666e4986f6f02b0c3acbb9ce20_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36ffcd15281161666e4986f6f02b0c3acbb9ce20_2_1380x774.png 2x" data-dominant-color="A6A4A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1436×807 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mau_igna_06 (2025-04-30 19:34 UTC)

<p>You can mask-out everything outside a cylinder with the following steps:</p>
<ol>
<li>Install extension “Extra segment editor effects” using the Extensions Manager</li>
<li>Create a segmentation node for your volume in the Segment Editor module</li>
<li>Create a new segment</li>
<li>Use the “Draw tube” effect, and create a point at the top and another one at the bottom of the cylinder visible on your CT. Adjust the radius to cover the cylinder. Click apply.</li>
<li>Use “Mask volume” effect. Select “Fill outside”. Set fill value as “-1024”. Click apply</li>
<li>Check out that you should have a newer CT volume that only contains your cylinder</li>
</ol>

---

## Post #3 by @Antmaker (2026-02-04 23:48 UTC)

<p>Thanks, this is just what I needed.</p>
<p>For posterity, the “Mask Volume” effect is part of the default effect set starting with v.4.13 (src: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects?tab=readme-ov-file#mask-volume" rel="noopener nofollow ugc">SlicerSegmentEditorExtraEffects README</a>).</p>

---

## Post #4 by @cpinter (2026-02-05 09:22 UTC)

<p>Note that to do the above workflow you still need the extra effects extension, because the Draw tube effect is there.</p>

---
