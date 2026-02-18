# ROI to IJK coordinates

**Topic ID**: 2589
**Date**: 2018-04-14
**URL**: https://discourse.slicer.org/t/roi-to-ijk-coordinates/2589

---

## Post #1 by @zjx1805 (2018-04-14 21:36 UTC)

<p>I am trying to get iMin, iMax, jMin, jMax, kMin, kMax from some ROI node using Python script such that croppedVolume = dataVolume[kMin:kMax, jMin:jMax, iMin:iMax] and then I will perform some analysis on the cropped volume. What I know is that I can get the center and radius of ROI box in RAS coordinates by roiNode.GetXYZ() and roiNode.GetRadiusXYZ(). So I can get the RAS coordinates of center points of the 6 faces of the ROI box. Assuming the edges of ROI box are parallel to the RAS coordinate axes (which might not be true), I should be able to compute iMin, iMax, jMin, jMax, kMin, kMax with the help of dataVolumeNode.GetRAStoIJKMatrix(). For example, the converted ijk coordinates of the center points on left and right plane should have two same components and the differing component should give you iMin/iMax (or jMin/jMax or kMin/kMax). However, all three components I get are different. Then I saw the source code of VolumeClipWithROI <a href="https://github.com/PerkLab/SlicerVolumeClip/blob/master/VolumeClipWithRoi/VolumeClipWithRoi.py" rel="nofollow noopener">here</a> (starting from line 254), so I realized there might be another coordinate transform between ROI coordinates and volume RAS coordinates. But I get lost from there. So my questions are:</p>
<ol>
<li>Is there a way to compute a slice object (in the form of iMin, iMax, jMin, jMax, kMin, kMax or other) such that croppedVolume = dataVolume[sliceObject]? BTW, I don’t care about the interpolation at the boundary. So if the resulting ijk are not integers, rounding is perfectly fine with me.</li>
<li>What if the ROI box is rotated such that the edges of the box are no longer parallel with the RAS coordinate axes? I suppose a binary mask might be needed to indicate which portion of the original volume gets cropped?</li>
</ol>
<p>Any help is greatly appreciated!</p>

---

## Post #2 by @lassoan (2018-04-15 12:12 UTC)

<p>You can easily get any point’s position in any coordinate system by computing the transform between the coordinate systems (4x4 matrix) and multiply the point coordinates by the matrix.</p>
<p>The transformation chain: ROI -&gt; RAS (a.k.a. World) -&gt; Volume RAS -&gt; Volume IJK. You can get ROI to Volume RAS directly using <a href="http://apidocs.slicer.org/master/classvtkMRMLTransformNode.html#a5adb52ab1ade61f18dff88097a1ba17b">GetTransformBetweenNodes</a> and append the volumes RAS to IJK transform. See some information and examples here:</p>
<ul>
<li>
<a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a> - U-04 Coordinate transformations</li>
<li><a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/CoordinateSystemDefinitions.html#TransformationMatrix">PLUS Toolkit User’s Manual</a></li>
</ul>
<p>Points to transform: Probably the best is to transform the 8 corner points of the ROI (you compute the 8 point coordinates in ROI coordinate system and transform one by one to Volume IJK).</p>

---

## Post #3 by @lassoan (2018-04-15 12:29 UTC)

<p>What would you like to use the transformed ROI for? For images, it is often more efficient to crop the image with the ROI (to reduce the amount of data) - for example, using Crop volumes module.</p>
<p>If you need to define an arbitrarily shaped ROI, then you need to use image masks. You can create image masks using Segment editor module and export it to binary labelmap using Segmentations module.</p>

---

## Post #4 by @zjx1805 (2018-04-15 17:08 UTC)

<p>GetTransformBetweenNodes seems to be what I need! I saw one of your earlier post on GetTransformBetweenNodes <a href="https://discourse.slicer.org/t/transformation-graph-for-quick-calculation-of-concatenated-transforms/326/3">here</a>, so my code should probably look like this:</p>
<pre><code>transformMatrix = vtk.vtkMatrix4x4() # I think transforms between these coordinate systems should be linear?
a = getNode('myROI').GetParentTransformNode()
b = ?
slicer.vtkMRMLTransformNode().GetMatrixTransformBetweenNodes(a, b, transformMatrix)
ijkCoordinates = transformMatrix.MultiplyPoint(rasCoordinates of ROI points appended by 1)
</code></pre>
<p>But how should I define b? Since it represents the ijk coordinates to index the data matrix and it does not have a corresponding node in Slicer…</p>
<p>To your second question, the reason why I didn’t want to use Crop volumes module is that I will do some calculation on the cropped volume, change its value, and eventually put it back to the original volume (so I need to get the ijk coordinates to know where to put it back)</p>
<p>Thanks!</p>

