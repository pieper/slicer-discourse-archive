---
topic_id: 410
title: "Extract Labelmap Contour"
date: 2017-05-31
url: https://discourse.slicer.org/t/410
---

# Extract labelmap contour

**Topic ID**: 410
**Date**: 2017-05-31
**URL**: https://discourse.slicer.org/t/extract-labelmap-contour/410

---

## Post #1 by @DanC (2017-05-31 22:09 UTC)

<p>Hi.<br>
I would like to extract the contour of the labelmap saved in a nrrd file using itk filters. It seems that the toggle button for the label map in the reslice viewers has this functionality. Is there a sample code of this functionality that I could search for? I’ve been trying to use the itk::BinaryContourImageFilter, but cannot get it to work.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2017-06-02 14:23 UTC)

<p>Would you like an image, a closed surface, or a set of planar contours? In what file format?</p>

---

## Post #3 by @DanC (2017-06-02 21:18 UTC)

<p>I would like to extract the point set (cloud) of the label contours. Here is my current code.<br>
Thanks!</p>
<pre><code>// declare the image class
typedef itk::Image&lt;float, 3&gt;                      OriginalImageType;

//  -Read in label map
typedef itk::ImageFileReader&lt;OriginalImageType&gt; itkReaderType;
itkReaderType::Pointer itkreader = itkReaderType::New();
itkreader-&gt;SetFileName("label.nrrd");
itkreader-&gt;Update();

OriginalImageType::Pointer outImage = itkreader-&gt;GetOutput();

// Extract point data from label map
typedef itk::ImageRegionConstIterator&lt; OriginalImageType &gt; IteratorType;
typedef itk::PointSet&lt; float, 3 &gt; KdPointSetType;
typedef KdPointSetType::PointType     KdPointType;

IteratorType it(outImage, outImage-&gt;GetBufferedRegion());
it.GoToBegin();

KdPointSetType::Pointer  PointSet = KdPointSetType::New();
KdPointType point;

unsigned long pointId = 0;
	
while (!it.IsAtEnd())
{
	// Convert the pixel position into a Point
	outImage-&gt;TransformIndexToPhysicalPoint(it.GetIndex(), point);
	PointSet-&gt;SetPoint(pointId, point);
	// Transfer the pixel data to the value associated with the point.
	PointSet-&gt;SetPointData(pointId, it.Get());
	++it;
	++pointId;
}
std::cout &lt;&lt; "Number Of Points = " &lt;&lt; PointSet-&gt;GetNumberOfPoints() &lt;&lt; std::endl;</code></pre>

---

## Post #4 by @lassoan (2017-06-02 21:49 UTC)

<p>If you only have a point cloud then you cannot do much with your data (because you don’t know what is inside/outside, you don’t have surface normals, you don’t have surfaces that you can render, etc). until you reconstruct a surface.</p>
<p>That’s why typically you run a marching cubes filter to create surface mesh from the image.</p>

---

## Post #5 by @DanC (2017-06-02 22:01 UTC)

<p>I am trying to write a deformablemesh surface filter that would deform against the point cloud of the surface. The slicers are so far apart that the marching cubes won’t give a satisfying result. Thanks for the help!</p>

---

## Post #6 by @lassoan (2017-06-02 22:20 UTC)

<p>Reconstruction from point cloud is a much difficult problem than smooth interpolation between slices, so that’s not a good direction to explore.</p>
<p>Instead, create a high-resolution labelmap with isotropic spacing (preferably create a high-res labelmap in the first place by segmenting an isotropic supersampled  input volume) using Crop volume module. For deformation, use Transforms module directly on the labelmap; or import the labelmap to a Segmentation node, create closed surface representation (point cloud with connectivity; you can apply smoothing on the labelmap in Segment editor; or during conversion to closed surface), make it the master representation and apply transform to that.</p>
<p>No need for any custom module development, these are all very common tasks.</p>

---

## Post #7 by @Lorensen (2017-06-02 23:42 UTC)

<p>Vtk has recently added a number of point cloud filters. See<br>
<a href="https://lorensen.github.io/VTKExamples/site/Cxx/#point-cloud-operations" class="onebox" target="_blank" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/Cxx/#point-cloud-operations</a></p>
<p>In particular there is a new surface construction filter:<br>
<a href="https://lorensen.github.io/VTKExamples/site/Cxx/Points/ExtractSurface/" class="onebox" target="_blank" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/Cxx/Points/ExtractSurface/</a></p>

---

## Post #8 by @lassoan (2017-06-03 03:42 UTC)

