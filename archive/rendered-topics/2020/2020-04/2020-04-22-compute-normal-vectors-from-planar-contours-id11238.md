# Compute normal vectors from planar contours

**Topic ID**: 11238
**Date**: 2020-04-22
**URL**: https://discourse.slicer.org/t/compute-normal-vectors-from-planar-contours/11238

---

## Post #1 by @loubna (2020-04-22 06:11 UTC)

<p>Hi,</p>
<p>Is it possible to compute normal vectors for each 3D point of planar contour in SlicerRT? If yes , how we can do it.</p>
<p>thank’s in advance</p>

---

## Post #2 by @gcsharp (2020-04-22 22:59 UTC)

<p>Computing surface normals is not a SlicerRT function.  I am not an expert, but I think converting to model representation would be the first step.  In what format would you want the normal vectors and why do you think you need them?</p>

---

## Post #3 by @loubna (2020-04-23 15:59 UTC)

<p>I want implement an implicit method to construct a 3D surface from a set of planar contours. So I need to compute a normal vector for each 3D point of the contour to be able to evalute the implicit function. More precisely, i want convert planar contours to a 3D surface using the converter rule planarcontoursto3d surface. there is an interpolation method in slicerRT but the compute of the 3d surface via this method does not need the knowledge of normal of each 3D point.</p>

---

## Post #4 by @lassoan (2020-04-24 04:13 UTC)

<aside class="quote no-group" data-username="loubna" data-post="3" data-topic="11238">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/cab0a1/48.png" class="avatar"> loubna:</div>
<blockquote>
<p>I need to compute a normal vector for each 3D point of the contour to be able to evalute the implicit function</p>
</blockquote>
</aside>
<p>Computing the normal vector correctly is hard (comparable to the difficulty of reconstructing a surface). SlicerRT can compute it after it has already reconstructed the closed surface.</p>

---

## Post #5 by @loubna (2020-04-24 22:42 UTC)

<p>Hi professor;</p>
<p>thank’s for the response. I just  want to know if I can access to the points of each contour separately?. I want implement a flood fill algorithm  in order to be able to compute an approximate normal vector.</p>
<p>Thank’s in advance</p>

---

## Post #6 by @lassoan (2020-04-24 22:45 UTC)

<p>You can find the closest point on the reconstructed surface using a <a href="https://vtk.org/doc/nightly/html/classvtkPointLocator.html#a7ab83a64b5035755c440922a8db6a1dc">VTK locator</a> and get the surface normal from there.</p>

---

## Post #7 by @loubna (2020-04-24 22:53 UTC)

<p>but i need to knwo the normal vector before reconstructing the 3D surface . I have implemented the implicot method in 3D slicer but the results were not very satisfactory. So i want reimplement it in SlicerRT because the planar contours is the master representation.</p>
<p>I thought modify thie existing method <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.h" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.h</a></p>
<p>but there are just  vtkPolyData* inputROIPoints which contains all points of all contours. Is there any way to extract the points of each contours from inputROIPoints?</p>

---

## Post #8 by @lassoan (2020-04-24 23:04 UTC)

<p>You can let SlicerRT reconstruct the surface and provide you the normals. If your reconstructed surface is significantly better than what SlicerRT generates then you can start thinking about how to get the normals (if it’s OK to use SlicerRT as a preprocessor or you want to use an alternative normal estimation method).</p>

---

## Post #9 by @Chris_Rorden (2020-04-25 12:21 UTC)

<p>If you want to compute the surface normal for a triangulated mesh, you simply compute the cross-product for two sides. The winding-order of the triangles is crucial to disambiguate the front and back face of the triangle.</p>
<p>If you can to compute the surface normal for a voxelwise 3D image (using the intensity of each voxel), you can compute the <a href="https://www.mccauslandcenter.sc.edu/mricrogl/gradients" rel="nofollow noopener">gradient</a> using a Sobel operator. You can do this using the CPU, but tor 3D textures a GPU using GLSL is tremendously faster. CPU and GLSL code is provided with <a href="https://github.com/rordenlab/MRIcroGL12" rel="nofollow noopener">MRIcroGL</a>. MRIcroGL does this once for the entire 3D volume to help estimate lighting (specular, diffuse, MatCaps).</p>

---

## Post #10 by @loubna (2020-04-25 14:54 UTC)

<p>In vtkPlanarContourToClosedSurfaceConversionRule, all contours are set to be counter-clockwise ? I don’t understand what is the difference between counter-clockwise and clockwise contours.</p>
<p>Do you mean by this the existence of small contours inside the large contour?</p>

---

## Post #11 by @lassoan (2020-04-25 15:12 UTC)

<p>In computer graphics, direction of a polygon (which way direction is towards inside/outside) is usually defined by its winding.</p>
<p>In planar contours in DICOM RTSTRUCT information objects, winding is not used. Instead, concavities (which may appear as holes in planar contours) and holes are specified using keyhole technique. See details in the DICOM standard.</p>

---

## Post #13 by @cpinter (2020-04-27 08:52 UTC)

<p>SlicerRT building instructions can be found here: <a href="https://github.com/SlicerRt/SlicerRT/wiki/SlicerRt-developers-page">https://github.com/SlicerRt/SlicerRT/wiki/SlicerRt-developers-page</a></p>
<p>If you mention any errors, it is very useful to actually send those errors so that we can give a meaningful answer.</p>