---

## Post #5 by @lassoan (2018-04-15 18:58 UTC)

<p>a = ROI node<br>
b = volume node<br>
Once you have the matrix between a and b, multiply it with Volume RAS to IJK matrix (you can get this matrix from the volume node) to compute ROI to IJK. Pay attention to correct ordering (multiplication is not commutative for matrices) and if you need to invert matrices.</p>
<p>Cropping does not change physical position of voxels, so you can always copy the contents back to the original volume.</p>

---

## Post #6 by @zjx1805 (2018-04-15 19:24 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  I updated my code and now I get volume RAS coordinates of the center point in the format of (a1,b,c),(a2,b,c),(a,b1,c),(a,b2,c),(a,b,c1),(a,b,c2), which is as expected. However, when I applied RAS to IJK transformation, none of the three components are the same anymore. So I guess the volume RAS coordinates are not aligned with data matrix ijk axes and so I cannot use <code>croppedVolume = dataVolume[kMin:kMax, jMin:jMax, iMin:iMax]</code>.</p>
<p>From your description, cropping seems to perfectly meet my needs. However, I couldn’t find any instructions on how to run the cropping module in python except <a href="https://github.com/PerkLab/SlicerVolumeClip/blob/master/VolumeClipWithRoi/VolumeClipWithRoi.py" rel="nofollow noopener">this</a> ClipVolumeWithRoi script. I am wondering if there is a way to do things like this:</p>
<pre><code>croppedVolumeNode = crop(volumeNode, roiNode)
Perform some calculation on cropped volume...
volumeNode.update(croppedVolumeNode) # put it back to the original volume
</code></pre>
<p>Thanks!</p>

---

## Post #7 by @lassoan (2018-04-17 03:23 UTC)

<p>You can use <a href="http://apidocs.slicer.org/master/classvtkSlicerCropVolumeLogic.html#a1ae018eafbecd7af47ff82f191f133d8"><code>slicer.modules.cropvolume.logic().CropInterpolated(...)</code></a> or <a href="http://apidocs.slicer.org/master/classvtkSlicerCropVolumeLogic.html#ab1b21a6baf2512d8f1e008cbea12be04"><code>slicer.modules.cropvolume.logic().CropVoxelBased(...)</code></a> method.</p>

---

## Post #8 by @zjx1805 (2018-04-17 05:59 UTC)

<p>Thank you. But may I ask how to put the cropped volume back? I see that the size of the cropped volume changes but the spatial location doesn’t. So is there a function I can use to replace the part of the original volume with the modified cropped volume? Thanks!</p>

---

## Post #9 by @lassoan (2018-04-17 13:53 UTC)

<p>There are many ways to do this. If you have a rectangular ROI then you can use SimpleITK’s PasteImageFilter (it is available in Simple Filters module with a GUI, so you can find out how to use it). If you have an image mask, then create two images where parts to be replaced are set to a very small value then combine them using maximum operation (using numpy, ITK, or VTK filters, or Slicer modules).</p>

---

## Post #10 by @zjx1805 (2018-04-17 18:05 UTC)

<p>I am sorry to bother you again on this but I tried the Simple Filters module and I am confused about DestinationIndex. I read the documentation on the PasteImageFilter and thought it should be one of the 8 corner coordinates of the ROI box expressed in volume RAS coordinates. I tried all 8 of them but none of them works (not even close). Could you please elaborate on how to compute DestinationIndex from the roiNode and volumeNode? BTW, I am using rectangular ROI hand dragged in 3D slicer.<br>
Thanks!</p>

---

## Post #11 by @lassoan (2018-04-17 21:34 UTC)

<p>Maybe <a class="mention" href="/u/blowekamp">@blowekamp</a> can help. If not, then you need to figure this out from SimpleITK documentation.</p>

---

## Post #12 by @blowekamp (2018-04-18 14:05 UTC)

<p>The first image it the “destination” larger volume, the second image is the “source” image where the region is read from. The ITK documentation is here:<br>
<a href="https://itk.org/Doxygen/html/classitk_1_1PasteImageFilter.html" class="onebox" target="_blank" rel="nofollow noopener">https://itk.org/Doxygen/html/classitk_1_1PasteImageFilter.html</a></p>
<p>This filter operates in index space. I’d start by leaving the SourceIndex, and Destination index as (0,0,0), then just specify the Source size. This will result in the filter just copying one corner from the source image to the destination image. Make sure you create a new output volume and select the proper input volumes.</p>