<p>Thanks Bill for the links. These methods are useful when you don’t have connectivity information in your point cloud and you want to reconstruct only a single structure.</p>
<p>If you have connectivity information between the points (you have a surface mesh), then it would be a huge mistake to discard that information. Even when connectivity information within an image slice is available and you only miss connectivity info between slices (this is how segmentation is stored in DICOM-RT structure sets), there is a lot of ambiguity in reconstructing the surface. There is an <a href="https://app.assembla.com/spaces/slicerrt/subversion/source/HEAD/trunk/SlicerRt/src/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx">algorithm for this in SlicerRT</a>, that can reconstruct nice smooth surfaces most of the time while preserve most details, it’s quite tricky and in some cases the results are still not optimal.</p>
<p>I think any of these methods would give better results (no reconstruction errors, controllable smoothing, works well with multiple labels):</p>
<ul>
<li>Option A. Convert labelmap to mesh, smooth the mesh, then convert back to labelmap. This method is implemented in the Segment Editor: Smoothing effect, Joint smoothing method. This is somewhat similar to what <a class="mention" href="/u/danc">@DanC</a> may try to achieve, but with the important difference of not discarding connectivity information when we convert labelmap to mesh.</li>
<li>Option B. Reduce the slice spacing to approximately match in-slice pixel size and insert empty slices between the original slices. Then run <a href="https://github.com/KitwareMedical/ITKMorphologicalContourInterpolation">morphological contour interpolation</a>. The morphological interpolator is available in Slicer in the Segment editor module, as <code>Interpolate between slices</code> effect.</li>
<li>Option C. Supersample the labelmap and apply smoothing (median filter, morphological operators, Gaussian, etc). These are available in Segment editor’s smoothing effect.</li>
</ul>

---

## Post #9 by @DanC (2017-06-03 17:31 UTC)

<p>Thanks for the suggestions Andras.</p>
<p>I am trying to reconstruct histological cross sections of a prostate including other structures such as urethra,etc.<br>
The spacing of the image set is 0.07 x 0.07 x 2 mm.<br>
The cross sections varies so much between images, that any smoothing or interpolation I’ve tried in slicer would not give a continuous surface.Hence I was trying to explore a totally different approach. The urethra would look like a spine instead of a continuous surface after reconstruction.</p>
<p>Option A. Are the suggested algorithms different than the ones used in the Model Maker Module? The smoothing/ joint smoothing in the model maker module wasn’t good enough in my case.<br>
Option B.  I will try the morphological contour interpolation. I wan’t aware of this new function.<br>
Option C. Does supersample meen to resample with smaller spacing between slices with interpolation?</p>
<p>Thanks!</p>

---

## Post #10 by @DanC (2017-06-03 17:33 UTC)

<p>Hi Bill.<br>
Thank for the suggestion. I will definitely explore these if I go this direction.</p>
<p>Any suggestions to extract the contour points from the Slicer label maps? I currently am able to save the point set of all filled voxels using ITK.</p>
<p>Thanks!</p>

---

## Post #11 by @lassoan (2017-06-03 17:58 UTC)

<aside class="quote no-group" data-username="DanC" data-post="9" data-topic="410">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/77aa72/48.png" class="avatar"> DanC:</div>
<blockquote>
<p>Are the suggested algorithms different than the ones used in the Model Maker Module?</p>
</blockquote>
</aside>
<p>The one in Segment Editor is slightly improved, but it still won’t be able to do any good if voxel spacing is highly anisotropic (you’ll see staircase artifacts or you’ll lose details in the reconstructed surface). <strong>If spacing of your volume differs more than about 10% between axes then first you have to crop&amp;resample your volume using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/CropVolume">Crop Volume</a> module.</strong></p>
<p>So, before trying any of the recommended options, you must resample your input volume.</p>
<aside class="quote no-group" data-username="DanC" data-post="9" data-topic="410">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/77aa72/48.png" class="avatar"> DanC:</div>
<blockquote>
<p>Does supersample meen to resample with smaller spacing between slices with interpolation?</p>
</blockquote>
</aside>
<p>Yes.</p>
<p>When you have 20x difference between intra/inter-slice spacing, then most likely you cannot utilize all the information in the slice, so you have to use a spacing that is in between the smallest spacing vale - for 0.07x0.07x2mm spacing, something like 0.5mm should be good enough.</p>
<p>Do you register histology to US or MRI? Do you use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerProstate">SlicerProstate</a> or <a href="https://github.com/SlicerRt/SegmentRegistration">Segment registration</a> extensions? They are specifically developed for prostate registration between high-resolution and low-resolution images.</p>

---
