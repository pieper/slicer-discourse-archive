# Create mesh from binary image

**Topic ID**: 23179
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/create-mesh-from-binary-image/23179

---

## Post #1 by @Tutti (2022-04-28 16:47 UTC)

<p>Hello everyone,</p>
<p>From an airway Dicom image (.hdr) with the background = 0, and airway = 255, I would like to create the mesh to perform simulation later from this image by Slicer3D. After reading some guidance, I used Segment Editor to segment the airway part and export it to model, it has some problems:</p>
<ol>
<li>I used threshold with a range [1:255] to segment the airway (without smoothing), but it does not capture all pixels (Fig1). Is there any other method to obtain mesh image?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed26e1833c458a0ba4a00b9c33190677dfa1bc8b.jpeg" alt="F1" data-base62-sha1="xPWsFGYTbaAhBt5WkvDCUi24AGf" width="390" height="327">
</li>
<li>After obtaining the segmented image, I used Surface toolbox to smooth the surface of airway mesh with the Taubin method (Fig2) without shrinkage (it is better than Laplacian in my case). Is there any method I can compare with Taubin (from Slicer/VTK code)?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a88d010708abb04db181cdd76063b54fc543c3c8.jpeg" data-download-href="/uploads/short-url/o34jvREF8UaLChtP3VPQ5XWxR68.jpeg?dl=1" title="F2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a88d010708abb04db181cdd76063b54fc543c3c8_2_489x500.jpeg" alt="F2" data-base62-sha1="o34jvREF8UaLChtP3VPQ5XWxR68" width="489" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a88d010708abb04db181cdd76063b54fc543c3c8_2_489x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a88d010708abb04db181cdd76063b54fc543c3c8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a88d010708abb04db181cdd76063b54fc543c3c8.jpeg 2x" data-dominant-color="8E90C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">F2</span><span class="informations">684×699 44.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
<li>Is smoothing before creating mesh image or after meshing better?<br>
Could you please suggest what I might try?</li>
</ol>
<p>Many thanks,</p>

---