---

## Post #13 by @zjx1805 (2018-04-19 02:10 UTC)

<p>Hello <a class="mention" href="/u/blowekamp">@blowekamp</a>, I figured out the DestinationIndex issue, it was because when I created a new volume node in Python, I forgot to set the IJKToRASMatrix of it to be the same as that of the original volume. But now I have another problem here: after I put back the cropped volume back to the original volume, it seems that there is a small offset (looks like 1 pixel?) as below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5d1f43f33782636147b173bf1f40819b4d0b8eb.jpeg" data-download-href="/uploads/short-url/wN5afomEZOsCzwzzCnFvz83uWTN.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5d1f43f33782636147b173bf1f40819b4d0b8eb_2_690x302.jpg" alt="image" data-base62-sha1="wN5afomEZOsCzwzzCnFvz83uWTN" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5d1f43f33782636147b173bf1f40819b4d0b8eb_2_690x302.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5d1f43f33782636147b173bf1f40819b4d0b8eb_2_1035x453.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5d1f43f33782636147b173bf1f40819b4d0b8eb_2_1380x604.jpg 2x" data-dominant-color="8C8D99"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×841 440 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What I did was:</p>
<ol>
<li>Open the built-in MRHead image</li>
<li>Drag an arbitrary ROI box</li>
<li>Using the crop volume module to crop the volume. I have also tried using the following code with the same result:<br>
<code>slicer.modules.cropvolume.logic().CropVoxelBased(getNode('AnnotationROI_30'), getNode('MRHead'), croppedVolumeNode)</code><br>
where <code>croppedVolumeNode</code> is some scalar volume node I created using scripts.</li>
<li>In the simple filters module, set the first input volume as MRHead, the second as MRHead cropped, source size is the same as the size of the cropped volume. Source and destination index are kept as (0,0,0). I also chose to create a new volume as the output.</li>
</ol>
<p>I am wondering if I have done any steps wrong that produce this slight offset. And also is there a way to programmatically invoke the PasteImageFilter() in Python? I read the documentation page and found out the following code is needed:</p>
<pre><code>myFilter = PasteImageFilter()
myFilter.SetDebug(False)
myFilter.SetDestinationIndex((0, 0, 0))
myFilter.SetNumberOfThreads(8)
myFilter.SetSourceIndex((0, 0, 0))
myFilter.SetSourceSize((194, 80, 129))
myFilter.SetSourceImage(??) # Should I put node or array here?
myFilter.SetDestinationImage(??)
</code></pre>
<p>But obviously this gives an error saying that PasteImageFilter() is not found. I also tried to import itk by using <code>import itk</code> but returns a module not found error. So could you please help me complete this snippet? Thanks!</p>

---

## Post #14 by @blowekamp (2018-04-19 13:04 UTC)

<p>So the SimpleFilters module utilizes <a href="https://github.com/SimpleITK/SimpleITK" rel="nofollow noopener">SimpleITK</a> for python. The interface is very similar to ITK’s but is designed to have more of a native Python feel, and compatible with may Python intrinsic types. You can find the SimpleITK documentation for the <a href="https://itk.org/SimpleITKDoxygen/html/classitk_1_1simple_1_1PasteImageFilter.html" rel="nofollow noopener">PasteImageFilter here</a>. SimpleITK also has a <a href="https://itk.org/SimpleITKDoxygen/html/namespaceitk_1_1simple.html#a49f5bb557f802ce6acc94f4ad10e6838" rel="nofollow noopener">procedural interface</a>. Yesterday I did notice that the image inputs were not named. The first argument is the “DestinationImage”, while the second is the “SourceImage”. I have a<a href="https://github.com/SimpleITK/SimpleITK/pull/443/files" rel="nofollow noopener">pull request</a> that will improve this.</p>
<p>Your simpleITK code would look something like this:</p>
<pre><code class="lang-auto">import SimpleITK as sitk
myFilter = sitk.PasteImageFilter()
myFilter.SetDebug(False)
myFilter.SetDestinationIndex((0, 0, 0))
myFilter.SetNumberOfThreads(8)
myFilter.SetSourceIndex((0, 0, 0))
myFilter.SetSourceSize((194, 80, 129))
output = myFilter.Execute(destinationImage, sourceImage)
</code></pre>
<p>This describes how to get the images from Slicer into SimpleITK and python: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK</a></p>
<p>Regarding your off by one error. I would closing inspect the image’s meta data, and the coordinations of the ROI. There may be slight differences in the physical locations of the image’s pixels that are causing problems, or look for rounding issues.</p>

---
