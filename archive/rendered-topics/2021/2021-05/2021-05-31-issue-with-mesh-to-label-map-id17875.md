# Issue with Mesh to Label Map

**Topic ID**: 17875
**Date**: 2021-05-31
**URL**: https://discourse.slicer.org/t/issue-with-mesh-to-label-map/17875

---

## Post #1 by @quan (2021-05-31 00:51 UTC)

<p>I’m trying to generate a SPHARM-PDM mesh from a .stl file. I imported the .stl and used “Mesh to Label Map” to obtain the .nrrd. However, the .nrrd is inverted (the white space are supposed to be black and vice versa). This inversion caused the final SPHARM-PDM mesh to be a rectangular box with a hole inside with the shape of my original mesh. How do I get my current procedure to work correctly?</p>
<p>Original mesh + generated label mesh:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ae2526be241233b900e0387c4ee7aebc0cb0f4c.png" data-download-href="/uploads/short-url/67mWFEjR3pVXJvHzQ3TmYo6BSOw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ae2526be241233b900e0387c4ee7aebc0cb0f4c_2_690x452.png" alt="image" data-base62-sha1="67mWFEjR3pVXJvHzQ3TmYo6BSOw" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ae2526be241233b900e0387c4ee7aebc0cb0f4c_2_690x452.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ae2526be241233b900e0387c4ee7aebc0cb0f4c_2_1035x678.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ae2526be241233b900e0387c4ee7aebc0cb0f4c_2_1380x904.png 2x" data-dominant-color="7E7F97"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1424×933 48.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Final SPHARM-PDM mesh:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7d3f5b89bfe83ac14b4b1284d9eb9f1cf779ac2.png" data-download-href="/uploads/short-url/qeduW373R1f9HnKbZzhH2bOhKo2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7d3f5b89bfe83ac14b4b1284d9eb9f1cf779ac2_2_403x500.png" alt="image" data-base62-sha1="qeduW373R1f9HnKbZzhH2bOhKo2" width="403" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7d3f5b89bfe83ac14b4b1284d9eb9f1cf779ac2_2_403x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7d3f5b89bfe83ac14b4b1284d9eb9f1cf779ac2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7d3f5b89bfe83ac14b4b1284d9eb9f1cf779ac2.png 2x" data-dominant-color="77787F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">585×725 61.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-05-31 23:30 UTC)

<p>Probably “Mesh to label map” module does not know what is inside/outside because the model is not fully enclosed by the output image. You may also try the very similar “Model to Labelmap” module in Slicer core.</p>
<p>If you want a method that is simple and works more robustly then convert the model to segmentation (by right-clicking on the model in Data module), and then export the segmentation to binary labelmap (by right-clicking on the segmentation in Data module).</p>
<p>You can fine-tune conversion parameters in segmentation module (resolution, smoothing, decimation) if the default quality is not sufficient.</p>

---

## Post #3 by @quan (2021-06-01 05:18 UTC)

<p>The “convert the model to segmentation” then “export the segmentation to binary labelmap” method works very well. Thank you for the help.</p>

---
