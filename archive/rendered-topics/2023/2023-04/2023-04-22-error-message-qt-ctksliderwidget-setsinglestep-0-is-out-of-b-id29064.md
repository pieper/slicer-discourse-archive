---
topic_id: 29064
title: "Error Message Qt Ctksliderwidget Setsinglestep 0 Is Out Of B"
date: 2023-04-22
url: https://discourse.slicer.org/t/29064
---

# Error message:[Qt] ctkSliderWidget::setSingleStep() 0 is out of bounds. 0 100 1

**Topic ID**: 29064
**Date**: 2023-04-22
**URL**: https://discourse.slicer.org/t/error-message-qt-ctksliderwidget-setsinglestep-0-is-out-of-bounds-0-100-1/29064

---

## Post #1 by @Dexter777 (2023-04-22 21:12 UTC)

<p>Hi, when I’m drawing a closed curve on a surface mesh to cut out and create a new surface model, I am receiving the following message:<br>
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1</p>
<p>The code I’m using is:</p>
<h1><a name="p-93907-get-input-data-1" class="anchor" href="#p-93907-get-input-data-1" aria-label="Heading link"></a>Get input data</h1>
<p>curveNode = getNode(‘CC_5’)<br>
modelNode = getNode(‘Segment_1’)<br>
extractLargestPart = False</p>
<h1><a name="p-93907-get-vtk-data-objects-from-mrml-nodes-2" class="anchor" href="#p-93907-get-vtk-data-objects-from-mrml-nodes-2" aria-label="Heading link"></a>Get VTK data objects from MRML nodes</h1>
<p>curvePoints = curveNode.GetCurvePointsWorld()<br>
meshToClip = modelNode.GetMesh()  # we should apply transform to World</p>
<h1><a name="p-93907-clip-model-with-curve-3" class="anchor" href="#p-93907-clip-model-with-curve-3" aria-label="Heading link"></a>Clip model with curve</h1>
<p>loop = vtk.vtkSelectPolyData()<br>
loop.SetLoop(curvePoints)<br>
loop.GenerateSelectionScalarsOn()<br>
loop.SetInputData(meshToClip)<br>
loop.SetSelectionModeToLargestRegion()<br>
clip = vtk.vtkClipPolyData()<br>
clip.InsideOutOn()<br>
clip.SetInputConnection(loop.GetOutputPort())<br>
clip.GenerateClippedOutputOn()<br>
clip.Update()<br>
clippedOutput = clip.GetOutput() if extractLargestPart else clip.GetClippedOutput()</p>
<p>connectivity = vtk.vtkConnectivityFilter()<br>
connectivity.SetInputData(clippedOutput)<br>
connectivity.Update()<br>
clippedOutput2 = connectivity.GetOutput()</p>
<h1><a name="p-93907-remove-unused-points-4" class="anchor" href="#p-93907-remove-unused-points-4" aria-label="Heading link"></a>Remove unused points</h1>
<p>cleaner = vtk.vtkCleanPolyData()<br>
cleaner.SetInputData(clippedOutput2)<br>
cleaner.Update()<br>
cleanedClippedOutput = cleaner.GetOutput()</p>
<h1><a name="p-93907-save-result-to-new-node-5" class="anchor" href="#p-93907-save-result-to-new-node-5" aria-label="Heading link"></a>Save result to new node</h1>
<p>clippedModel = slicer.modules.models.logic().AddModel(cleanedClippedOutput)<br>
clippedModel.GetDisplayNode().SetActiveScalarName(“”)<br>
clippedModel.GetDisplayNode().BackfaceCullingOff()</p>
<p>Previously I was able to cut the skin surface out but the cut line was not close enough to where it needed to be. Trying again, I am receiving the error message.</p>
<p>Any suggestions?<br>
Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4ac0e9efaa4a02917168c99366bae5759c58895.png" data-download-href="/uploads/short-url/wCVuCELVEw8LQVcngzxX4wgXdbf.png?dl=1" title="Skin Model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4ac0e9efaa4a02917168c99366bae5759c58895_2_348x500.png" alt="Skin Model" data-base62-sha1="wCVuCELVEw8LQVcngzxX4wgXdbf" width="348" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4ac0e9efaa4a02917168c99366bae5759c58895_2_348x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4ac0e9efaa4a02917168c99366bae5759c58895.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4ac0e9efaa4a02917168c99366bae5759c58895.png 2x" data-dominant-color="A2A496"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skin Model</span><span class="informations">415×596 71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cc648568b775845db77bf0d12a8732f74dbec6a.png" data-download-href="/uploads/short-url/6o5Phywba2iXIIA9pClshEn06aS.png?dl=1" title="Error Message" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2cc648568b775845db77bf0d12a8732f74dbec6a_2_603x499.png" alt="Error Message" data-base62-sha1="6o5Phywba2iXIIA9pClshEn06aS" width="603" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2cc648568b775845db77bf0d12a8732f74dbec6a_2_603x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2cc648568b775845db77bf0d12a8732f74dbec6a_2_904x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cc648568b775845db77bf0d12a8732f74dbec6a.png 2x" data-dominant-color="BEB2BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error Message</span><span class="informations">1168×968 394 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Dexter777 (2023-04-25 23:39 UTC)

<p>The problem is having a green segmentation under the red model. I was hoping to use the green segmentation as a guide to show me where to cut the skin. The closed curve created can not find the red model to cut the surface model. If I turn off the green segmentation off I can cut the red surface as a model.</p>
<p>I am creating veterinary medical simulators which are then molded to create duplicates. It would be great to have a parametric function to create boxes/cubes with a draft on them to facilitate removal from the mold.<br>
Thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/769561dd4bacc2223558494777c5fdeb0c2b1c0c.png" data-download-href="/uploads/short-url/gV2ohe2syTumi7k2hBFy1tqZPkg.png?dl=1" title="Green Segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/769561dd4bacc2223558494777c5fdeb0c2b1c0c_2_319x500.png" alt="Green Segmentation" data-base62-sha1="gV2ohe2syTumi7k2hBFy1tqZPkg" width="319" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/769561dd4bacc2223558494777c5fdeb0c2b1c0c_2_319x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/769561dd4bacc2223558494777c5fdeb0c2b1c0c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/769561dd4bacc2223558494777c5fdeb0c2b1c0c.png 2x" data-dominant-color="768A92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Green Segmentation</span><span class="informations">453×708 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2aaefc373ffb751e61371022af68cf8aeec69dc2.png" data-download-href="/uploads/short-url/65AXo0JCl2ldXKO4KikW9kvvHuq.png?dl=1" title="Red Model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aaefc373ffb751e61371022af68cf8aeec69dc2_2_293x499.png" alt="Red Model" data-base62-sha1="65AXo0JCl2ldXKO4KikW9kvvHuq" width="293" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aaefc373ffb751e61371022af68cf8aeec69dc2_2_293x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aaefc373ffb751e61371022af68cf8aeec69dc2_2_439x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2aaefc373ffb751e61371022af68cf8aeec69dc2.png 2x" data-dominant-color="AD3D55"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Red Model</span><span class="informations">489×833 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
