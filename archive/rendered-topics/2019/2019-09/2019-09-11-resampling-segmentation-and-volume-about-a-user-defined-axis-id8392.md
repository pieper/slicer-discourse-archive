# Resampling Segmentation and Volume about a User-Defined Axis For Plotting

**Topic ID**: 8392
**Date**: 2019-09-11
**URL**: https://discourse.slicer.org/t/resampling-segmentation-and-volume-about-a-user-defined-axis-for-plotting/8392

---

## Post #1 by @abniesen (2019-09-11 22:17 UTC)

<p>Hi,</p>
<p>I have segmented a CT scan of the proximal femur as shown below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28aebe03715d1201da6463406e3dfcc261ccaedf.png" alt="image" data-base62-sha1="5NTtU7gHzDq1mtX3wshIYKJsNkj" width="224" height="183"><br>
I am looking to plot the cross-sectional area of this segmentation along the axis of the femoral neck using SliceAreaPlot.py ((<a href="https://gist.github.com/lassoan/62370c6b0552f7df1111eb7fc37abfd2" class="inline-onebox" rel="noopener nofollow ugc">Example module that computes and plots the cross sectional area of each visible segment. Direction of cross-section can be picked. · GitHub</a>).<br>
Currently, the code only allows calculation in the coronal, axial, or sagittal planes.  Thus, I need help reorienting my segmentation and volume along the axis of the femoral neck.</p>
<p>For a first try, I first reoriented the axes by applying a linear transform to my segmentation and volume as shown below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5b107167f65b03a273296ca8db846c1bcd6fa51.png" alt="image" data-base62-sha1="nDM3SZOLGPOPECX0T9ugzmFP9df" width="295" height="296"><br>
I then applied the SlicePlotArea.py code. However, the plot did not take the transform into account and instead plotted the original axis.</p>
<p>I am looking for another method to try.  I believe I need to resample my segmentation and volume, but I’m not sure how to do this. When I tried using Resample Scalar/Vector/DWI Volume Module along with my transform, all of my views became black. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/152ac4b760a15996bb66026b443b347dc191da7c.png" alt="image" data-base62-sha1="31fEMAXvZEy5W7buUAUZO3bC5OI" width="352" height="261"></p>
<p>Please provide some help!</p>
<p>Thanks,<br>
Abby</p>

---

## Post #2 by @hherhold (2019-09-12 00:12 UTC)

<p>Did you try hardening the transform before running SliceAreaPlot?</p>

---

## Post #3 by @lassoan (2019-09-12 02:43 UTC)

<p>Since a linear transform is applied, hardening would not resample the volume.</p>
<p>A simple solution would be to create an ROI node, rotate it with a transform so that it is aligned with the axis directions that you need and use that in Crop volume module to crop/resample the volume.</p>
<p>You can set up the transform manually, using sliders and/or interactively moving/rotating in a 3D view (in Transforms module, enable Display / Interaction / Visible in 3D view). Or, create the ROI automatically from an open curve node (in recent Slicer Preview version) by dropping a curve point in the middle of the femur head, a second point along the femur, and copy-pasting this code into the Python console:</p>
<pre data-code-wrap="python"><code class="lang-python">femurLineNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsCurveNode")
femurToWorldMatrix = vtk.vtkMatrix4x4()
femurLineNode.GetCurvePointToWorldTransformAtPointIndex(0,femurToWorldMatrix)
femurToWorldTransform = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode")
femurToWorldTransform.SetAndObserveMatrixTransformToParent(femurToWorldMatrix)
roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLAnnotationROINode")
roiNode.SetXYZ(0, 0, 30)
roiNode.SetRadiusXYZ(40, 40, 60)
roiNode.SetAndObserveTransformNodeID(femurToWorldTransform.GetID())
</code></pre>
<p>Choose Open Curve on toolbar then click the first curve point:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0f2b2a4085c72b32de0f249dd4f699d72ec0311.png" data-download-href="/uploads/short-url/pfm0LW4k3Efk8qud1Zx9VH17UFb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0f2b2a4085c72b32de0f249dd4f699d72ec0311_2_439x499.png" alt="image" data-base62-sha1="pfm0LW4k3Efk8qud1Zx9VH17UFb" width="439" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0f2b2a4085c72b32de0f249dd4f699d72ec0311_2_439x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0f2b2a4085c72b32de0f249dd4f699d72ec0311_2_658x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0f2b2a4085c72b32de0f249dd4f699d72ec0311.png 2x" data-dominant-color="B4B4B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">734×835 89.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Go to a different slice, place the second contour point then right-click to finish the curve:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d83adebb6297156233e63f28bd5aaa357edb249b.jpeg" data-download-href="/uploads/short-url/uQRgfygQg9G3AkvBxBWsy8Ylbwn.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83adebb6297156233e63f28bd5aaa357edb249b_2_499x500.jpeg" alt="image" data-base62-sha1="uQRgfygQg9G3AkvBxBWsy8Ylbwn" width="499" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83adebb6297156233e63f28bd5aaa357edb249b_2_499x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83adebb6297156233e63f28bd5aaa357edb249b_2_748x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83adebb6297156233e63f28bd5aaa357edb249b_2_998x1000.jpeg 2x" data-dominant-color="A8A8B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1218×1219 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Copy-paste the code snippet above to automatically generate ROI:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42a0b69377455520c4a57fddbd79a015d2816c2b.jpeg" data-download-href="/uploads/short-url/9vpQ2Ui5MCCrJSH9yOuPAHSDTJx.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42a0b69377455520c4a57fddbd79a015d2816c2b_2_690x438.jpeg" alt="image" data-base62-sha1="9vpQ2Ui5MCCrJSH9yOuPAHSDTJx" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42a0b69377455520c4a57fddbd79a015d2816c2b_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42a0b69377455520c4a57fddbd79a015d2816c2b_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42a0b69377455520c4a57fddbd79a015d2816c2b_2_1380x876.jpeg 2x" data-dominant-color="CFCECF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1434 708 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Use Crop Volume module (you can leave all settings at default) to crop&amp;resample the volume using the oriented ROI:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc5c49b9cc6e9068aad0959b818351b9cadf1d0e.jpeg" data-download-href="/uploads/short-url/vroLIncqgLcnYqPIb0XvCuCD4n4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc5c49b9cc6e9068aad0959b818351b9cadf1d0e_2_690x438.jpeg" alt="image" data-base62-sha1="vroLIncqgLcnYqPIb0XvCuCD4n4" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc5c49b9cc6e9068aad0959b818351b9cadf1d0e_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc5c49b9cc6e9068aad0959b818351b9cadf1d0e_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc5c49b9cc6e9068aad0959b818351b9cadf1d0e_2_1380x876.jpeg 2x" data-dominant-color="999898"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1434 752 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can rotate slice views to align with volume axes by clicking pushpin icon at the top-left corner of the slice view controller and clicking “Rotate to volume plane” button.</p>
<p>You can then perform cross section analysis using this cropped volume.</p>

---

## Post #4 by @abniesen (2019-09-12 19:19 UTC)

<p>Thank you very much for the detailed response Andras!  I was able to get the SliceAreaPlot code to work along my defined axis using the methods you described.  I opted to manually set-up the ROI node and transform.</p>
<p>I greatly appreciate the help!</p>
<p>Best,<br>
Abby</p>

---
