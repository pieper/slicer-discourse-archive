---
topic_id: 13174
title: "Created An Stl File From Numpy Array But Unable To Get This"
date: 2020-08-26
url: https://discourse.slicer.org/t/13174
---

# Created an STL file from numpy array but unable to get this aligned with dicom volume after loading

**Topic ID**: 13174
**Date**: 2020-08-26
**URL**: https://discourse.slicer.org/t/created-an-stl-file-from-numpy-array-but-unable-to-get-this-aligned-with-dicom-volume-after-loading/13174

---

## Post #1 by @Gabriel_T (2020-08-26 13:19 UTC)

<p>I have a binary segmentation mask, I converted this to an STL file. I converted to mm space from pixel coordinate space by</p>
<ol>
<li>Finding the coordinates of the vertices using marching cubes lewinn algorithm from skimage</li>
<li>multiplying the coordinates of the vertices with the corresponding x,y,z pixel spacing and adding the ImagePositionPatient of the first dicom slice obtained from the dicom meta tags</li>
<li>convert to stl using numpy-stl</li>
</ol>
<p>When I load the image it seems that the loaded STL is having the same size and shape, but it has some rotational and translational offset, how do I form the stl file so that it is automatically aligned as soon as I load ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e8b299dfc81ea18ad1b0c420698a2e3deb1c568.jpeg" data-download-href="/uploads/short-url/6DK7jQfwY6XlrCsQg5TigFfeGmc.jpeg?dl=1" title="slicer3dstl" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e8b299dfc81ea18ad1b0c420698a2e3deb1c568_2_563x499.jpeg" alt="slicer3dstl" data-base62-sha1="6DK7jQfwY6XlrCsQg5TigFfeGmc" width="563" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e8b299dfc81ea18ad1b0c420698a2e3deb1c568_2_563x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e8b299dfc81ea18ad1b0c420698a2e3deb1c568_2_844x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e8b299dfc81ea18ad1b0c420698a2e3deb1c568_2_1126x998.jpeg 2x" data-dominant-color="9B9DA4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer3dstl</span><span class="informations">1889×1676 514 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-08-26 15:25 UTC)

<p>I would recommend to convert form segmentation to STL using Slicer. If you use skimage or other basic Python tools that are not intended for medical imaging, then most likely they don’t handle image origin, spacing, axis directions properly and may not be aware of commond anatomical coordinate systems conventions (RAS/LPS). You can of course figure out and apply the transform manually, it is just a bit more work for you.</p>

---

## Post #3 by @Gabriel_T (2020-08-31 00:14 UTC)

<p>Thank you for the response, how do I apply the transform manually ? since all my segmentations are computer generated and not manually generated I store the coordinates as numpy array.</p>

---

## Post #4 by @lassoan (2020-08-31 01:22 UTC)

<p>If you want to apply a linear transform (translation, rotation, scaling) to a mesh then you can represent it as a homogeneous transformation matrix and apply to all the mesh points by a single matrix multiplication. Constructing this transform and applying it manually is a useful learning exercise, but normally you would just use labelmap image &lt;-&gt; segmentation &lt;-&gt; mesh conversions that are conveniently available in Slicer (including all necessary coordinate system transformations, mesh smoothing, etc.). It takes two clicks of a button (right-click on the labelmap, segmentation, or model node in Data module then choose what you want to convert to) or by running a few lines of Python code (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_nodes_from_segmentation_node">examples in script repository</a>).</p>

---