---

## Post #17 by @lassoan (2020-04-27 20:56 UTC)

<p>If you build your own Sicer, then you also need to build all extensions you need. It is very simple to do that, just clone the repository on your computer, configure with CMake (set you Slicer-build folder as Slicer_DIR), and build.</p>

---

## Post #19 by @lassoan (2020-04-27 21:01 UTC)

<p>In Visual Studio, you need to choose the same build configuration (Debug/Release) that you chose when you built Slicer.</p>

---

## Post #24 by @gcsharp (2020-04-29 03:18 UTC)

<p>The repository you cloned is a fork of the official repository.  It was forked May 2018, and therefore it is two years out of date.</p>

---

## Post #26 by @loubna (2020-05-12 15:58 UTC)

<p>Hi Mr;</p>
<p>thank’s forthe reply. I search in MRIcroGL code but i Don’t found how the normal vectors are computed from binary volume using filters on CPU. Can you give me more précisions please.</p>
<p>thank’s in advance</p>

---

## Post #27 by @Chris_Rorden (2020-05-12 17:33 UTC)

<p>The function <a href="https://github.com/rordenlab/MRIcroGL12/blob/d151da089dacd7bd4b4f4e78e0ebe835de585644/nifti.pas" rel="nofollow noopener">sobel()</a> estimates the <a href="https://en.wikipedia.org/wiki/Sobel_operator" rel="nofollow noopener">Sobel operator</a>.</p>
<p>This is easiest to describe in 2D, where each pixel has 8 neighbors (in 3D each voxel has 26 neighbors that share a face, edge or corner). Since the principle is the same, I will describe for 2D. Consider a 2D image where each pixel has 8 neighbors that are Left/Right(L/R), Up/Down(U/D) from the center: LU, U, RU, L, R, LD, D, RD.</p>
<p>The left-right gradient <code>x</code> is<br>
<code>x = (LU+2*L+LD) - (RU+2*R+RD)</code><br>
The up-down gradient <code>y</code> is<br>
<code>y = (LU+2*U+RU) - (LD+2*D+RD)</code></p>
<p>Extending to 3 dimensions is described <a href="https://en.wikipedia.org/wiki/Sobel_operator#Extension_to_other_dimensions" rel="nofollow noopener">here</a>.</p>

---

## Post #28 by @loubna (2020-05-12 17:53 UTC)

<p>thank’s again for reply. what about “vtkImageSobel3D”?</p>
<p>I have applied gaussian filter to blur the binary volume folowed by vtkImageSobel3D but i have artifacts in some régions of model.  what is the difference by the sobel operator illustrated in your exemple the the vtkSobelImage filter.? the both give same results?</p>

---

## Post #29 by @Chris_Rorden (2020-05-14 15:28 UTC)

<p>You can see the code for <a href="https://github.com/Kitware/VTK/blob/master/Imaging/General/vtkImageSobel3D.cxx" rel="noopener nofollow ugc">vtkImageSobel3D.cxx</a> here. It is conceptually identical to the <a href="https://en.wikipedia.org/wiki/Sobel_operator#Extension_to_other_dimensions" rel="noopener nofollow ugc">wiki Sobel 3D</a> formula. The wiki uses weights 1,2,4 for voxels that share a corner, edge or face while VTK uses the weights 1, 1.71, 3.41. These should provide very similar results.</p>
<p>In general, your approach of applying a Gaussian blur prior to a Sobel is a wise choice. I am not sure what artifacts you are experiencing. Working with binary data might be part of the issue.  If you look at my application, I apply these to continuous data (e.g. different voxels in CT and MRI have slightly different intensities). Specifically, I usually apply it to the alpha channel (transparency) of the image I am working with. Below is an example of a CT scan with a window center of 188 and a window width of 288 (in Hounsfield units). The horizontal axis in the graph shows the selected intensity range (from 114…302) and the vertical axis shows the alpha channel, which in this case is a linear ramp. Thus, values darker than 114 are completely transparent and values greater than 302 are completely opaque. Intermediate values are translucent. Using this approach helps with partial volume issues (e.g. a voxel that is only partially bone). The gradient is shown on the right. So my sense is you want to think about a segmentation that is continuous rather than binary to capture partial volume effects.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9e50b7415555e409b2138a7dbe76b7e4656dfff.jpeg" data-download-href="/uploads/short-url/qwv3BqUz0nkoNtc2b9h0cIQuGiH.jpeg?dl=1" title="gradient" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9e50b7415555e409b2138a7dbe76b7e4656dfff_2_690x491.jpeg" alt="gradient" data-base62-sha1="qwv3BqUz0nkoNtc2b9h0cIQuGiH" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9e50b7415555e409b2138a7dbe76b7e4656dfff_2_690x491.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9e50b7415555e409b2138a7dbe76b7e4656dfff.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9e50b7415555e409b2138a7dbe76b7e4656dfff.jpeg 2x" data-dominant-color="C8BFBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">gradient</span><span class="informations">878×625 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #30 by @loubna (2020-05-16 21:47 UTC)

<p>Thank you so much for clarification</p>

---
