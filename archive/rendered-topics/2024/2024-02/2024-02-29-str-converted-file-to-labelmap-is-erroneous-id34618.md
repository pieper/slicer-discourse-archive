# str-converted file to labelmap is erroneous

**Topic ID**: 34618
**Date**: 2024-02-29
**URL**: https://discourse.slicer.org/t/str-converted-file-to-labelmap-is-erroneous/34618

---

## Post #1 by @richyrich (2024-02-29 17:55 UTC)

<p>Hi,<br>
I have a geometry created by a CFD-solver (StarCCM+).<br>
I exported the surface geometry as an .stl file, and then converted it to labelmap (as recommended in the forums).<br>
I am getting this weird segmentation below that does not allow me to proceed.<br>
Note that my ultimate aim is to identify the centerline.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bce661c19bf71c25c12301e3d6075925cb0e2f92.png" data-download-href="/uploads/short-url/qX5m1MUV3V3Sdysx39lbSmYq0GS.png?dl=1" title="Screenshot 2024-02-29 at 13.49.12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bce661c19bf71c25c12301e3d6075925cb0e2f92_2_583x500.png" alt="Screenshot 2024-02-29 at 13.49.12" data-base62-sha1="qX5m1MUV3V3Sdysx39lbSmYq0GS" width="583" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bce661c19bf71c25c12301e3d6075925cb0e2f92_2_583x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bce661c19bf71c25c12301e3d6075925cb0e2f92_2_874x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bce661c19bf71c25c12301e3d6075925cb0e2f92_2_1166x1000.png 2x" data-dominant-color="3E4045"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-02-29 at 13.49.12</span><span class="informations">1546×1324 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>cheers</p>

---

## Post #2 by @pieper (2024-02-29 19:41 UTC)

<p>Rasterizing an STL file can lead to problems like this when the triangles are small or there are other numerical issues.  Try changing the segmentation geometry in the segment editor.</p>

---

## Post #3 by @richyrich (2024-03-01 14:35 UTC)

<p>Thanks Steve.<br>
If I import as the file as Model, I need to export it as labelmap first, which leads me to the same results as when I am importing it directly as Segmentation.<br>
In both options, I cannot do much manipulations/improvements in the segment editor, much less centerline calculations.</p>

---

## Post #4 by @pieper (2024-03-01 14:45 UTC)

<p>What I mean is that you may need to change the spacing or orientation of the sampling grid to avoid this kind of numerical issue.  If you load the stl as a segmentation, it will stay as a surface definition until another representation is needed.  You can control this process in the segmentations module.  Maybe setting the oversampling is enough or maybe you need to try some other options.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/481f89bee3ea9d4c4a6cd7b79758a09be73207ca.png" data-download-href="/uploads/short-url/ai1WLCNZf515tdlvbRTARvHt8Ho.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/481f89bee3ea9d4c4a6cd7b79758a09be73207ca_2_430x500.png" alt="image" data-base62-sha1="ai1WLCNZf515tdlvbRTARvHt8Ho" width="430" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/481f89bee3ea9d4c4a6cd7b79758a09be73207ca_2_430x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/481f89bee3ea9d4c4a6cd7b79758a09be73207ca_2_645x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/481f89bee3ea9d4c4a6cd7b79758a09be73207ca_2_860x1000.png 2x" data-dominant-color="D0D1D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">891×1034 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
