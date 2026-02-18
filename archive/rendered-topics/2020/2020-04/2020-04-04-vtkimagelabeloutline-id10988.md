# vtkImageLabelOutline

**Topic ID**: 10988
**Date**: 2020-04-04
**URL**: https://discourse.slicer.org/t/vtkimagelabeloutline/10988

---

## Post #1 by @loubna (2020-04-04 17:24 UTC)

<p>Hi,</p>
<p>my question is when we apply vtkImageLabelOutline filter on labelMap means get the 2D contours of segmented slices or not?what is the difference between the 2d contours obtained from segmented slices and the results given by vtkImageLabelOutline.</p>
<p>thank’s in advance</p>

---

## Post #2 by @lassoan (2020-04-04 17:43 UTC)

<p>vtkImageLabelOutline takes a labelmap image as input and provides a labelmap image as output where all “internal” pixels are cleared (so that only boundary pixels are left). This is used in Slicer for highlighting boundaries when displaying labelmap volumes and segmentations in slice views.</p>

---

## Post #3 by @loubna (2020-04-04 17:52 UTC)

<p>Thank you so much for the response<br>
there are some 3d reconstrction methods that allow to reconstruct 3D models from 2d contours like the method implemented in SlicerRt which convert 2d contours to 3d smoothed surface (more precisely the converter rule : **vtkPlanarContourToClosedSurfaceConversionRule". can I use vtkImageLabelOutline to get 2D contours or i must segment each 2d image and exract the contour ?</p>

---

## Post #4 by @loubna (2020-04-04 18:17 UTC)

<p>In fact  I would like to extract the point set (cloud) of the label contours, compute the point gradiants and a pply a 3d reconstrcution method. vtkImageLabelOutline does not seem providing good results  are there Vtk filters to do that,</p>

---

## Post #5 by @lassoan (2020-04-04 18:23 UTC)

<p>“Planar contour” representation is a set of polygons on parallel planes, while output of the image label outline filter is a 3D image.</p>
<p>SlicerRT extension’s planar contour to closed surface conversion rule creates a 3D surface. You can have a look at it how it works and modify it to do what you want.</p>
<p>Note that “planar contours” representation is already a point cloud, but it also has very valuable point connectivity information, which allows reconstruction of much more elaborate surfaces.</p>

---

## Post #6 by @loubna (2020-04-06 17:52 UTC)

<p>Thank’s again for the response.</p>
<p>I have a question that seems important, you know that 3d reconstruction methods which use implicit function depend to the precision of normal vectors.</p>
<p>To compute normal vectors from labelMap, I have applied gaussian and gradians filters to get the normal vectors. I have used Cast filter also to avoid providing null normal vectors. Bt I don’t get good results. My question is : I want extract ponts from labelMap, convert them to RAS space and apply “vtkPCANormalEstimation” to estimate normal vector.</p>
<p>I want normal vectors points outside.  but I don’t knwo if it is the right choice</p>

---

## Post #7 by @lassoan (2020-04-06 18:03 UTC)

<p><a href="https://vtk.org/doc/nightly/html/classvtkPCANormalEstimation.html">vtkPCANormalEstimation</a> is not relevant here, as it works on unorganized point clouds, while here you know the geometry (you have contours organized in planes). Ignoring connectivity information and treating contour points as a point cloud would lead to very bad quality results, especially when the contours are relatively far away from each other (farther than neighbor points from each other within a contour).</p>
<p>In other posts, I already explained in detail how you can get point normals (smoothing the binary labelmap and computing image gradient).</p>

---

## Post #8 by @loubna (2020-04-06 18:09 UTC)

<p>Yes is exactly what I did, But I don’t want compute normal vectors of the entire labelMap , so I need to apply first “vtkImageLabelOutline”  to clear internal pixels and left only boundry pixels, can I apply the series of filters (cast filter, gaussain, gradiant…) on labelMap boundries or it is wrong because apply my implicit method on the entire labelMap does not seem work. It is just an idea beacuse planar contours representation is not supported yet in 3d slicer</p>

---

## Post #9 by @lassoan (2020-04-06 18:28 UTC)

<aside class="quote no-group" data-username="loubna" data-post="8" data-topic="10988">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/cab0a1/48.png" class="avatar"> loubna:</div>
<blockquote>
<p>But I don’t want compute normal vectors of the entire labelMap</p>
</blockquote>
</aside>
<p>Why not? It should be really fast.</p>

---

## Post #10 by @loubna (2020-04-06 18:29 UTC)

<p>because the method that I want implement operates only on boundries that is why i have applied “vtkImageLabelOutline”</p>

---

## Post #11 by @lassoan (2020-04-06 18:34 UTC)

<p>You need to compute the gradient on the original labelmap (not on the labelmap outline).</p>

---

## Post #12 by @loubna (2020-04-06 18:50 UTC)

<p>I think the only solution is to compute gradient on the original labelMap then get the gradients of the labelMpa outlines using vtkProbeFilter</p>

---
