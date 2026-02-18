# Export segmentation contour from cine-mri images (one single time frame)

**Topic ID**: 22411
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/export-segmentation-contour-from-cine-mri-images-one-single-time-frame/22411

---

## Post #1 by @MSensale (2022-03-09 14:50 UTC)

<p>Hi 3D Slicer Community !</p>
<p>My name is Marco and I am a PhD student passionated about medical images based modelling.</p>
<p>I would like to ask support about exporting the segmentation contour of a mask.</p>
<p>I am working with cine-mri images of the human aorta. With this kind of imaging technique, you can get the in-plane motion of the aorta over the time. In this case, the time resolution is about 25 frames for cardiac cycle. My aim is to estimate the motion of the aorta from cine-mri images.</p>
<p>I segmented manually each frame (therefore one single slice for each frame). An example of segmentation for one frame is reported below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e52e9d3345919ba670dcfb0ea645e7516f273cb.jpeg" data-download-href="/uploads/short-url/4kfXQgfmEg83ZIqD30WvoeNMeSL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e52e9d3345919ba670dcfb0ea645e7516f273cb_2_390x500.jpeg" alt="image" data-base62-sha1="4kfXQgfmEg83ZIqD30WvoeNMeSL" width="390" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e52e9d3345919ba670dcfb0ea645e7516f273cb_2_390x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e52e9d3345919ba670dcfb0ea645e7516f273cb_2_585x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e52e9d3345919ba670dcfb0ea645e7516f273cb.jpeg 2x" data-dominant-color="444A44"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">729×934 61.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If I untick the Slice Fill option, I get the contour of the segmetation as shown in the image below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0335846632f161a5966820f3e44cd29c46e08365.jpeg" data-download-href="/uploads/short-url/so5Jnt2MYGBeyPSLRZQK57Jidf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0335846632f161a5966820f3e44cd29c46e08365_2_355x500.jpeg" alt="image" data-base62-sha1="so5Jnt2MYGBeyPSLRZQK57Jidf" width="355" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0335846632f161a5966820f3e44cd29c46e08365_2_355x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0335846632f161a5966820f3e44cd29c46e08365_2_532x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0335846632f161a5966820f3e44cd29c46e08365.jpeg 2x" data-dominant-color="4A4A4A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">642×903 58.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In that image, the contour of the segmentation is represented by a broken line. The broken line is made up by joining several points. These points are corners of pixels in the slice and are associated with some x, y and z coordinates.</p>
<p>I am looking for a method to store those coordinates.</p>
<p>I have seen similar topics at:<br>
<a href="https://discourse.slicer.org/t/extract-contours-only-from-a-segmentation/1853">Extract contours only from a segmentation - Support - 3D Slicer Community</a></p>
<p>And found that the vtkImageLabelOutline should be the right filter for this task. However it does not seem to be available in Python API.</p>
<p>It would be great if someone would like to share his/her ideas.</p>
<p>Thanks,</p>
<p>Marco</p>

---

## Post #2 by @pieper (2022-03-10 00:11 UTC)

<p>I guess this is a sequence of 2D frames?  If so you might try this class:</p>
<p><a href="https://vtk.org/doc/nightly/html/classvtkFlyingEdges2D.html#details" class="onebox" target="_blank" rel="noopener">https://vtk.org/doc/nightly/html/classvtkFlyingEdges2D.html#details</a></p>
<p>Otherwise if it’s 3D you could just export to a surface model and get the vertices.</p>

---

## Post #3 by @MSensale (2022-03-10 16:53 UTC)

<p>Hi Steve,</p>
<p>Many thanks for your answer.</p>
<p>Indeed, it is a sequence of 2D frames and the class you suggested seems to do exactly what I am looking for. I will try it and let you know.</p>
<p>Thanks</p>
<p>Marco</p>

---

## Post #4 by @MSensale (2022-03-14 14:22 UTC)

<p>Hi Steve,<br>
Thanks again for your suggestion.<br>
In the description of the vtkFlyingEdges2D filter it is written: “If you are interested in extracting segmented regions from a label mask, consider using <a href="https://vtk.org/doc/nightly/html/classvtkDiscreteFlyingEdges2D.html" rel="noopener nofollow ugc">vtkDiscreteFlyingEdges2D</a>.”</p>
<p>I implemented this filter in my code and it does perfectly what I asked in the post.</p>
<p>Thanks,</p>
<p>Marco</p>

---
