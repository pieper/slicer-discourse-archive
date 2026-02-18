# The perfect STL file for the 3D print job

**Topic ID**: 15418
**Date**: 2021-01-09
**URL**: https://discourse.slicer.org/t/the-perfect-stl-file-for-the-3d-print-job/15418

---

## Post #1 by @Andreas (2021-01-09 15:32 UTC)

<p>Hello everybody,</p>
<p>I would like to know how to create the perfect STL file for the 3D printing job.</p>
<p>In my previous 3D vessel models, the triangles (polygons) are still clearly visible on the surface network. (Python coding)</p>
<p>However, it should be noted that the print job came out very well despite this “resolution”. It is probably just the representation in the software and does not reflect the actual surface properties of the model.</p>
<p>Is there a way to increase / improve the resolution of the STL file without distorting the wall thickness?</p>
<p>Uniform wall thickness has a higher priority than perfect representation in the program.</p>
<p>Many thanks for your help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5342547b12a68745d97458c4056464f89d10c036.jpeg" data-download-href="/uploads/short-url/bSxJY1TOkDX2NhE6DEjZK0noNfw.jpeg?dl=1" title="poly22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5342547b12a68745d97458c4056464f89d10c036_2_639x500.jpeg" alt="poly22" data-base62-sha1="bSxJY1TOkDX2NhE6DEjZK0noNfw" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5342547b12a68745d97458c4056464f89d10c036_2_639x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5342547b12a68745d97458c4056464f89d10c036_2_958x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5342547b12a68745d97458c4056464f89d10c036.jpeg 2x" data-dominant-color="9D95A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">poly22</span><span class="informations">1137×889 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14e252ed54b240ce921ef0d6fc1a6439fbba4f3f.jpeg" data-download-href="/uploads/short-url/2YKrFcbVmAE6I2hThex0wHf8O0D.jpeg?dl=1" title="poly1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14e252ed54b240ce921ef0d6fc1a6439fbba4f3f_2_634x500.jpeg" alt="poly1" data-base62-sha1="2YKrFcbVmAE6I2hThex0wHf8O0D" width="634" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14e252ed54b240ce921ef0d6fc1a6439fbba4f3f_2_634x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14e252ed54b240ce921ef0d6fc1a6439fbba4f3f_2_951x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14e252ed54b240ce921ef0d6fc1a6439fbba4f3f.jpeg 2x" data-dominant-color="9A9094"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">poly1</span><span class="informations">1137×896 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-01-09 15:38 UTC)

<p>This model looks high quality. You can choose to make individual triangles visible by using flat shading (this is what you show above). If you don’t want to see each triangle then all you need to do is compute surface normals using Surface Toolbox module.</p>

---
